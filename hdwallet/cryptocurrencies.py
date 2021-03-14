#!/usr/bin/env python3

from types import SimpleNamespace
from typing import Any, Optional

import inspect
import sys


class NestedNamespace(SimpleNamespace):
    def __init__(self, dictionary, **kwargs):
        super().__init__(**kwargs)
        for key, value in dictionary.items():
            if isinstance(value, dict):
                self.__setattr__(key, NestedNamespace(value))
            else:
                self.__setattr__(key, value)


class SegwitAddress(NestedNamespace):

    HRP: Optional[str] = None
    VERSION: int = 0x00


class CoinType(NestedNamespace):

    INDEX: int
    HARDENED: bool
    
    def __str__(self):
        return f"{self.INDEX}'" if self.HARDENED else f"{self.INDEX}"


class ExtendedKey(NestedNamespace):

    P2PKH: int
    P2SH: int

    P2WPKH: Optional[int] = None
    P2WPKH_IN_P2SH: Optional[int] = None

    P2WSH: Optional[int] = None
    P2WSH_IN_P2SH: Optional[int] = None


class ExtendedPrivateKey(ExtendedKey):

    pass


class ExtendedPublicKey(ExtendedKey):

    pass


class Cryptocurrency(NestedNamespace):

    NAME: str
    SYMBOL: str
    NETWORK: str
    COIN_TYPE: CoinType

    SCRIPT_ADDRESS: int
    PUBLIC_KEY_ADDRESS: int
    SEGWIT_ADDRESS: SegwitAddress

    EXTENDED_PRIVATE_KEY: ExtendedPrivateKey
    EXTENDED_PUBLIC_KEY: ExtendedPublicKey

    MESSAGE_PREFIX: Optional[str]
    DEFAULT_PATH: str
    WIF_SECRET_KEY: int


class ArgoneumMainnet(Cryptocurrency):

    NAME = "Argoneum"
    SYMBOL = "AGM"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 421,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x61
    PUBLIC_KEY_ADDRESS = 0x32
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xbf


class AsiacoinMainnet(Cryptocurrency):

    NAME = "Asiacoin"
    SYMBOL = "AC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 51,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x8
    PUBLIC_KEY_ADDRESS = 0x17
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18AsiaCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x97


class AtomMainnet(Cryptocurrency):

    NAME = "Atom"
    SYMBOL = "ATOM"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 118,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xa
    PUBLIC_KEY_ADDRESS = 0x17
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "atom",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x488ade4,
        "P2WPKH_IN_P2SH": 0x488ade4,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x488b21e,
        "P2WPKH_IN_P2SH": 0x488b21e,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Bitcoin Atom Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class AuroracoinMainnet(Cryptocurrency):

    NAME = "Auroracoin"
    SYMBOL = "AUR"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 85,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x17
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18AuroraCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x97


class AxeMainnet(Cryptocurrency):

    NAME = "Axe"
    SYMBOL = "AXE"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 4242,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x10
    PUBLIC_KEY_ADDRESS = 0x37
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xcc


class BataMainnet(Cryptocurrency):

    NAME = "Bata"
    SYMBOL = "BTA"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 89,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x19
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0xa40b91bd,
        "P2SH": 0xa40b91bd,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0xa40c86fa,
        "P2SH": 0xa40c86fa,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Bata Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xa4


class BeetleCoinMainnet(Cryptocurrency):

    NAME = "Beetle Coin"
    SYMBOL = "BEET"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 800,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x55
    PUBLIC_KEY_ADDRESS = 0x1a
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x19Beetlecoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x99


class BelaCoinMainnet(Cryptocurrency):

    NAME = "Bela Coin"
    SYMBOL = "BELA"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 73,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x19
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18BelaCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x99


class BitCloudMainnet(Cryptocurrency):

    NAME = "Bit Cloud"
    SYMBOL = "BTDX"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 218,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x19
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18BitCloud Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x99


class BitSendMainnet(Cryptocurrency):

    NAME = "Bit Send"
    SYMBOL = "BSD"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 91,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x66
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Bitsend Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xcc


