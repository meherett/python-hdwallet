#!/usr/bin/env python3

from python_hdwallet.utils import (
    generate_mnemonic, generate_entropy, is_mnemonic, get_bytes, get_mnemonic_language
)

MNEMONIC = "병아리 실컷 여인 축제 극히 저녁 경찰 설사 할인 해물 시각 자가용"


def test_utils():

    assert len(generate_entropy(strength=128)) == 32

    assert len(generate_mnemonic(language="chinese_traditional", strength=128).split(" ")) == 12

    assert get_mnemonic_language(mnemonic=MNEMONIC) == "korean"

    assert is_mnemonic(mnemonic=MNEMONIC, language="korean")

    assert not is_mnemonic(mnemonic=MNEMONIC, language="english")

    assert isinstance(get_bytes(string=b"meherett"), bytes)
