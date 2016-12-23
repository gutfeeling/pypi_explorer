import time
import os

os.environ["DJANGO_SETTINGS_MODULE"] = "pypi_database.settings"

import requests
from bs4 import BeautifulSoup

import django
django.setup()

from packages.models import Package

def get_all_pypi_packages():
    response = requests.get("https://pypi.python.org/simple/")
    html_doc = response.text
    html_soup = BeautifulSoup(html_doc, "html.parser")
    links = html_soup.find_all("a")
    for link in links:
        yield link.string

def get_package_info(package_name):
    url = "http://pypi.python.org/pypi/{0}/json".format(package_name)
    response = requests.get(url)
    if response.status_code != 200:
        raise IOError
    return response.text

if __name__ == "__main__":

    print("Starting sync...")

    packages = [package for package in get_all_pypi_packages()]

    existing_packages = [package.name for package in Package.objects.all()]

    #num_of_existing_packages = len(existing_packages)
    delete_counter = 0

    for package in existing_packages:
        try:
            packages.remove(package)
        except ValueError:
            Package.objects.get(name = package).delete()
            #num_of_existing_packages -= 1
            delete_counter += 1

    add_counter = 1

    for package in packages:
        try:
            metadata = get_package_info(package)
            package_db_entry = Package(name = package,
               metadata = get_package_info(package))
            package_db_entry.save()
            add_counter += 1
        except IOError:
            print("Could not download metadata for package {0}"
                " (does it exist?)".format(package))

        #if counter % 1000 == 0:
        #    print("Downloaded {0} new packages, total {1} packages in the"
        #        " database.".format(counter, counter + num_of_existing_packages))

    print("Added {0} new packages. Deleted {1} existing packages.".format(
        add_counter -1, delete_counter))
    print("Finished sync.")