class BitcoinCashMainnet(Cryptocurrency):

    NAME = "Bitcoin Cash"
    SYMBOL = "BCH"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 145,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x28
    PUBLIC_KEY_ADDRESS = 0x1c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "bc",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0488ade4,
        "P2SH": 0x0488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": 0x02aa7a99,
        "P2WSH_IN_P2SH": 0x0295b005
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0488b21e,
        "P2SH": 0x0488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": 0x02aa7ed3,
        "P2WSH_IN_P2SH": 0x0295b43f
    })

    MESSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class BitcoinGoldMainnet(Cryptocurrency):

    NAME = "Bitcoin Gold"
    SYMBOL = "BTG"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 156,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x17
    PUBLIC_KEY_ADDRESS = 0x26
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "btg",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0488ade4,
        "P2SH": 0x0488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": 0x02aa7a99,
        "P2WSH_IN_P2SH": 0x0295b005
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0488b21e,
        "P2SH": 0x0488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": 0x02aa7ed3,
        "P2WSH_IN_P2SH": 0x0295b43f
    })

    MESSAGE_PREFIX = "\x1DBitcoin Gold Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class BitcoinMainnet(Cryptocurrency):

    NAME = "Bitcoin"
    SYMBOL = "BTC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 0,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x05
    PUBLIC_KEY_ADDRESS = 0x00
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "bc",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0488ade4,
        "P2SH": 0x0488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": 0x02aa7a99,
        "P2WSH_IN_P2SH": 0x0295b005
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0488b21e,
        "P2SH": 0x0488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": 0x02aa7ed3,
        "P2WSH_IN_P2SH": 0x0295b43f
    })

    MESSAGE_PREFIX = "\x18Bitcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class BitcoinPlusMainnet(Cryptocurrency):

    NAME = "Bitcoin Plus"
    SYMBOL = "XBC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 65,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x8
    PUBLIC_KEY_ADDRESS = 0x19
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18BitcoinPlus Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x99


class BitcoinTestnet(Cryptocurrency):

    NAME = "Bitcoin"
    SYMBOL = "BTCTEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xc4
    PUBLIC_KEY_ADDRESS = 0x6f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "tb",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x04358394,
        "P2SH": 0x04358394,
        "P2WPKH": 0x045f18bc,
        "P2WPKH_IN_P2SH": 0x044a4e28,
        "P2WSH": 0x02575048,
        "P2WSH_IN_P2SH": 0x024285b5
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x043587cf,
        "P2SH": 0x043587cf,
        "P2WPKH": 0x045f1cf6,
        "P2WPKH_IN_P2SH": 0x044a5262,
        "P2WSH": 0x02575483,
        "P2WSH_IN_P2SH": 0x024289ef
    })

    MESSAGE_PREFIX = "\x18Bitcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


class BitcoreMainnet(Cryptocurrency):

    NAME = "Bitcore"
    SYMBOL = "BTX"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 160,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x7d
    PUBLIC_KEY_ADDRESS = 0x3
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "bitcore",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x488ade4,
        "P2WPKH_IN_P2SH": 0x488ade4,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x488b21e,
        "P2WPKH_IN_P2SH": 0x488b21e,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18BitCore Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class BlackcoinMainnet(Cryptocurrency):

    NAME = "Blackcoin"
    SYMBOL = "BLK"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 10,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x55
    PUBLIC_KEY_ADDRESS = 0x19
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x2cfbf60,
        "P2SH": 0x2cfbf60,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x2cfbede,
        "P2SH": 0x2cfbede,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18BlackCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x99


class BlockStampMainnet(Cryptocurrency):

    NAME = "Block Stamp"
    SYMBOL = "BST"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 254,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x0
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "bc",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x488ade4,
        "P2WPKH_IN_P2SH": 0x488ade4,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x488b21e,
        "P2WPKH_IN_P2SH": 0x488b21e,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18BlockStamp Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class BolivarcoinMainnet(Cryptocurrency):

    NAME = "Bolivarcoin"
    SYMBOL = "BOLI"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 278,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x55
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "Bolivarcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xd5


class BritCoinMainnet(Cryptocurrency):

    NAME = "Brit Coin"
    SYMBOL = "BRIT"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 70,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x55
    PUBLIC_KEY_ADDRESS = 0x19
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18BritCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x99


