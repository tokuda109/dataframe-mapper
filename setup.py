# -*- coding: utf-8 -*-

import re
import ast
from setuptools import find_packages, setup

VERSION_RE = re.compile(r'__version__\s+=\s+(.*)')

with open("dfmapper/__init__.py", "rb") as f:
    version = str(ast.literal_eval(VERSION_RE.search(
        f.read().decode('utf-8')
    ).group(1)))

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="dataframe-mapper",
    version=version,
    description="Object-oriented pandas DataFrame mapper.",
    long_description=long_description,
    keywords="pandas",
    author="Tsuyoshi Tokuda",
    author_email="tokuda109@gmail.com",
    url="https://pypi.org/project/dataframe-mapper/",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "pandas>=0.23.0"
    ],
    extras_require={
        'lint': [
            'pylint==1.9.1'
        ],
        'test': [
            'pytest==3.5.1'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
