#!/usr/bin/env python3

from .hdwallet import (
    HDWallet,
    BIP32HDWallet,
    BIP44HDWallet,
    BIP49HDWallet,
    BIP84HDWallet,
    BIP141HDWallet
)

# HDWallet Information's
__version__: str = "v2.1.2"
__license__: str = "ISCL"
__author__: str = "Meheret Tesfaye Batu"
__email__: str = "meherett@zoho.com"
__description__: str = "Python-based library for the implementation of a hierarchical deterministic wallet " \
                       "generator for more than 140+ multiple cryptocurrencies."

__all__: list = [
    "__version__",
    "__license__",
    "__author__",
    "__email__",
    "__description__",
    "HDWallet",
    "BIP32HDWallet",
    "BIP44HDWallet",
    "BIP49HDWallet",
    "BIP84HDWallet",
    "BIP141HDWallet"
]
