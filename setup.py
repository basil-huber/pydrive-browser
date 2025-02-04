from setuptools import setup
from os import environ

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='PyDriveBrowser',
      version=environ.get('VERSION', '0.0.0').lstrip('v'),
      description='Command line file Browser for Google Drive',
      long_description=long_description,
      long_description_content_type='text/markdown',
      keywords='Google Drive Command Line Tool',
      author='Basil Huber',
      author_email='basil.huber@gmail.com',
      url='https://github.com/basil-huber/PyDriveBrowser',
      project_urls={'Bug Tracker': 'https://github.com/basil-huber/PyDriveBrowser/issues'},
      license='Anti-996',
      packages=['pydrivebrowser'],
      install_requires=['pydrive2==1.20.0', 'pick==2.4.0', 'oauth2client==4.1.3'],
      zip_safe=False)
