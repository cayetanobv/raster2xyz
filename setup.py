# -*- coding: utf-8 -*-

# This file is part of Raster2xyz.

# Licensed under the GPLv2 license:
# https://www.gnu.org/licenses/gpl-2.0.txt
# Copyright (c) 2015-2016, Cayetano Benavent <cayetano.benavent@geographica.gs>

from setuptools import setup, find_packages


# Get the long description from README file.
# Before upload a new version run rstgenerator.sh
# to update Readme reStructuredText file from
# original Readme markdown file.
with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='raster2xyz',
    version='0.1.2',

    description='Alternative and faster (vectorized) version of gdal2xyz.py',
    long_description=long_description,

    author='Cayetano Benavent',
    author_email='cayetano.benavent@geographica.gs',

    scripts=['bin/raster2xyz'],

    # The project's main homepage.
    url='http://github.com/cayetanobv/raster2xyz',

    # Licensed under the GPLv2 license:
    # https://www.gnu.org/licenses/gpl-2.0.txt
    license='GPLv2',

    # According to: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: GIS'
    ],

    keywords='raster GIS xyz gdal',

    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'numpy',
        'pandas',
        'GDAL'
    ]

)
