#!/usr/bin/env python3

import json
import os

from python_hdwallet import PythonHDWallet

# Test Values
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "values.json"))
values = open(file_path, "r", encoding="utf-8")
_ = json.loads(values.read())
values.close()


def test_from_mnemonic():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["qtum"]["mainnet"]["symbol"]
    )
    
    python_hdwallet.from_mnemonic(
        mnemonic=_["qtum"]["mainnet"]["mnemonic"],
        passphrase=_["qtum"]["mainnet"]["passphrase"],
        language=_["qtum"]["mainnet"]["language"]
    ).from_path(
        path=_["qtum"]["mainnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["qtum"]["mainnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["qtum"]["mainnet"]["symbol"]
    assert python_hdwallet.network() == _["qtum"]["mainnet"]["network"]
    assert python_hdwallet.entropy() is None
    assert python_hdwallet.mnemonic() == _["qtum"]["mainnet"]["mnemonic"]
    assert python_hdwallet.language() == _["qtum"]["mainnet"]["language"]
    assert python_hdwallet.passphrase() == _["qtum"]["mainnet"]["passphrase"]
    assert python_hdwallet.seed() == _["qtum"]["mainnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["qtum"]["mainnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["qtum"]["mainnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["qtum"]["mainnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["qtum"]["mainnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["qtum"]["mainnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["qtum"]["mainnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["qtum"]["mainnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["qtum"]["mainnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["qtum"]["mainnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["qtum"]["mainnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["qtum"]["mainnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["qtum"]["mainnet"]["private_key"]
    assert python_hdwallet.public_key() == _["qtum"]["mainnet"]["public_key"]
    assert python_hdwallet.wif() == _["qtum"]["mainnet"]["wif"]
    assert python_hdwallet.identifier() == _["qtum"]["mainnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["qtum"]["mainnet"]["finger_print"]
    assert python_hdwallet.path() == _["qtum"]["mainnet"]["path"]
    assert python_hdwallet.address() == _["qtum"]["mainnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["qtum"]["mainnet"]

    dumps["entropy"] = None
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
