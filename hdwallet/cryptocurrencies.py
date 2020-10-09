#!/usr/bin/env python3

from codecs import decode
from typing import Any


class Cryptocurrency:

    NAME: str
    SYMBOL: str
    SCRIPT_ADDRESS: bytes
    PUBLIC_KEY_ADDRESS: bytes
    WIF_SECRET_KEY: bytes
    EXTENDED_PRIVATE_KEY: bytes
    EXTENDED_PUBLIC_KEY: bytes
    BIP44_PATH: str
    DEFAULT_PATH: str


class BitcoinMainnet(Cryptocurrency):

    NAME = "Bitcoin Mainnet"
    SYMBOL = "BTC"
    SCRIPT_ADDRESS = decode("05", "hex")
    PUBLIC_KEY_ADDRESS = decode("00", "hex")
    WIF_SECRET_KEY = decode("80", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/0'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/0'/0'/0/0"


class BitcoinTestnet(Cryptocurrency):

    NAME = "Bitcoin Testnet"
    SYMBOL = "BTCTEST"
    SCRIPT_ADDRESS = decode("c4", "hex")
    PUBLIC_KEY_ADDRESS = decode("6f", "hex")
    WIF_SECRET_KEY = decode("ef", "hex")
    EXTENDED_PRIVATE_KEY = decode("04358394", "hex")
    EXTENDED_PUBLIC_KEY = decode("043587cf", "hex")
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


class EthereumMainnet(Cryptocurrency):

    NAME = "Ethereum Mainnet"
    SYMBOL = "ETH"
    WIF_SECRET_KEY = decode("80", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/60'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/60'/0'/0/0"


class EthereumTestnet(Cryptocurrency):

    NAME = "Ethereum Testnet"
    SYMBOL = "ETHTEST"
    WIF_SECRET_KEY = decode("80", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/60'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/60'/0'/0/0"


class DogecoinMainnet(Cryptocurrency):

    NAME = "Dogecoin Mainnet"
    SYMBOL = "DOGE"
    SCRIPT_ADDRESS = decode("16", "hex")
    PUBLIC_KEY_ADDRESS = decode("1e", "hex")
    WIF_SECRET_KEY = bytes([0x1e + 128])
    EXTENDED_PRIVATE_KEY = decode("02fac398", "hex")
    EXTENDED_PUBLIC_KEY = decode("02facafd", "hex")
    BIP44_PATH = "m/44'/3'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/3'/0'/0/0"


class DogecoinTestnet(Cryptocurrency):

    NAME = "Dogecoin Testnet"
    SYMBOL = "DOGETEST"
    SCRIPT_ADDRESS = decode("c4", "hex")
    PUBLIC_KEY_ADDRESS = decode("71", "hex")
    WIF_SECRET_KEY = bytes([0x71 + 128])
    EXTENDED_PRIVATE_KEY = decode("04358394", "hex")
    EXTENDED_PUBLIC_KEY = decode("043587cf", "hex")
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


class LitecoinMainnet(Cryptocurrency):

    NAME = "Litecoin Mainnet"
    SYMBOL = "LTC"
    SCRIPT_ADDRESS = decode("05", "hex")
    PUBLIC_KEY_ADDRESS = decode("30", "hex")
    WIF_SECRET_KEY = bytes([0x30 + 128])
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")  # 019d9cfe
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")  # 019da462
    BIP44_PATH = "m/44'/2'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/2'/0'/0/0"


class LitecoinTestnet(Cryptocurrency):

    NAME = "Litecoin Testnet"
    SYMBOL = "LTCTEST"
    SCRIPT_ADDRESS = decode("c4", "hex")
    PUBLIC_KEY_ADDRESS = decode("6f", "hex")
    WIF_SECRET_KEY = bytes([0x6f + 128])
    EXTENDED_PRIVATE_KEY = decode("04358394", "hex")  # 0436ef7d
    EXTENDED_PUBLIC_KEY = decode("043587cf", "hex")  # 0436f6e1
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


class OmniMainnet(Cryptocurrency):

    NAME = "Omni Mainnet"
    SYMBOL = "OMNI"
    SCRIPT_ADDRESS = decode("05", "hex")
    PUBLIC_KEY_ADDRESS = decode("00", "hex")
    WIF_SECRET_KEY = decode("80", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/200'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/200'/0'/0/0"


class OmniTestnet(Cryptocurrency):

    NAME = "Omni Testnet"
    SYMBOL = "OMNITEST"
    SCRIPT_ADDRESS = decode("c4", "hex")
    PUBLIC_KEY_ADDRESS = decode("6f", "hex")
    WIF_SECRET_KEY = decode("ef", "hex")
    EXTENDED_PRIVATE_KEY = decode("04358394", "hex")
    EXTENDED_PUBLIC_KEY = decode("043587cf", "hex")
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


class DashMainnet(Cryptocurrency):

    NAME = "Dash Mainnet"
    SYMBOL = "DASH"
    SCRIPT_ADDRESS = decode("10", "hex")
    PUBLIC_KEY_ADDRESS = decode("4c", "hex")
    WIF_SECRET_KEY = decode("cc", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/5'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/5'/0'/0/0"


class DashTestnet(Cryptocurrency):

    NAME = "Dash Testnet"
    SYMBOL = "DASHTEST"
    SCRIPT_ADDRESS = decode("13", "hex")
    PUBLIC_KEY_ADDRESS = decode("8c", "hex")
    WIF_SECRET_KEY = decode("ef", "hex")
    EXTENDED_PRIVATE_KEY = decode("04358394", "hex")
    EXTENDED_PUBLIC_KEY = decode("043587cf", "hex")
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


class QtumMainnet(Cryptocurrency):

    NAME = "Qtum Mainnet"
    SYMBOL = "QTUM"
    SCRIPT_ADDRESS = decode("32", "hex")
    PUBLIC_KEY_ADDRESS = decode("3a", "hex")
    WIF_SECRET_KEY = decode("80", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/88'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/88'/0'/0/0"


class QtumTestnet(Cryptocurrency):

    NAME = "Qtum Testnet"
    SYMBOL = "QTUMTEST"
    SCRIPT_ADDRESS = decode("6e", "hex")
    PUBLIC_KEY_ADDRESS = decode("78", "hex")
    WIF_SECRET_KEY = decode("ef", "hex")
    EXTENDED_PRIVATE_KEY = decode("04358394", "hex")
    EXTENDED_PUBLIC_KEY = decode("043587cf", "hex")
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


def get_cryptocurrency(symbol: str) -> Any:

    if symbol.upper() == "BTC":
        return BitcoinMainnet
    elif symbol.upper() == "BTCTEST":
        return BitcoinTestnet
    elif symbol.upper() == "ETH":
        return EthereumMainnet
    elif symbol.upper() == "ETHTEST":
        return EthereumTestnet
    elif symbol.upper() == "DOGE":
        return DogecoinMainnet
    elif symbol.upper() == "DOGETEST":
        return DogecoinTestnet
    elif symbol.upper() == "LTC":
        return LitecoinMainnet
    elif symbol.upper() == "LTCTEST":
        return LitecoinTestnet
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
        raise ValueError("Invalid cryptocurrency symbol.")
