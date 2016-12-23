# PyPI Explorer
### Explore the [Python Package Index](https://pypi.python.org/pypi)

### Description

Ever wanted to explore the Python Package Index? If yes, this repository will get you started quickly. It includes scripts for
downloading the metadata of all packages in PyPI, functions for extracting important pieces of information from this metadata
and lots more. 

Recently, I have used it to analyze Python 3 support of packages in PyPI.

### Setup

1. Install the requirements 

   ```
   pip install -r requirements.txt
   ```
2. Setup the Django project

   ```
   cd pypi_database
   python manage.py makemigrations
   python manage.py migrate
   ```

### Obtain the 1 GB dataset

This project analyzes package metadata for all packages in PyPI. The dataset can be obtained in two ways:

1. The fast way is to [download](https://drive.google.com/open?id=0B9nABrt15_W5UUZJLVFRMWpvMEE) the sqlite database from Google Drive first. After downloading it, put it inside the 
pypi_database folder. If you wish to update it with the latest information, then run the following command.
    ```
    python download_metadata.py
    ```

2. The slow way is to download the data directly from PyPI and process it yourself by executing two commands. 
Note that the first job may take a lot of time to complete.
    ```
    python download_metadata.py
    python process_data.py
    ```
    
### What's in the database?

The database has two major tables. The corresponding Django models are called `packages.models.Package` and  
`package_info.models.PackageInfo`.
The first model stores the raw data.  The second model stores processed data, ready for analysis. 
In the following example, we will explore the fields of these models, starting with `Package`.

```python
python manage.py shell
>>> import json
>>> from packages.models import Package
>>> maya = Package.objects.get(name = "maya")  # one field is called "name" and stores the name of the package
>>> metadata_json = json.loads(maya.metadata)  # the other field is called "metadata" and stores the metadata as a string
>>> print(metadata_json)                       # this is how the metadata looks like
{'info': {'_pypi_hidden': False,
  '_pypi_ordering': 2,
  'author': 'Kenneth Reitz',
  'author_email': 'me@kennethreitz.com',
  'bugtrack_url': None,
  'cheesecake_code_kwalitee_id': None,
  'cheesecake_documentation_id': None,
  'cheesecake_installability_id': None,
  'classifiers': [],
  'description': "Maya: Datetime for Humans™ ..."
  'download_url': '',
  'downloads': {'last_day': 0, 'last_month': 0, 'last_week': 0},
  'home_page': 'https://github.com/kennethreitz/maya',
  'keywords': '',
  'license': 'MIT',
  'maintainer': '',
  'maintainer_email': '',
  'name': 'maya',
  'package_url': 'http://pypi.python.org/pypi/maya',
  'platform': '',
  'release_url': 'http://pypi.python.org/pypi/maya/0.1.1',
  'requires_python': '',
  'summary': 'Datetimes for Humans.',
  'version': '0.1.1'},
 'releases': {'0.0.0': [{'comment_text': '',
    'downloads': 217,
    'filename': 'maya-0.0.0.tar.gz',
    'has_sig': False,
    'md5_digest': '9671d718ba2e0e543117c038c056244d',
    'packagetype': 'sdist',
    'path': '16/57/6c61f6b1c9e5fff98fdac0cbcd274b674104a354b051329083f76c92d4e3/maya-0.0.0.tar.gz',
    'python_version': 'source',
    'size': 1822,
    'upload_time': '2016-12-16T18:33:57',
    'url': 'https://pypi.python.org/packages/16/57/6c61f6b1c9e5fff98fdac0cbcd274b674104a354b051329083f76c92d4e3/maya-0.0.0.tar.gz'}],
  '0.1.0': [{'comment_text': '',
    'downloads': 0,
    'filename': 'maya-0.1.0-py2-none-any.whl',
    'has_sig': False,
    'md5_digest': '4449dcc8503e8e3f8a620301395cf7f0',
    'packagetype': 'bdist_wheel',
    'path': '46/7b/c00d9dde952ee04eea3c8d8e66c524b71773167b9ed6212d6d0c9618c880/maya-0.1.0-py2-none-any.whl',
    'python_version': '2.7',
    'size': 3902,
    'upload_time': '2016-12-18T07:20:55',
    'url': 'https://pypi.python.org/packages/46/7b/c00d9dde952ee04eea3c8d8e66c524b71773167b9ed6212d6d0c9618c880/maya-0.1.0-py2-none-any.whl'},
   {'comment_text': '',
    'downloads': 0,
    'filename': 'maya-0.1.0.tar.gz',
    'has_sig': False,
    'md5_digest': 'ff477e7facee99405e8845189edaedeb',
    'packagetype': 'sdist',
    'path': '55/60/353c21fe84b482d225dd223de50d6a922e5295afe93d3b2d78deec3e1120/maya-0.1.0.tar.gz',
    'python_version': 'source',
    'size': 2260,
    'upload_time': '2016-12-18T07:20:54',
    'url': 'https://pypi.python.org/packages/55/60/353c21fe84b482d225dd223de50d6a922e5295afe93d3b2d78deec3e1120/maya-0.1.0.tar.gz'}],
  '0.1.1': [{'comment_text': '',
    'downloads': 0,
    'filename': 'maya-0.1.1-py2-none-any.whl',
    'has_sig': False,
    'md5_digest': '5c6cd9d7ee2a311a0e86ed4ec0cb5602',
    'packagetype': 'bdist_wheel',
    'path': '31/9d/7e3763f2069066ed30f7c030595900f926f89be28989ad37485fa6fe632b/maya-0.1.1-py2-none-any.whl',
    'python_version': '2.7',
    'size': 5806,
    'upload_time': '2016-12-18T17:43:41',
    'url': 'https://pypi.python.org/packages/31/9d/7e3763f2069066ed30f7c030595900f926f89be28989ad37485fa6fe632b/maya-0.1.1-py2-none-any.whl'},
   {'comment_text': '',
    'downloads': 0,
    'filename': 'maya-0.1.1.tar.gz',
    'has_sig': False,
    'md5_digest': '9354e57c845b60dc5ca3e00c490082b4',
    'packagetype': 'sdist',
    'path': 'a4/6d/737ac16cd7710c58512c888c5f382da6b4cdcc9ab9b790f9e5f6514a3c64/maya-0.1.1.tar.gz',
    'python_version': 'source',
    'size': 3984,
    'upload_time': '2016-12-18T17:43:40',
    'url': 'https://pypi.python.org/packages/a4/6d/737ac16cd7710c58512c888c5f382da6b4cdcc9ab9b790f9e5f6514a3c64/maya-0.1.1.tar.gz'}]},
 'urls': [{'comment_text': '',
   'downloads': 0,
   'filename': 'maya-0.1.1-py2-none-any.whl',
   'has_sig': False,
   'md5_digest': '5c6cd9d7ee2a311a0e86ed4ec0cb5602',
   'packagetype': 'bdist_wheel',
   'path': '31/9d/7e3763f2069066ed30f7c030595900f926f89be28989ad37485fa6fe632b/maya-0.1.1-py2-none-any.whl',
   'python_version': '2.7',
   'size': 5806,
   'upload_time': '2016-12-18T17:43:41',
   'url': 'https://pypi.python.org/packages/31/9d/7e3763f2069066ed30f7c030595900f926f89be28989ad37485fa6fe632b/maya-0.1.1-py2-none-any.whl'},
  {'comment_text': '',
   'downloads': 0,
   'filename': 'maya-0.1.1.tar.gz',
   'has_sig': False,
   'md5_digest': '9354e57c845b60dc5ca3e00c490082b4',
   'packagetype': 'sdist',
   'path': 'a4/6d/737ac16cd7710c58512c888c5f382da6b4cdcc9ab9b790f9e5f6514a3c64/maya-0.1.1.tar.gz',
   'python_version': 'source',
   'size': 3984,
   'upload_time': '2016-12-18T17:43:40',
   'url': 'https://pypi.python.org/packages/a4/6d/737ac16cd7710c58512c888c5f382da6b4cdcc9ab9b790f9e5f6514a3c64/maya-0.1.1.tar.gz'}]}
```
The second model `PackageInfo` stores processed data in its fields.
```python
python manage.py shell
>>> from package_info.models import PackageInfo
>>> arrow = PackageInfo.objects.get(name = "arrow")
>>> print(arrow.has_classifiers) # indicates if trove classifiers are present in the metadata
True
>>> print(arrow.python3_compatible) 
True
>>> print(arrow.total_downloads)
1517293
>>> print(arrow.last_release_date)
2016-11-30
>>> print(arrow.last_release_size_source) # size of the gzipped archive
86506
>>> print(arrow.last_release_size_wheel) # size of the wheel, if it exists
None
>>> print(arrow.development_status) # development status trove classifier
Development Status :: 4 - Beta
>>> print(arrow.keywords) # keywords associated with the package, if any
>>>
```

### Analysis of Python 3 support for actively developed production ready packages

This example jupyter notebook analyzes Python 3 support for actively developed, production ready packages using the
data in the database. You can use it as a starting point or inspiration for your exploration of PyPI.
