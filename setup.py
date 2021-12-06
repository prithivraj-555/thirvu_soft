from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in thirvu_soft/__init__.py
from thirvu_soft import __version__ as version

setup(
	name="thirvu_soft",
	version=version,
	description="doctypecreation",
	author="prithiv",
	author_email="prithivrajthangadurai@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
