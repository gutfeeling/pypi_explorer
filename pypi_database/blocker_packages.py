import os
import csv

os.environ["DJANGO_SETTINGS_MODULE"] = "pypi_database.settings"

import django
django.setup()

import arrow
from django.db.models import Q

from package_info.models import PackageInfo

if __name__ == "__main__":

    one_year_ago = arrow.now().replace(years = -1).datetime.date()

    blocker_packages = PackageInfo.objects.exclude(
        has_classifiers = False).exclude(
        last_release_date = None).exclude(
        last_release_date__lt = one_year_ago).filter(
        Q(development_status = "Development Status :: 5 - Production/Stable") |
        Q(development_status = "Development Status :: 6 - Mature")).exclude(
        python3_compatible = True).exclude(
        last_release_size_source = None).filter(
        last_release_size_source__gt = 100000)

    csv_data = [["Package Name", "Last Release Date", "Keywords"]]

    for package in blocker_packages.order_by("-total_downloads"):
        csv_data.append([package.name, package.last_release_date,
            package.keywords])

    csv_file = "blocker_packages_2016.csv"
    with open(csv_file, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(csv_data)
