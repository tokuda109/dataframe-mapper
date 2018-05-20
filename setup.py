
import re
import ast
from setuptools import find_packages, setup

version_re = re.compile(r'__version__\s+=\s+(.*)')

with open("dfmapper/__init__.py", "rb") as f:
    version = str(ast.literal_eval(version_re.search(
        f.read().decode('utf-8')
    ).group(1)))

with open("README.md") as f:
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
        "pandas>=0.20.0"
    ],
    extras_require={
        'test': [
            'pytest==3.5.1'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