class CPUChainMainnet(Cryptocurrency):

    NAME = "CPU Chain"
    SYMBOL = "CPU"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 363,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x1e
    PUBLIC_KEY_ADDRESS = 0x1c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "cpu",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x1DCPUchain Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class CanadaECoinMainnet(Cryptocurrency):

    NAME = "Canada eCoin"
    SYMBOL = "CDN"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 34,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x1c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Canada eCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x9c


class CannacoinMainnet(Cryptocurrency):

    NAME = "Cannacoin"
    SYMBOL = "CCN"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 19,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x1c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Cannacoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x9c


class ClamsMainnet(Cryptocurrency):

    NAME = "Clams"
    SYMBOL = "CLAM"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 23,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xd
    PUBLIC_KEY_ADDRESS = 0x89
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0xa8c17826,
        "P2SH": 0xa8c17826,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0xa8c26d64,
        "P2SH": 0xa8c26d64,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x85


class ClubCoinMainnet(Cryptocurrency):

    NAME = "Club Coin"
    SYMBOL = "CLUB"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 79,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x55
    PUBLIC_KEY_ADDRESS = 0x1c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18ClubCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x99


class CompcoinMainnet(Cryptocurrency):

    NAME = "Compcoin"
    SYMBOL = "CMP"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 71,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x55
    PUBLIC_KEY_ADDRESS = 0x1c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18CompCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x9c


class CranePayMainnet(Cryptocurrency):

    NAME = "Crane Pay"
    SYMBOL = "CRP"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 2304,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xa
    PUBLIC_KEY_ADDRESS = 0x1c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "cp",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Bitcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x7b


class CraveMainnet(Cryptocurrency):

    NAME = "Crave"
    SYMBOL = "CRAVE"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 186,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x55
    PUBLIC_KEY_ADDRESS = 0x46
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18DarkNet Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x99


class DashMainnet(Cryptocurrency):

    NAME = "Dash"
    SYMBOL = "DASH"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 5,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x10
    PUBLIC_KEY_ADDRESS = 0x4c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0488ade4,
        "P2SH": 0x0488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0488b21e,
        "P2SH": 0x0488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MESSAGE_PREFIX = "\x18Bitcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xcc


class DashTestnet(Cryptocurrency):

    NAME = "Dash"
    SYMBOL = "DASHTEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x13
    PUBLIC_KEY_ADDRESS = 0x8c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x04358394,
        "P2SH": 0x04358394,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x043587cf,
        "P2SH": 0x043587cf,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MESSAGE_PREFIX = "\x18Bitcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


class DeepOnionMainnet(Cryptocurrency):

    NAME = "Deep Onion"
    SYMBOL = "ONION"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 305,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x4e
    PUBLIC_KEY_ADDRESS = 0x1f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "dpn",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x488ade4,
        "P2WPKH_IN_P2SH": 0x488ade4,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x488b21e,
        "P2WPKH_IN_P2SH": 0x488b21e,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18DeepOnion Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x9f


class DefcoinMainnet(Cryptocurrency):

    NAME = "Defcoin"
    SYMBOL = "DFC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 1337,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x1e
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18defcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x9e


class DenariusMainnet(Cryptocurrency):

    NAME = "Denarius"
    SYMBOL = "DNR"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 116,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5a
    PUBLIC_KEY_ADDRESS = 0x1e
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x19Denarius Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x9e


class DiamondMainnet(Cryptocurrency):

    NAME = "Diamond"
    SYMBOL = "DMD"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 152,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x8
    PUBLIC_KEY_ADDRESS = 0x5a
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Diamond Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xda


class DigiByteMainnet(Cryptocurrency):

    NAME = "Digi Byte"
    SYMBOL = "DGB"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 20,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x1e
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "dgb",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x19DigiByte Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class DigitalcoinMainnet(Cryptocurrency):

    NAME = "Digitalcoin"
    SYMBOL = "DGC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 18,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x1e
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x9e0488b2,
        "P2SH": 0x9e0488b2,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Digitalcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x9e


