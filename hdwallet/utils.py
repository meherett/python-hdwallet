#!/usr/bin/env python3

from mnemonic import Mnemonic
from binascii import hexlify, unhexlify
from random import choice
from typing import AnyStr, Optional

import string
import os
import inspect
import unicodedata
import binascii

from hdwallet import cryptocurrencies
from .cryptocurrencies import (
    get_cryptocurrency, Cryptocurrency
)
from .libs.base58 import check_decode

# Alphabet and digits.
letters = string.ascii_letters + string.digits


def _unhexlify(integer: int):
    try:
        return unhexlify("0%x" % integer)
    except binascii.Error:
        return unhexlify("%x" % integer)


def get_semantic(_cryptocurrency: Cryptocurrency, version: bytes, key_type: str) -> str:
    for name, cryptocurrency in inspect.getmembers(cryptocurrencies):
        if inspect.isclass(cryptocurrency):
            if issubclass(cryptocurrency, cryptocurrencies.Cryptocurrency) and cryptocurrency == _cryptocurrency:
                if key_type == "private_key":
                    for key, value in inspect.getmembers(cryptocurrency.EXTENDED_PRIVATE_KEY):
                        if value == int(version.hex(), 16):
                            return key.lower()
                elif key_type == "public_key":
                    for key, value in inspect.getmembers(cryptocurrency.EXTENDED_PUBLIC_KEY):
                        if value == int(version.hex(), 16):
                            return key.lower()


def get_bytes(string: AnyStr) -> bytes:
    if isinstance(string, bytes):
        byte = string
    elif isinstance(string, str):
        byte = bytes.fromhex(string)
    else:
        raise TypeError("Agreement must be either 'bytes' or 'string'!")
    return byte


def generate_passphrase(length: int = 32) -> str:
    """
    Generate entropy hex string.

    :param length: Passphrase length, default to 32.
    :type length: int

    :returns: str -- Passphrase hex string.

    >>> from hdwallet.utils import generate_passphrase
    >>> generate_passphrase(length=32)
    "N39rPfa3QvF2Tm2nPyoBpXNiBFXJywTz"
    """

    return str().join(choice(letters) for _ in range(length))


