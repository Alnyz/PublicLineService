from setuptools import setup, find_packages

with open("README.md", "r") as fp:
	long_desc = fp.read()
	
setup(
	author="Dyseo",
	author_email="katro.coplax@gmail.com",
	name="LineService",
	version="0.10.0",
	packages=find_packages(),
	description="Line Messaging protocol for Python",
	long_description=long_desc,
	long_description_content_type="text/markdown",
	url="https://github.com/dyseo/LineService",
	keywords="frugal thrift line lineservice",
	install_requires=['frugal'],
	classifiers=[
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: Apache Software License 2.0 (Apache-2.0)",
		"Topic :: Software Development :: Libraries :: Python Modules"
	]
)