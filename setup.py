#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="valideer",
    version="0.4.1",
    description="Lightweight data validation and adaptation library for Python",
    long_description=open("README.rst").read(),
    url="https://github.com/podio/valideer",
    author="George Sakkis",
    author_email="george.sakkis@gmail.com",
    packages=find_packages(),
    install_requires=["decorator"],
    test_suite="valideer.tests",
    platforms=["any"],
    keywords="validation adaptation typechecking jsonschema",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)