def generate_entropy(strength: int = 128) -> str:
    """
    Generate entropy hex string.

    :param strength: Entropy strength, default to 128.
    :type strength: int

    :returns: str -- Entropy hex string.

    >>> from hdwallet.utils import generate_entropy
    >>> generate_entropy(strength=128)
    "ee535b143b0d9d1f87546f9df0d06b1a"
    """

    if strength not in [128, 160, 192, 224, 256]:
        raise ValueError(
            "Strength should be one of the following "
            "[128, 160, 192, 224, 256], but it is not (%d)."
            % strength
        )
    return hexlify(os.urandom(strength // 8)).decode()


def generate_mnemonic(language: str = "english", strength: int = 128) -> str:
    """
    Generate mnemonic words.

    :param language: Mnemonic language, default to english.
    :type language: str
    :param strength: Entropy strength, default to 128.
    :type strength: int

    :returns: str -- Mnemonic words.

    >>> from hdwallet.utils import generate_mnemonic
    >>> generate_mnemonic(language="french")
    "sceptre capter séquence girafe absolu relatif fleur zoologie muscle sirop saboter parure"
    """

    if language and language not in ["english", "french", "italian", "japanese",
                                     "chinese_simplified", "chinese_traditional", "korean", "spanish"]:
        raise ValueError("invalid language, use only this options english, french, "
                         "italian, spanish, chinese_simplified, chinese_traditional, japanese or korean languages.")
    if strength not in [128, 160, 192, 224, 256]:
        raise ValueError(
            "Strength should be one of the following "
            "[128, 160, 192, 224, 256], but it is not (%d)."
            % strength
        )

    return Mnemonic(language=language).generate(strength=strength)


def is_entropy(entropy: str) -> bool:
    """
    Check entropy hex string.

    :param entropy: Mnemonic words.
    :type entropy: str

    :returns: bool -- Entropy valid/invalid.

    >>> from hdwallet.utils import is_entropy
    >>> is_entropy(entropy="ee535b143b0d9d1f87546f9df0d06b1a")
    True
    """

    try:
        return len(unhexlify(entropy)) in [16, 20, 24, 28, 32]
    except:
        return False


def is_mnemonic(mnemonic: str, language: Optional[str] = None) -> bool:
    """
    Check mnemonic words.

    :param mnemonic: Mnemonic words.
    :type mnemonic: str
    :param language: Mnemonic language, default to None.
    :type language: str

    :returns: bool -- Mnemonic valid/invalid.

    >>> from hdwallet.utils import is_mnemonic
    >>> is_mnemonic(mnemonic="sceptre capter séquence girafe absolu relatif fleur zoologie muscle sirop saboter parure")
    True
    """

    if language and language not in ["english", "french", "italian", "japanese",
                                     "chinese_simplified", "chinese_traditional", "korean", "spanish"]:
        raise ValueError("invalid language, use only this options english, french, "
                         "italian, spanish, chinese_simplified, chinese_traditional, japanese or korean languages.")
    try:
        mnemonic = unicodedata.normalize("NFKD", mnemonic)
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


def get_entropy_strength(entropy: str) -> int:
    """
    Get entropy strength.

    :param entropy: Entropy hex string.
    :type entropy: str

    :returns: int -- Entropy strength.

    >>> from hdwallet.utils import get_entropy_strength
    >>> get_entropy_strength(entropy="ee535b143b0d9d1f87546f9df0d06b1a")
    128
    """

    if not is_entropy(entropy=entropy):
        raise ValueError("Invalid entropy hex string.")

    length = len(unhexlify(entropy))
    if length == 16:
        return 128
    elif length == 20:
        return 160
    elif length == 24:
        return 192
    elif length == 28:
        return 224
    elif length == 32:
        return 256


def get_mnemonic_strength(mnemonic: str, language: Optional[str] = None) -> int:
    """
    Get mnemonic strength.

    :param mnemonic: Mnemonic words.
    :type mnemonic: str
    :param language: Mnemonic language, default to None.
    :type language: str

    :returns: int -- Mnemonic strength.

    >>> from hdwallet.utils import get_mnemonic_strength
    >>> get_mnemonic_strength(mnemonic="sceptre capter séquence girafe absolu relatif fleur zoologie muscle sirop saboter parure")
    128
    """

    if not is_mnemonic(mnemonic=mnemonic, language=language):
        raise ValueError("Invalid mnemonic words.")

    words = len(unicodedata.normalize("NFKD", mnemonic).split(" "))
    if words == 12:
        return 128
    elif words == 15:
        return 160
    elif words == 18:
        return 192
    elif words == 21:
        return 224
    elif words == 24:
        return 256


def get_mnemonic_language(mnemonic: str) -> str:
    """
    Get mnemonic language.

    :param mnemonic: Mnemonic words.
    :type mnemonic: str

    :returns: str -- Mnemonic language.

    >>> from hdwallet.utils import get_mnemonic_language
    >>> get_mnemonic_language(mnemonic="sceptre capter séquence girafe absolu relatif fleur zoologie muscle sirop saboter parure")
    "french"
    """

    if not is_mnemonic(mnemonic=mnemonic):
        raise ValueError("Invalid mnemonic words.")

    language = None
    mnemonic = unicodedata.normalize("NFKD", mnemonic)
    for _language in ["english", "french", "italian",
                      "chinese_simplified", "chinese_traditional", "japanese", "korean", "spanish"]:
        if Mnemonic(language=_language).check(mnemonic=mnemonic) is True:
            language = _language
            break
    return language


def entropy_to_mnemonic(entropy: str, language: str = "english") -> str:
    """
    Get mnemonic from entropy hex string.

    :param entropy: Entropy hex string.
    :type entropy: str
    :param language: Mnemonic language, default to english.
    :type language: str

    :returns: str -- Mnemonic words.

    >>> from hdwallet.utils import entropy_to_mnemonic
    >>> entropy_to_mnemonic(entropy="ee535b143b0d9d1f87546f9df0d06b1a", language="korean")
    "학력 외침 주민 스위치 출연 연습 근본 여전히 울음 액수 귀신 마누라"
    """

    if not is_entropy(entropy=entropy):
        raise ValueError("Invalid entropy hex string.")

    if language and language not in ["english", "french", "italian", "japanese",
                                     "chinese_simplified", "chinese_traditional", "korean", "spanish"]:
        raise ValueError("Invalid language, use only this options english, french, "
                         "italian, spanish, chinese_simplified, chinese_traditional, japanese or korean languages.")

    return Mnemonic(language=language).to_mnemonic(unhexlify(entropy))


def mnemonic_to_entropy(mnemonic: str, language: Optional[str] = None) -> str:
    """
    Get entropy from mnemonic words.

    :param mnemonic: Mnemonic words.
    :type mnemonic: str
    :param language: Mnemonic language, default to english.
    :type language: str

    :returns: str -- Enropy hex string.

    >>> from hdwallet.utils import mnemonic_to_entropy
    >>> mnemonic_to_entropy(mnemonic="학력 외침 주민 스위치 출연 연습 근본 여전히 울음 액수 귀신 마누라", language="korean")
    "ee535b143b0d9d1f87546f9df0d06b1a"
    """

    if not is_mnemonic(mnemonic=mnemonic, language=language):
        raise ValueError("Invalid mnemonic words.")

    mnemonic = unicodedata.normalize("NFKD", mnemonic)
    language = language if language else get_mnemonic_language(mnemonic=mnemonic)
    return Mnemonic(language=language).to_entropy(mnemonic).hex()


def is_root_xprivate_key(xprivate_key: str, symbol: str) -> bool:
    decoded_xprivate_key = check_decode(xprivate_key)
    if len(decoded_xprivate_key) != 78:  # 78, 156
        raise ValueError("Invalid xprivate key.")
    cryptocurrency = get_cryptocurrency(symbol=symbol)
    semantic = get_semantic(_cryptocurrency=cryptocurrency, version=decoded_xprivate_key[:4], key_type="private_key")
    version = cryptocurrency.EXTENDED_PRIVATE_KEY.__getattribute__(
        semantic.upper()
    )
    if version is None:
        raise NotImplementedError(semantic)
    raw = f"{_unhexlify(version).hex()}000000000000000000"
    return decoded_xprivate_key.hex().startswith(raw)


def is_root_xpublic_key(xpublic_key: str, symbol: str) -> bool:
    decoded_xpublic_key = check_decode(xpublic_key)
    if len(decoded_xpublic_key) != 78:  # 78, 156
        raise ValueError("Invalid xpublic key.")
    cryptocurrency = get_cryptocurrency(symbol=symbol)
    semantic = get_semantic(_cryptocurrency=cryptocurrency, version=decoded_xpublic_key[:4], key_type="public_key")
    version = cryptocurrency.EXTENDED_PUBLIC_KEY.__getattribute__(
        semantic.upper()
    )
    if version is None:
        raise NotImplementedError(semantic)
    raw = f"{_unhexlify(version).hex()}000000000000000000"
    return decoded_xpublic_key.hex().startswith(raw)
