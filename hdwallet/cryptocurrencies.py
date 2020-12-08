#!/usr/bin/env python3

from codecs import decode
from typing import Any


class Cryptocurrency:

    NAME: str
    SYMBOL: str
    NETWORK: str
    SCRIPT_ADDRESS: bytes
    PUBLIC_KEY_ADDRESS: bytes
    WIF_SECRET_KEY: bytes
    EXTENDED_PRIVATE_KEY: bytes
    EXTENDED_PUBLIC_KEY: bytes
    BIP44_PATH: str
    DEFAULT_PATH: str


class BitcoinMainnet(Cryptocurrency):

    NAME = "Bitcoin"
    SYMBOL = "BTC"
    NETWORK = "mainnet"
    SCRIPT_ADDRESS = decode("05", "hex")
    PUBLIC_KEY_ADDRESS = decode("00", "hex")
    WIF_SECRET_KEY = decode("80", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/0'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/0'/0'/0/0"


class BitcoinTestnet(Cryptocurrency):

    NAME = "Bitcoin"
    SYMBOL = "BTCTEST"
    NETWORK = "testnet"
    SCRIPT_ADDRESS = decode("c4", "hex")
    PUBLIC_KEY_ADDRESS = decode("6f", "hex")
    WIF_SECRET_KEY = decode("ef", "hex")
    EXTENDED_PRIVATE_KEY = decode("04358394", "hex")
    EXTENDED_PUBLIC_KEY = decode("043587cf", "hex")
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


class EthereumMainnet(Cryptocurrency):

    NAME = "Ethereum"
    SYMBOL = "ETH"
    NETWORK = "mainnet"
    WIF_SECRET_KEY = decode("80", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/60'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/60'/0'/0/0"


class EthereumTestnet(Cryptocurrency):

    NAME = "Ethereum"
    SYMBOL = "ETHTEST"
    NETWORK = "testnet"
    WIF_SECRET_KEY = decode("80", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


class DogecoinMainnet(Cryptocurrency):

    NAME = "Dogecoin"
    SYMBOL = "DOGE"
    NETWORK = "mainnet"
    SCRIPT_ADDRESS = decode("16", "hex")
    PUBLIC_KEY_ADDRESS = decode("1e", "hex")
    WIF_SECRET_KEY = bytes([0x1e + 128])
    EXTENDED_PRIVATE_KEY = decode("02fac398", "hex")
    EXTENDED_PUBLIC_KEY = decode("02facafd", "hex")
    BIP44_PATH = "m/44'/3'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/3'/0'/0/0"


class DogecoinTestnet(Cryptocurrency):

    NAME = "Dogecoin"
    SYMBOL = "DOGETEST"
    NETWORK = "testnet"
    SCRIPT_ADDRESS = decode("c4", "hex")
    PUBLIC_KEY_ADDRESS = decode("71", "hex")
    WIF_SECRET_KEY = bytes([0x71 + 128])
    EXTENDED_PRIVATE_KEY = decode("04358394", "hex")
    EXTENDED_PUBLIC_KEY = decode("043587cf", "hex")
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


class LitecoinMainnet(Cryptocurrency):

    NAME = "Litecoin"
    SYMBOL = "LTC"
    NETWORK = "mainnet"
    SCRIPT_ADDRESS = decode("05", "hex")
    PUBLIC_KEY_ADDRESS = decode("30", "hex")
    WIF_SECRET_KEY = bytes([0x30 + 128])
    EXTENDED_PRIVATE_KEY = decode("019d9cfe", "hex")  # 0488ade4
    EXTENDED_PUBLIC_KEY = decode("019da462", "hex")  # 0488b21e
    BIP44_PATH = "m/44'/2'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/2'/0'/0/0"


class LitecoinTestnet(Cryptocurrency):

    NAME = "Litecoin"
    SYMBOL = "LTCTEST"
    NETWORK = "testnet"
    SCRIPT_ADDRESS = decode("c4", "hex")
    PUBLIC_KEY_ADDRESS = decode("6f", "hex")
    WIF_SECRET_KEY = bytes([0x6f + 128])
    EXTENDED_PRIVATE_KEY = decode("0436ef7d", "hex")  # 04358394
    EXTENDED_PUBLIC_KEY = decode("0436f6e1", "hex")  # 043587cf
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


class OmniMainnet(Cryptocurrency):

    NAME = "Omni"
    SYMBOL = "OMNI"
    NETWORK = "mainnet"
    SCRIPT_ADDRESS = decode("05", "hex")
    PUBLIC_KEY_ADDRESS = decode("00", "hex")
    WIF_SECRET_KEY = decode("80", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/200'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/200'/0'/0/0"


class OmniTestnet(Cryptocurrency):

    NAME = "Omni"
    SYMBOL = "OMNITEST"
    NETWORK = "testnet"
    SCRIPT_ADDRESS = decode("c4", "hex")
    PUBLIC_KEY_ADDRESS = decode("6f", "hex")
    WIF_SECRET_KEY = decode("ef", "hex")
    EXTENDED_PRIVATE_KEY = decode("04358394", "hex")
    EXTENDED_PUBLIC_KEY = decode("043587cf", "hex")
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


class DashMainnet(Cryptocurrency):

    NAME = "Dash"
    SYMBOL = "DASH"
    NETWORK = "mainnet"
    SCRIPT_ADDRESS = decode("10", "hex")
    PUBLIC_KEY_ADDRESS = decode("4c", "hex")
    WIF_SECRET_KEY = decode("cc", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/5'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/5'/0'/0/0"


class DashTestnet(Cryptocurrency):

    NAME = "Dash"
    SYMBOL = "DASHTEST"
    NETWORK = "testnet"
    SCRIPT_ADDRESS = decode("13", "hex")
    PUBLIC_KEY_ADDRESS = decode("8c", "hex")
    WIF_SECRET_KEY = decode("ef", "hex")
    EXTENDED_PRIVATE_KEY = decode("04358394", "hex")
    EXTENDED_PUBLIC_KEY = decode("043587cf", "hex")
    BIP44_PATH = "m/44'/1'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/1'/0'/0/0"


class QtumMainnet(Cryptocurrency):

    NAME = "Qtum"
    SYMBOL = "QTUM"
    NETWORK = "mainnet"
    SCRIPT_ADDRESS = decode("32", "hex")
    PUBLIC_KEY_ADDRESS = decode("3a", "hex")
    WIF_SECRET_KEY = decode("80", "hex")
    EXTENDED_PRIVATE_KEY = decode("0488ade4", "hex")
    EXTENDED_PUBLIC_KEY = decode("0488b21e", "hex")
    BIP44_PATH = "m/44'/88'/{account}'/{change}/{address}"
    DEFAULT_PATH = "m/44'/88'/0'/0/0"


class QtumTestnet(Cryptocurrency):

    NAME = "Qtum"
    SYMBOL = "QTUMTEST"
    NETWORK = "testnet"
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
        raise ValueError("Invalid Cryptocurrency symbol.")
