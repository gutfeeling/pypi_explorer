import os
import json

os.environ["DJANGO_SETTINGS_MODULE"] = "pypi_database.settings"

import django
django.setup()

from packages.models import Package
from package_info.models import PackageInfo
from data_helpers import (has_classifiers, package_is_python3_compatible,
    get_total_downloads, get_last_release_date, get_last_release_size_source,
    get_last_release_size_wheel, get_development_status, get_keywords)

if __name__ == "__main__":
    PackageInfo.objects.all().delete()
    packages = [package for package in Package.objects.all()]
    package_info_list = []
    for package in packages:
        metadata_json = json.loads(package.metadata)
        new_package_info = PackageInfo(name = package.name,
            has_classifiers = has_classifiers(metadata_json),
            python3_compatible = package_is_python3_compatible(metadata_json),
            total_downloads = get_total_downloads(metadata_json),
            last_release_date = get_last_release_date(metadata_json),
            last_release_size_source = get_last_release_size_source(
                metadata_json),
            last_release_size_wheel = get_last_release_size_wheel(
                metadata_json),
            development_status = get_development_status(metadata_json),
            keywords = get_keywords(metadata_json))

        package_info_list.append(new_package_info)

        if len(package_info_list) % 10000 == 0:
            PackageInfo.objects.bulk_create(package_info_list)
            package_info_list = []

    PackageInfo.objects.bulk_create(package_info_list)
