#!/usr/bin/env python3

import json
import unicodedata
import os

from hdwallet.utils import (
    get_bytes, generate_mnemonic, generate_entropy, is_entropy, get_mnemonic_strength,
    get_entropy_strength, is_mnemonic, get_mnemonic_language, entropy_to_mnemonic, mnemonic_to_entropy,
    is_root_xprivate_key, is_root_xpublic_key, generate_passphrase
)

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_utils():

    assert isinstance(get_bytes(string=b"meherett"), bytes)

    assert is_root_xprivate_key(
        xprivate_key=_["bitcoin"]["mainnet"]["root_xprivate_key"],
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )
    assert not is_root_xprivate_key(
        xprivate_key=_["bitcoin"]["mainnet"]["xprivate_key"],
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )

    assert is_root_xpublic_key(
        xpublic_key=_["bitcoin"]["mainnet"]["root_xpublic_key"],
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )
    assert not is_root_xpublic_key(
        xpublic_key=_["bitcoin"]["mainnet"]["xpublic_key"],
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )

    assert len(generate_passphrase(length=19999)) == 19999


def test_utils_entropy():

    assert len(generate_entropy(strength=128)) == 32
    assert len(generate_entropy(strength=160)) == 40
    assert len(generate_entropy(strength=192)) == 48
    assert len(generate_entropy(strength=224)) == 56
    assert len(generate_entropy(strength=256)) == 64

    for entropy in _["utils"]["entropy"]:

        assert len(entropy["entropy"]) == entropy["length"]
        assert get_entropy_strength(entropy["entropy"]) == entropy["strength"]
        assert is_entropy(entropy["entropy"])

    assert mnemonic_to_entropy(
        mnemonic=_["bitcoin"]["mainnet"]["mnemonic"], language=_["bitcoin"]["mainnet"]["language"]
    ) == _["bitcoin"]["mainnet"]["entropy"]


def test_utils_mnemonic():

    assert len(generate_mnemonic(strength=128).split(" ")) == 12
    assert len(generate_mnemonic(strength=160).split(" ")) == 15
    assert len(generate_mnemonic(strength=192).split(" ")) == 18
    assert len(generate_mnemonic(strength=224).split(" ")) == 21
    assert len(generate_mnemonic(strength=256).split(" ")) == 24

    for mnemonic in _["utils"]["mnemonic"]:

        assert len(unicodedata.normalize("NFKD", mnemonic["mnemonic"]).split(" ")) == mnemonic["words"]
        assert get_mnemonic_strength(mnemonic["mnemonic"]) == mnemonic["strength"]
        assert is_mnemonic(mnemonic["mnemonic"])
        if mnemonic["language"] == "english":
            assert not is_mnemonic(mnemonic["mnemonic"], "korean")
        assert is_mnemonic(mnemonic["mnemonic"], mnemonic["language"])
        assert get_mnemonic_language(mnemonic["mnemonic"]) == mnemonic["language"]

    assert entropy_to_mnemonic(
        entropy=_["bitcoin"]["mainnet"]["entropy"], language=_["bitcoin"]["mainnet"]["language"]
    ) == _["bitcoin"]["mainnet"]["mnemonic"]
