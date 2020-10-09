#!/usr/bin/env python3

from mnemonic import Mnemonic
from binascii import hexlify
from typing import AnyStr

import os

from .cryptocurrencies import get_cryptocurrency
from .libs.base58 import check_decode


def get_bytes(string: AnyStr) -> bytes:
    if isinstance(string, bytes):
        byte = string
    elif isinstance(string, str):
        byte = bytes.fromhex(string)
    else:
        raise TypeError("agreement must be either 'bytes' or 'string'!")
    return byte


def generate_mnemonic(language: str = "english", strength: int = 128) -> str:
    return Mnemonic(language=language).generate(strength=strength)


def generate_entropy(strength: int = 128) -> str:

    if strength not in [128, 160, 192, 224, 256]:
        raise ValueError(
            "Strength should be one of the following "
            "[128, 160, 192, 224, 256], but it is not (%d)."
            % strength
        )

    return hexlify(os.urandom(strength // 8)).decode()


def is_mnemonic(mnemonic: str, language: str = None) -> bool:

    if language and language not in ["english", "french", "italian", "japanese",
                                     "chinese_simplified", "chinese_traditional", "korean", "spanish"]:
        raise ValueError("Invalid language, use only this options english, french, "
                         "italian, spanish, chinese_simplified, chinese_traditional, japanese & korean.")

    try:
        if language is None:
            for _language in ["english", "french", "italian",
                              "chinese_simplified", "chinese_traditional", "japanese", "korean", "spanish"]:
                valid = False
                if Mnemonic(language=_language).check(mnemonic=mnemonic) is True:
                    valid = True
                    break
            return valid
        else:
            return Mnemonic(language=language).check(mnemonic=mnemonic)
    except:
        return False


def get_mnemonic_language(mnemonic: str) -> str:

    if not is_mnemonic(mnemonic=mnemonic):
        raise ValueError("Invalid 12 word mnemonic.")

    language = None
    for _language in ["english", "french", "italian",
                      "chinese_simplified", "chinese_traditional", "japanese", "korean", "spanish"]:
        if Mnemonic(language=_language).check(mnemonic=mnemonic) is True:
            language = _language
            break
    return language


def is_root_xprivate_key(xprivate_key: str, symbol: str) -> bool:
    decoded_xprivate_key = check_decode(xprivate_key).hex()
    if len(decoded_xprivate_key) != 156:  # 78
        raise ValueError("Invalid xprivate key.")
    cryptocurrency = get_cryptocurrency(symbol=symbol)
    version = cryptocurrency.EXTENDED_PRIVATE_KEY.hex()
    raw = f"{version}000000000000000000"
    return decoded_xprivate_key.startswith(raw)


def is_root_xpublic_key(xpublic_key: str, symbol: str) -> bool:
    decoded_xpublic_key = check_decode(xpublic_key).hex()
    if len(decoded_xpublic_key) != 156:  # 78
        raise ValueError("Invalid xpublic key.")
    cryptocurrency = get_cryptocurrency(symbol=symbol)
    version = cryptocurrency.EXTENDED_PUBLIC_KEY.hex()
    raw = f"{version}000000000000000000"
    return decoded_xpublic_key.startswith(raw)
