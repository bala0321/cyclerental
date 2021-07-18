# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in cyclerental/__init__.py
from cyclerental import __version__ as version

setup(
	name='cyclerental',
	version=version,
	description='Rents cycles',
	author='Hari',
	author_email='hari@hari.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