class DogecoinMainnet(Cryptocurrency):

    NAME = "Dogecoin"
    SYMBOL = "DOGE"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 3,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x16
    PUBLIC_KEY_ADDRESS = 0x1e
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x02fac398,
        "P2SH": 0x02fac398,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x02facafd,
        "P2SH": 0x02facafd,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MESSAGE_PREFIX = "\x19Dogecoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xf1


class DogecoinTestnet(Cryptocurrency):

    NAME = "Dogecoin"
    SYMBOL = "DOGETEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 3,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xc4
    PUBLIC_KEY_ADDRESS = 0x71
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "dogecointestnet",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x04358394,
        "P2SH": 0x04358394,
        "P2WPKH": 0x04358394,
        "P2WPKH_IN_P2SH": 0x04358394,
        "P2WSH": 0x04358394,
        "P2WSH_IN_P2SH": 0x04358394
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x043587cf,
        "P2SH": 0x043587cf,
        "P2WPKH": 0x043587cf,
        "P2WPKH_IN_P2SH": 0x043587cf,
        "P2WSH": 0x043587cf,
        "P2WSH_IN_P2SH": 0x043587cf
    })

    MESSAGE_PREFIX = "\x19Dogecoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xf1


class EDRCoinMainnet(Cryptocurrency):

    NAME = "EDR Coin"
    SYMBOL = "EDRC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 56,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x1c
    PUBLIC_KEY_ADDRESS = 0x5d
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18EDRcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xdd


class EcoinMainnet(Cryptocurrency):

    NAME = "Ecoin"
    SYMBOL = "ECN"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 115,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x14
    PUBLIC_KEY_ADDRESS = 0x5c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18eCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xdc


class EinsteiniumMainnet(Cryptocurrency):

    NAME = "Einsteinium"
    SYMBOL = "EMC2"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 41,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x21
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Einsteinium Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xa1


class EthereumMainnet(Cryptocurrency):

    NAME = "Ethereum"
    SYMBOL = "ETH"
    NETWORK = "mainnet"

    COIN_TYPE = CoinType({
        "INDEX": 60,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x05
    PUBLIC_KEY_ADDRESS = 0x00
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "bc",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0488ade4,
        "P2SH": 0x0488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": 0x02aa7a99,
        "P2WSH_IN_P2SH": 0x0295b005
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0488b21e,
        "P2SH": 0x0488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": 0x02aa7ed3,
        "P2WSH_IN_P2SH": 0x0295b43f
    })

    MESSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class EuropeCoinMainnet(Cryptocurrency):

    NAME = "Europe Coin"
    SYMBOL = "ERC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 151,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x21
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Bitcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xa8


class ExclusiveCoinMainnet(Cryptocurrency):

    NAME = "Exclusive Coin"
    SYMBOL = "EXCL"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 190,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x89
    PUBLIC_KEY_ADDRESS = 0x21
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18ExclusiveCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xa1


class FIXMainnet(Cryptocurrency):

    NAME = "FIX"
    SYMBOL = "FIX"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 336,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5f
    PUBLIC_KEY_ADDRESS = 0x23
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x221312b,
        "P2SH": 0x221312b,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x22d2533,
        "P2SH": 0x22d2533,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x3c


class FIXTestnet(Cryptocurrency):

    NAME = "FIX"
    SYMBOL = "FIXTEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x89
    PUBLIC_KEY_ADDRESS = 0x4c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x3a805837,
        "P2SH": 0x3a805837,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x3a8061a0,
        "P2SH": 0x3a8061a0,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xed


class FeathercoinMainnet(Cryptocurrency):

    NAME = "Feathercoin"
    SYMBOL = "FTC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 8,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0xe
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488daee,
        "P2SH": 0x488daee,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488bc26,
        "P2SH": 0x488bc26,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Feathercoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x8e


class FirstcoinMainnet(Cryptocurrency):

    NAME = "Firstcoin"
    SYMBOL = "FRST"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 167,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x23
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18FirstCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xa3


class FlashcoinMainnet(Cryptocurrency):

    NAME = "Flashcoin"
    SYMBOL = "FLASH"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 120,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x82
    PUBLIC_KEY_ADDRESS = 0x44
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Flashcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xc4


