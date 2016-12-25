import json
import re

import arrow

def package_is_python3_compatible(metadata_json):
    for entry in metadata_json["info"]["classifiers"]:
        if re.search("Python :: 3", entry) is not None:
            return True
    return False

def get_total_downloads(metadata_json):
    total_downloads = 0
    releases = metadata_json["releases"]
    for key in releases:
        for entry in releases[key]:
            try:
                total_downloads += int(entry["downloads"])
            except KeyError:
                pass

    return total_downloads

def get_last_release_size_source(metadata_json):
    for entry in metadata_json["urls"]:
        if entry["packagetype"] == "sdist":
            return entry["size"]
    return None

def get_last_release_size_wheel(metadata_json):
    for entry in metadata_json["urls"]:
        if entry["packagetype"] == "bdist_wheel":
            return entry["size"]
    return None

def get_last_release_date(metadata_json):
    try:
        last_release_date_timestamp = metadata_json["urls"][0]["upload_time"]
    except IndexError:
        return None
    arrow_last_release_date = arrow.get(last_release_date_timestamp)
    date = arrow_last_release_date.datetime.date()
    return date

def get_development_status(metadata_json):
    for entry in metadata_json["info"]["classifiers"]:
        if re.search("Development Status", entry) is not None:
            return entry
    return None

def has_classifiers(metadata_json):
    if metadata_json["info"]["classifiers"] == []:
        return False
    return True

def get_keywords(metadata_json):
    return metadata_json["info"]["keywords"]

def package_has_python2_classifier(metadata_json):
    for entry in metadata_json["info"]["classifiers"]:
        if re.search("Python :: 2", entry) is not None:
            return True
    return False

def get_first_release_date(metadata_json):
    releases = metadata_json["releases"]
    dates = []
    for key in releases:
        try:
            dates.append(arrow.get(releases[key][0]["upload_time"]))
        except IndexError:
            pass
    if dates == []:
        return None
    return min(dates).datetime.date()    
