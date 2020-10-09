#!/usr/bin/env python3

from hdwallet.utils import (
    generate_mnemonic, generate_entropy, is_mnemonic, get_bytes, get_mnemonic_language
)

import pytest


MNEMONIC = "병아리 실컷 여인 축제 극히 저녁 경찰 설사 할인 해물 시각 자가용"


def test_base58():

    assert len(generate_entropy(strength=128)) == 32

    assert len(generate_mnemonic(language="chinese_traditional", strength=128).split(" ")) == 12

    with pytest.raises(ValueError, match=r".*[128, 160, 192, 224, 256].*"):
        assert len(generate_entropy(strength=129).split(" ")) == 12

    assert is_mnemonic(mnemonic=MNEMONIC, language="korean")

    with pytest.raises(ValueError, match=r"Invalid language, .*"):
        assert is_mnemonic(mnemonic=MNEMONIC, language="amharic")

    assert not is_mnemonic(mnemonic=12341234, language="english")

    with pytest.raises(TypeError, match=r".*'bytes' or 'string'.*"):
        assert get_bytes(1234)

    with pytest.raises(ValueError, match="Invalid 12 word mnemonic."):
        assert get_mnemonic_language("1234 meheret tesfaye")
