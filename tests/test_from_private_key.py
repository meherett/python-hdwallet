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


def test_from_private_key():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )
    
    python_hdwallet.from_private_key(
        private_key=_["bitcoin"]["mainnet"]["private_key"]
    )

    assert python_hdwallet.cryptocurrency() == _["bitcoin"]["mainnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["bitcoin"]["mainnet"]["symbol"]
    assert python_hdwallet.network() == _["bitcoin"]["mainnet"]["network"]
    assert python_hdwallet.strength() is None
    assert python_hdwallet.entropy() is None
    assert python_hdwallet.mnemonic() is None
    assert python_hdwallet.language() is None
    assert python_hdwallet.passphrase() is None
    assert python_hdwallet.seed() is None
    assert python_hdwallet.root_xprivate_key(encoded=False) is None
    assert python_hdwallet.root_xprivate_key() is None
    assert python_hdwallet.root_xpublic_key(encoded=False) is None
    assert python_hdwallet.root_xpublic_key() is None
    assert python_hdwallet.xprivate_key(encoded=False) is None
    assert python_hdwallet.xprivate_key() is None
    assert python_hdwallet.xpublic_key(encoded=False) is None
    assert python_hdwallet.xpublic_key() is None
    assert python_hdwallet.uncompressed() == _["bitcoin"]["mainnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["bitcoin"]["mainnet"]["compressed"]
    assert python_hdwallet.chain_code() is None
    assert python_hdwallet.private_key() == _["bitcoin"]["mainnet"]["private_key"]
    assert python_hdwallet.public_key() == _["bitcoin"]["mainnet"]["public_key"]
    assert python_hdwallet.wif() == _["bitcoin"]["mainnet"]["wif"]
    assert python_hdwallet.identifier() == _["bitcoin"]["mainnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["bitcoin"]["mainnet"]["finger_print"]
    assert python_hdwallet.path() is None
    assert python_hdwallet.address() == _["bitcoin"]["mainnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["bitcoin"]["mainnet"]

    dumps["strength"] = None
    dumps["entropy"] = None
    dumps["mnemonic"] = None
    dumps["language"] = None
    dumps["passphrase"] = None
    dumps["seed"] = None
    dumps["root_xprivate_key"] = None
    dumps["root_xpublic_key"] = None
    dumps["xprivate_key"] = None
    dumps["xpublic_key"] = None
    dumps["chain_code"] = None
    dumps["path"] = None
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
