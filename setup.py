#!/usr/bin/env python3

from setuptools import (
    setup, find_packages
)

# README.md
with open("README.md", "r", encoding="utf-8") as readme:
    long_description: str = readme.read()

# requirements.txt
with open("requirements.txt", "r") as _requirements:
    requirements: list = list(map(str.strip, _requirements.read().split("\n")))

setup(
    name="hdwallet",
    version="1.3.1",
    description="Python-based library for the implementation of a "
                "hierarchical deterministic wallet generator for more than 140+ multiple cryptocurrencies.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="ISCL",
    author="Meheret Tesfaye",
    author_email="meherett@zoho.com",
    url="https://github.com/meherett/python-hdwallet",
    keywords=["cryptography", "hd", "bip32", "bip44", "bip39", "wallet", "cryptocurrencies"],
    python_requires=">=3.6,<4",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        "tests": [
            "pytest>=6.2.2,<7",
            "pytest-cov>=2.11.1,<3"
        ],
        "docs": [
            "sphinx>=3.5.1,<4",
            "sphinx-rtd-theme>=0.5.1,<1"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