class FujiCoinMainnet(Cryptocurrency):

    NAME = "Fuji Coin"
    SYMBOL = "FJC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 75,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x10
    PUBLIC_KEY_ADDRESS = 0x24
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "fc",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x19FujiCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xa4


class GCRCoinMainnet(Cryptocurrency):

    NAME = "GCR Coin"  # Global Currency Reserve Coin
    SYMBOL = "GCR"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 49,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x61
    PUBLIC_KEY_ADDRESS = 0x26
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18GCR Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x9a


class GameCreditsMainnet(Cryptocurrency):

    NAME = "Game Credits"
    SYMBOL = "GAME"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 101,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x26
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xa6


class GoByteMainnet(Cryptocurrency):

    NAME = "Go Byte"
    SYMBOL = "GBX"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 176,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xa
    PUBLIC_KEY_ADDRESS = 0x26
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18DarkCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xc6


class GridcoinMainnet(Cryptocurrency):

    NAME = "Gridcoin"
    SYMBOL = "GRC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 84,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x55
    PUBLIC_KEY_ADDRESS = 0x3e
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Gridcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xbe


class GroestlCoinMainnet(Cryptocurrency):

    NAME = "Groestl Coin"
    SYMBOL = "GRS"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 17,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x24
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "grs",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x19GroestlCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class GroestlCoinTestnet(Cryptocurrency):

    NAME = "Groestl Coin"
    SYMBOL = "GRSTEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xc4
    PUBLIC_KEY_ADDRESS = 0x6f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "tgrs",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x4358394,
        "P2SH": 0x4358394,
        "P2WPKH": 0x045f18bc,
        "P2WPKH_IN_P2SH": 0x044a4e28,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x43587cf,
        "P2SH": 0x43587cf,
        "P2WPKH": 0x045f1cf6,
        "P2WPKH_IN_P2SH": 0x044a5262,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x19GroestlCoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


class GuldenMainnet(Cryptocurrency):

    NAME = "Gulden"
    SYMBOL = "NLG"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 87,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x62
    PUBLIC_KEY_ADDRESS = 0x26
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Guldencoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x62


class HelleniccoinMainnet(Cryptocurrency):

    NAME = "Helleniccoin"
    SYMBOL = "HNC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 168,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x30
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18helleniccoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xb0


class HempcoinMainnet(Cryptocurrency):

    NAME = "Hempcoin"
    SYMBOL = "THC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 113,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x8
    PUBLIC_KEY_ADDRESS = 0x28
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Hempcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xa8


class IXCoinMainnet(Cryptocurrency):

    NAME = "IX Coin"
    SYMBOL = "IXC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 86,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x8a
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Ixcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class InsaneCoinMainnet(Cryptocurrency):

    NAME = "Insane Coin"
    SYMBOL = "INSN"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 68,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x39
    PUBLIC_KEY_ADDRESS = 0x66
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18INSaNe Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x37


class InternetOfPeopleMainnet(Cryptocurrency):

    NAME = "Internet Of People"
    SYMBOL = "IOP"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 66,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xae
    PUBLIC_KEY_ADDRESS = 0x75
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0xae3416f6,
        "P2SH": 0xae3416f6,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x2780915f,
        "P2SH": 0x2780915f,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18IoP Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x31


class JumbucksMainnet(Cryptocurrency):

    NAME = "Jumbucks"
    SYMBOL = "JBS"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 26,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x2b
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x37a6460,
        "P2SH": 0x37a6460,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x37a689a,
        "P2SH": 0x37a689a,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x19Jumbucks Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xab


class KobocoinMainnet(Cryptocurrency):

    NAME = "Kobocoin"
    SYMBOL = "KOBO"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 196,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x1c
    PUBLIC_KEY_ADDRESS = 0x23
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Kobocoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xa3


class KomodoMainnet(Cryptocurrency):

    NAME = "Komodo"
    SYMBOL = "KMD"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 141,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x55
    PUBLIC_KEY_ADDRESS = 0x3c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Komodo Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xbc


class LBRYCreditsMainnet(Cryptocurrency):

    NAME = "LBRY Credits"
    SYMBOL = "LBC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 140,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x7a
    PUBLIC_KEY_ADDRESS = 0x55
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18LBRYcrd Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x1c


