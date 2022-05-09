#!/usr/bin/env python3

import json
import os

from hdwallet import HDWallet

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "../values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_from_xpublic_key():

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )
    # account_extended_xpublic_key path m/44'/0'/0'
    hdwallet.from_xpublic_key(
        _["bitcoin"]["mainnet"]["account_extended_xpublic_key"]
    )
    # the xpublic_key path m/44'/0'/0'/0/0
    hdwallet.from_path(
        path="m/0/0"
    )

    assert hdwallet.cryptocurrency() == _["bitcoin"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["bitcoin"]["mainnet"]["symbol"]
    assert hdwallet.network() == _["bitcoin"]["mainnet"]["network"]
    # root_xpublic_key see hdwallet.from_xpublic_key(first_from_xpublic_key)
    assert hdwallet.root_xpublic_key() == _["bitcoin"]["mainnet"]["account_extended_xpublic_key"]

    assert hdwallet.public_key() == _["bitcoin"]["mainnet"]["public_key"]
    assert hdwallet.p2pkh_address() == _["bitcoin"]["mainnet"]["addresses"]["p2pkh"]
    assert hdwallet.p2sh_address() ==  _["bitcoin"]["mainnet"]["addresses"]["p2sh"]
    assert hdwallet.p2wpkh_address() == _["bitcoin"]["mainnet"]["addresses"]["p2wpkh"]
    assert hdwallet.p2wpkh_in_p2sh_address() == _["bitcoin"]["mainnet"]["addresses"]["p2wpkh_in_p2sh"]
    assert hdwallet.p2wsh_address() == _["bitcoin"]["mainnet"]["addresses"]["p2wsh"]
    assert hdwallet.p2wsh_in_p2sh_address() == _["bitcoin"]["mainnet"]["addresses"]["p2wsh_in_p2sh"]

    assert isinstance(hdwallet.dumps(), dict)

