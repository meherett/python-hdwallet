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


def test_from_seed():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["dash"]["testnet"]["symbol"]
    )
    
    python_hdwallet.from_seed(
        seed=_["dash"]["testnet"]["seed"]
    ).from_path(
        path=_["dash"]["testnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["dash"]["testnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["dash"]["testnet"]["symbol"]
    assert python_hdwallet.network() == _["dash"]["testnet"]["network"]
    assert python_hdwallet.entropy() is None
    assert python_hdwallet.mnemonic() is None
    assert python_hdwallet.language() is None
    assert python_hdwallet.passphrase() is None
    assert python_hdwallet.seed() == _["dash"]["testnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["dash"]["testnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["dash"]["testnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["dash"]["testnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["dash"]["testnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["dash"]["testnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["dash"]["testnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["dash"]["testnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["dash"]["testnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["dash"]["testnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["dash"]["testnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["dash"]["testnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["dash"]["testnet"]["private_key"]
    assert python_hdwallet.public_key() == _["dash"]["testnet"]["public_key"]
    assert python_hdwallet.wif() == _["dash"]["testnet"]["wif"]
    assert python_hdwallet.identifier() == _["dash"]["testnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["dash"]["testnet"]["finger_print"]
    assert python_hdwallet.path() == _["dash"]["testnet"]["path"]
    assert python_hdwallet.address() == _["dash"]["testnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["dash"]["testnet"]

    dumps["entropy"] = None
    dumps["mnemonic"] = None
    dumps["language"] = None
    dumps["passphrase"] = None
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
