#!/usr/bin/env python3

from setuptools import (
    setup, find_packages
)

# Project URLs
project_urls = {
    "Tracker": "https://github.com/meherett/python-hdwallet/issues",
    "Documentation": "https://hdwallet.readthedocs.io"
}

# README.md
with open("README.md", "r", encoding="utf-8") as readme:
    long_description: str = readme.read()

# requirements.txt
with open("requirements.txt", "r") as _requirements:
    requirements: list = list(map(str.strip, _requirements.read().split("\n")))

setup(
    name="hdwallet",
    version="v2.2.1",
    description="Python-based library for the implementation of a hierarchical deterministic wallet "
                "generator for more than 140+ multiple cryptocurrencies.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Meheret Tesfaye Batu",
    author_email="meherett.batu@gmail.com",
    url="https://github.com/meherett/python-hdwallet",
    project_urls=project_urls,
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
        "cli": [
            "click>=8.1.3,<9",
            "click-aliases>=1.0.1,<2",
            "tabulate>=0.9.0,<1"
        ],
        "tests": [
            "pytest>=7.2.0,<8",
            "pytest-cov>=4.0.0,<5",
            "tox==3.28.0"
        ],
        "docs": [
            "sphinx>=5.3.0,<6",
            "furo==2022.12.7",
            "sphinx-click>=4.4.0,<5"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
