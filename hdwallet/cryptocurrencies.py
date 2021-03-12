#!/usr/bin/env python3

from types import SimpleNamespace
from typing import Any, Optional


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


class EthereumTestnet(Cryptocurrency):

    NAME = "Ethereum"
    SYMBOL = "ETHTEST"
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

    MESSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


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


class XinFinTestnet(Cryptocurrency):

    NAME = "XinFin"
    SYMBOL = "XDCTEST"
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

    MESSAGE_PREFIX = None
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


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
        "INDEX": 35,
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
        "HRP": None,
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


def get_cryptocurrency(symbol: str) -> Any:

    if symbol.upper() == "BTC":
        return BitcoinMainnet
    elif symbol.upper() == "BTCTEST":
        return BitcoinTestnet
    elif symbol.upper() == "BTG":
        return BitcoinGoldMainnet
    elif symbol.upper() == "BCH":
        return BitcoinCashMainnet
    elif symbol.upper() == "ETH":
        return EthereumMainnet
    elif symbol.upper() == "ETHTEST":
        return EthereumTestnet
    elif symbol.upper() == "DOGE":
        return DogecoinMainnet
    elif symbol.upper() == "DOGETEST":
        return DogecoinTestnet
    elif symbol.upper() == "XDC":
        return XinFinMainnet
    elif symbol.upper() == "XDCTEST":
        return XinFinTestnet
    elif symbol.upper() == "LTC":
        return LitecoinMainnet
    elif symbol.upper() == "LTCTEST":
        return LitecoinTestnet
    elif symbol.upper() == "NAV":
        return NavcoinMainnet
    elif symbol.upper() == "SDC":
        return ShadowCashMainnet
    elif symbol.upper() == "SDCTEST":
        return ShadowCashTestnet
    elif symbol.upper() == "VIA":
        return ViacoinMainnet
    elif symbol.upper() == "VIATEST":
        return ViacoinTestnet
    elif symbol.upper() == "OMNI":
        return OmniMainnet
    elif symbol.upper() == "OMNITEST":
        return OmniTestnet
    elif symbol.upper() == "DASH":
        return DashMainnet
    elif symbol.upper() == "DASHTEST":
        return DashTestnet
    elif symbol.upper() == "QTUM":
        return QtumMainnet
    elif symbol.upper() == "QTUMTEST":
        return QtumTestnet
    else:
        raise ValueError("Invalid Cryptocurrency symbol.")