class LinxMainnet(Cryptocurrency):

    NAME = "Linx"
    SYMBOL = "LINX"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 114,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x4b
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18LinX Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xcb


class LitecoinMainnet(Cryptocurrency):

    NAME = "Litecoin"
    SYMBOL = "LTC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 2,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x32
    PUBLIC_KEY_ADDRESS = 0x30
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "ltc",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x019d9cfe,
        "P2SH": 0x019d9cfe,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x01b26792,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x019da462,
        "P2SH": 0x019da462,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x01b26ef6,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MESSAGE_PREFIX = "\x19Litecoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xb0


class LitecoinTestnet(Cryptocurrency):

    NAME = "Litecoin"
    SYMBOL = "LTCTEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xc4
    PUBLIC_KEY_ADDRESS = 0x6f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "litecointestnet",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0436ef7d,
        "P2SH": 0x0436ef7d,
        "P2WPKH": 0x04358394,
        "P2WPKH_IN_P2SH": 0x04358394,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0436f6e1,
        "P2SH": 0x0436f6e1,
        "P2WPKH": 0x043587cf,
        "P2WPKH_IN_P2SH": 0x043587cf,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MESSAGE_PREFIX = "\x19Litecoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xb0


class LkrcoinMainnet(Cryptocurrency):

    NAME = "Lkrcoin"
    SYMBOL = "LKR"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 557,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x55
    PUBLIC_KEY_ADDRESS = 0x30
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18LKRcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xb0


class MazacoinMainnet(Cryptocurrency):

    NAME = "Mazacoin"
    SYMBOL = "MZC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 13,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x9
    PUBLIC_KEY_ADDRESS = 0x32
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xe0


class MonacoinMainnet(Cryptocurrency):

    NAME = "Monacoin"
    SYMBOL = "MONA"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 22,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x37
    PUBLIC_KEY_ADDRESS = 0x32
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "mona",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x488ade4,
        "P2WPKH_IN_P2SH": 0x488ade4,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x488b21e,
        "P2WPKH_IN_P2SH": 0x488b21e,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Monacoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xb0


class MonkeyProjectMainnet(Cryptocurrency):

    NAME = "Monkey Project"
    SYMBOL = "MONK"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 214,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x1c
    PUBLIC_KEY_ADDRESS = 0x33
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "monkey",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488dde4,
        "P2SH": 0x488dde4,
        "P2WPKH": 0x488dde4,
        "P2WPKH_IN_P2SH": 0x488dde4,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x488b21e,
        "P2WPKH_IN_P2SH": 0x488b21e,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "Monkey Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x37


class MyriadcoinMainnet(Cryptocurrency):

    NAME = "Myriadcoin"
    SYMBOL = "XMY"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 90,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x9
    PUBLIC_KEY_ADDRESS = 0x32
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xb2


class NIXMainnet(Cryptocurrency):

    NAME = "NIX"
    SYMBOL = "NIX"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 400,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x35
    PUBLIC_KEY_ADDRESS = 0x26
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "nix",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x488ade4,
        "P2WPKH_IN_P2SH": 0x488ade4,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x488b21e,
        "P2WPKH_IN_P2SH": 0x488b21e,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Nix Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class NamecoinMainnet(Cryptocurrency):

    NAME = "Namecoin"
    SYMBOL = "NMC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 7,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xd
    PUBLIC_KEY_ADDRESS = 0x34
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class NavcoinMainnet(Cryptocurrency):

    NAME = "Navcoin"
    SYMBOL = "NAV"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 130,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x55
    PUBLIC_KEY_ADDRESS = 0x35
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0488ade4,
        "P2SH": 0x0488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0488b21e,
        "P2SH": 0x0488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MESSAGE_PREFIX = "\x18Navcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x96


class NeblioMainnet(Cryptocurrency):

    NAME = "Neblio"
    SYMBOL = "NEBL"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 146,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x70
    PUBLIC_KEY_ADDRESS = 0x35
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Neblio Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xb5


class NuBitsMainnet(Cryptocurrency):

    NAME = "NuBits"
    SYMBOL = "NBT"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 12,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x1a
    PUBLIC_KEY_ADDRESS = 0x19
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Nu Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x96


