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


def test_from_root_xprivate_key():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["dogecoin"]["mainnet"]["symbol"]
    )
    
    python_hdwallet.from_root_xprivate_key(
        root_xprivate_key=_["dogecoin"]["mainnet"]["root_xprivate_key"]
    ).from_path(
        path=_["dogecoin"]["mainnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["dogecoin"]["mainnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["dogecoin"]["mainnet"]["symbol"]
    assert python_hdwallet.network() == _["dogecoin"]["mainnet"]["network"]
    assert python_hdwallet.entropy() is None
    assert python_hdwallet.mnemonic() is None
    assert python_hdwallet.language() is None
    assert python_hdwallet.passphrase() is None
    assert python_hdwallet.seed() is None
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["dogecoin"]["mainnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["dogecoin"]["mainnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["dogecoin"]["mainnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["dogecoin"]["mainnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["dogecoin"]["mainnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["dogecoin"]["mainnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["dogecoin"]["mainnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["dogecoin"]["mainnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["dogecoin"]["mainnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["dogecoin"]["mainnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["dogecoin"]["mainnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["dogecoin"]["mainnet"]["private_key"]
    assert python_hdwallet.public_key() == _["dogecoin"]["mainnet"]["public_key"]
    assert python_hdwallet.wif() == _["dogecoin"]["mainnet"]["wif"]
    assert python_hdwallet.identifier() == _["dogecoin"]["mainnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["dogecoin"]["mainnet"]["finger_print"]
    assert python_hdwallet.path() == _["dogecoin"]["mainnet"]["path"]
    assert python_hdwallet.address() == _["dogecoin"]["mainnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["dogecoin"]["mainnet"]

    dumps["entropy"] = None
    dumps["mnemonic"] = None
    dumps["language"] = None
    dumps["passphrase"] = None
    dumps["seed"] = None
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
