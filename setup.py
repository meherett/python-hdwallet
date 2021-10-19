#!/usr/bin/env python3

from setuptools import (
    setup, find_packages
)

import hdwallet

# README.md
with open("README.md", "r", encoding="utf-8") as readme:
    long_description: str = readme.read()

# requirements.txt
with open("requirements.txt", "r") as _requirements:
    requirements: list = list(map(str.strip, _requirements.read().split("\n")))

setup(
    name="hdwallet",
    version=hdwallet.__version__,
    description=hdwallet.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=hdwallet.__license__,
    author=hdwallet.__author__,
    author_email=hdwallet.__email__,
    url="https://github.com/meherett/python-hdwallet",
    keywords=[
        "cryptography", "cli", "wallet", "bip32", "bip44", "bip39", "hdwallet", "cryptocurrencies", "bitcoin", "ethereum"
    ],
    entry_points={
        "console_scripts": ["hdwallet=hdwallet.cli.__main__:main"]
    },
    python_requires=">=3.6,<4",
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        "tests": [
            "pytest>=6.2.5,<7",
            "pytest-cov>=3.0.0,<4"
        ],
        "docs": [
            "sphinx>=4.2.0,<5",
            "sphinx-rtd-theme>=1.0.0,<2",
            "sphinx-click>=3.0.1,<4"
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
