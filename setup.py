#!/usr/bin/env python3

from setuptools import setup, find_packages


# README.md
with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

# requirements.txt
with open("requirements.txt", "r") as _requirements:
    requirements = list(map(str.strip, _requirements.read().split("\n")))

setup(
    name="python-hdwallet",
    version="0.1.1",
    description="The implementation of Hierarchical Deterministic (HD) wallet generator for cryptocurrencies.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="ISC",
    author="Meheret Tesfaye",
    author_email="meherett@zoho.com",
    url="https://github.com/meherett/wallet",
    keywords=["hd", "wallet", "cryptocurrencies", "bip32", "bip44"],
    python_requires=">=3.6,<4",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        "tests": [
            "pytest>=6.0.1,<7",
            "pytest-cov>=2.10.1,<3"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
