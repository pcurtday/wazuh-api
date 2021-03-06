#!/usr/bin/env python

# Created by Wazuh, Inc. <info@wazuh.com>.
# This program is a free software; you can redistribute it and/or modify it under the terms of GPLv2

from setuptools import setup

# Install the package locally: python setup.py install
# Install the package dev: python setup.py develop

setup(name='wazuh',
      version='0.1',
      description='OSSEC control with python',
      url='https://github.com/wazuh',
      author='Wazuh',
      author_email='hello@wazuh.com',
      license='GPLv2',
      packages=['wazuh'],
      install_requires=[
          'xmljson',
      ],
      zip_safe=False)
