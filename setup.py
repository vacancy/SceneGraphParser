#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : setup.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 12/30/2021
#
# This file is part of SceneGraphParser.
# Distributed under terms of the MIT license.

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='SceneGraphParser',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',

    description='A python toolkit for parsing sentences (natural language) into scene graphs (symbolic representations).',
    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires=[
        "spacy>=3.2.0",
        "tabulate>=0.8.9"
    ],

    # The project's main homepage.
    url='',

    # Author details
    author='',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
    ],

    # What does your project relate to?
    keywords='nlp',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=["tools", "example"]),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=["tensorflow==1.11.0","tensorflow-gpu==1.11.0", "pillow==5.4.1", "numpy"],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:

    # $ pip install -e .[dev,test]
    # extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    # },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # Attention: the root folder (used as keys) in package data must be dot separated if it goes deeper and not with /
    # example src.sng_parser instead of src/sng_parser
    package_data={
        'sng_parser': ["_data/*.txt"],
    },

    # data_files=[('project/configuration', ['project/configuration/configuration.ini.template'])],

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file.txt'])],
)