class OmniMainnet(Cryptocurrency):

    NAME = "Omni"
    SYMBOL = "OMNI"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 200,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x05
    PUBLIC_KEY_ADDRESS = 0x00
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0488ade4,
        "P2SH": 0x0488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0488b21e,
        "P2SH": 0x0488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MESSAGE_PREFIX = "\x18Bitcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class OmniTestnet(Cryptocurrency):

    NAME = "Omni"
    SYMBOL = "OMNITEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xc4
    PUBLIC_KEY_ADDRESS = 0x6f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x04358394,
        "P2SH": 0x04358394,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x043587cf,
        "P2SH": 0x043587cf,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MESSAGE_PREFIX = "\x18Bitcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


class OnixCoinMainnet(Cryptocurrency):

    NAME = "Onix Coin"
    SYMBOL = "ONX"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 174,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x4b
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "ONIX Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xcb


class PeercoinMainnet(Cryptocurrency):

    NAME = "Peercoin"
    SYMBOL = "PPC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 6,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x75
    PUBLIC_KEY_ADDRESS = 0x37
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xb7


class PivxMainnet(Cryptocurrency):

    NAME = "Pivx"
    SYMBOL = "PIVX"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 119,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xd
    PUBLIC_KEY_ADDRESS = 0x1e
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x221312b,
        "P2SH": 0x221312b,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x22d2533,
        "P2SH": 0x22d2533,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xd4


class PivxTestnet(Cryptocurrency):

    NAME = "Pivx"
    SYMBOL = "PIVXTEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x13
    PUBLIC_KEY_ADDRESS = 0x8b
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x3a805837,
        "P2SH": 0x3a805837,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x3a8061a0,
        "P2SH": 0x3a8061a0,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


class QtumMainnet(Cryptocurrency):

    NAME = "Qtum"
    SYMBOL = "QTUM"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 2301,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x32
    PUBLIC_KEY_ADDRESS = 0x3a
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "qc1",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0488ade4,
        "P2SH": 0x0488ade4,
        "P2WPKH": 0x045f18bc,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": 0x02aa7a99,
        "P2WSH_IN_P2SH": 0x0295b005
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0488b21e,
        "P2SH": 0x0488b21e,
        "P2WPKH": 0x045f1cf6,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": 0x02aa7ed3,
        "P2WSH_IN_P2SH": 0x0295b43f
    })

    MESSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class QtumTestnet(Cryptocurrency):

    NAME = "Qtum"
    SYMBOL = "QTUMTEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x6e
    PUBLIC_KEY_ADDRESS = 0x78
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "tq1",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x04358394,
        "P2SH": 0x04358394,
        "P2WPKH": 0x045f18bc,
        "P2WPKH_IN_P2SH": 0x044a4e28,
        "P2WSH": 0x02575048,
        "P2WSH_IN_P2SH": 0x024285b5
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x043587cf,
        "P2SH": 0x043587cf,
        "P2WPKH": 0x045f1cf6,
        "P2WPKH_IN_P2SH": 0x044a5262,
        "P2WSH": 0x02575483,
        "P2WSH_IN_P2SH": 0x024289ef
    })

    MESSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


class ScribeMainnet(Cryptocurrency):

    NAME = "Scribe"
    SYMBOL = "SCRIBE"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 545,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x7d
    PUBLIC_KEY_ADDRESS = 0x3c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x6e


class ShadowCashMainnet(Cryptocurrency):

    NAME = "Shadow Cash"
    SYMBOL = "SDC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 35,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x7d
    PUBLIC_KEY_ADDRESS = 0x3f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0xee8031e8,
        "P2SH": 0xee8031e8,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0xee80286a,
        "P2SH": 0xee80286a,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xbf


class ShadowCashTestnet(Cryptocurrency):

    NAME = "Shadow Cash"
    SYMBOL = "SDCTEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xc4
    PUBLIC_KEY_ADDRESS = 0x7f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x76c1077a,
        "P2SH": 0x76c1077a,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x76c0fdfb,
        "P2SH": 0x76c0fdfb,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xff


