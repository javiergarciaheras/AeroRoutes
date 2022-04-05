#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='aeroroutes',         # How you named your package folder (MyLib)
  packages=['aeroroutes'],   # Chose the same as "name"
  version='0.0.1',      # Start with a small number and increase it with every change you make
  license='lgpl-3.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description='Library to compute the main features in aircraft routes',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Javier García-Heras',                   # Type in your name
  author_email = 'gcarrete@ing.uc3m.es',      # Type in your E-Mail
  url='https://github.com/javiergarciaheras/AeroRoutes',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/javiergarciaheras/AeroRoutes/archive/v_01.tar.gz',    # I explain this later on
  keywords=['Routes', 'Navigation', 'Loxodrome', 'Orthodrome', 'Trajectories'],   # Keywords that define your package best
  install_requires=[
          'numpy',
      'matplotlib',
      'mpl_toolkits.basemap',
      ],
  include_package_data=True,
  tests_require=["pytest"],
  zip_safe=False,
  classifiers=[ # Chose the classifiers from here: https://pypi.org/classifiers/
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Education',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',   # Again, pick a license
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5', #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)