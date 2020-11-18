from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cerebuswrapper',
    version='0.1.1',
    description='A thin convenience wrapper around Cerelink cerebus.cbpy',
    long_description=long_description,
    url='https://github.com/charlesincharge/cerebuswrapper',
    author='Chadwick Boulay',
    author_email='chadwick.boulay@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['cerebus', 'loguru']
)