class SlimcoinMainnet(Cryptocurrency):

    NAME = "Slimcoin"
    SYMBOL = "SLM"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 63,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x7d
    PUBLIC_KEY_ADDRESS = 0x3f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0xef69ea80,
        "P2SH": 0xef69ea80,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0xef6adf10,
        "P2SH": 0xef6adf10,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x46


class SlimcoinTestnet(Cryptocurrency):

    NAME = "Slimcoin"
    SYMBOL = "SLMTEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xc4
    PUBLIC_KEY_ADDRESS = 0x6f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x4358394,
        "P2SH": 0x4358394,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x43587cf,
        "P2SH": 0x43587cf,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x57


class SugarchainMainnet(Cryptocurrency):

    NAME = "Sugarchain"
    SYMBOL = "SUGAR"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 408,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x7d
    PUBLIC_KEY_ADDRESS = 0x3f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "sugar",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Sugarchain Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class SugarchainTestnet(Cryptocurrency):

    NAME = "Sugarchain"
    SYMBOL = "SUGARTEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x80
    PUBLIC_KEY_ADDRESS = 0x42
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "tugar",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x45f18bc,
        "P2SH": 0x45f18bc,
        "P2WPKH": 0x045f18bc,
        "P2WPKH_IN_P2SH": 0x044a4e28,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x45f1cf6,
        "P2SH": 0x45f1cf6,
        "P2WPKH": 0x045f1cf6,
        "P2WPKH_IN_P2SH": 0x044a5262,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Sugarchain Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


class SyscoinMainnet(Cryptocurrency):

    NAME = "Syscoin"
    SYMBOL = "SYS"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 57,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x3f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "sys",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Syscoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class VertcoinMainnet(Cryptocurrency):

    NAME = "Vertcoin"
    SYMBOL = "VTC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 28,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5
    PUBLIC_KEY_ADDRESS = 0x47
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "vtc",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x0488ade4,
        "P2WPKH_IN_P2SH": 0x0488ade4,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x0488b21e,
        "P2WPKH_IN_P2SH": 0x0488b21e,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Vertcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class ViacoinMainnet(Cryptocurrency):

    NAME = "Viacoin"
    SYMBOL = "VIA"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 14,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x21
    PUBLIC_KEY_ADDRESS = 0x47
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "viacoin",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x0488ade4,
        "P2WPKH_IN_P2SH": 0x0488ade4,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x0488b21e,
        "P2WPKH_IN_P2SH": 0x0488b21e,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Viacoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xc7


class ViacoinTestnet(Cryptocurrency):

    NAME = "Viacoin"
    SYMBOL = "VIATEST"
    NETWORK = "testnet"
    COIN_TYPE = CoinType({
        "INDEX": 14,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xc4
    PUBLIC_KEY_ADDRESS = 0x7f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": None,
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x4358394,
        "P2SH": 0x4358394,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x43587cf,
        "P2SH": 0x43587cf,
        "P2WPKH": None,
        "P2WPKH_IN_P2SH": None,
        "P2WSH": None,
        "P2WSH_IN_P2SH": None
    })

    MASSAGE_PREFIX = "\x18Viacoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xff


class XinFinMainnet(Cryptocurrency):

    NAME = "XinFin"
    SYMBOL = "XDC"
    NETWORK = "mainnet"
    COIN_TYPE = CoinType({
        "INDEX": 550,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x05
    PUBLIC_KEY_ADDRESS = 0x00
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "bc",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0488ade4,
        "P2SH": 0x0488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": 0x02aa7a99,
        "P2WSH_IN_P2SH": 0x0295b005
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0488b21e,
        "P2SH": 0x0488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": 0x02aa7ed3,
        "P2WSH_IN_P2SH": 0x0295b43f
    })

    MESSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


def get_cryptocurrency(symbol: str) -> Any:

    for _, cryptocurrency in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(cryptocurrency):
            if issubclass(cryptocurrency, Cryptocurrency) and cryptocurrency != Cryptocurrency:
                if symbol == cryptocurrency.SYMBOL:
                    return cryptocurrency

    raise ValueError(f"Invalid Cryptocurrency '{symbol}' symbol.")

