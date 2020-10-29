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


def test_from_entropy():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["ethereum"]["mainnet"]["symbol"]
    )
    
    python_hdwallet.from_entropy(
        entropy=_["ethereum"]["mainnet"]["entropy"],
        passphrase=_["ethereum"]["mainnet"]["passphrase"],
        language=_["ethereum"]["mainnet"]["language"]
    ).from_path(
        path=_["ethereum"]["mainnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["ethereum"]["mainnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["ethereum"]["mainnet"]["symbol"]
    assert python_hdwallet.network() == _["ethereum"]["mainnet"]["network"]
    assert python_hdwallet.entropy() == _["ethereum"]["mainnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["ethereum"]["mainnet"]["mnemonic"]
    assert python_hdwallet.language() == _["ethereum"]["mainnet"]["language"]
    assert python_hdwallet.passphrase() == _["ethereum"]["mainnet"]["passphrase"]
    assert python_hdwallet.seed() == _["ethereum"]["mainnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["ethereum"]["mainnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["ethereum"]["mainnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["ethereum"]["mainnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["ethereum"]["mainnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["ethereum"]["mainnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["ethereum"]["mainnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["ethereum"]["mainnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["ethereum"]["mainnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["ethereum"]["mainnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["ethereum"]["mainnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["ethereum"]["mainnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["ethereum"]["mainnet"]["private_key"]
    assert python_hdwallet.public_key() == _["ethereum"]["mainnet"]["public_key"]
    assert python_hdwallet.wif() == _["ethereum"]["mainnet"]["wif"]
    assert python_hdwallet.identifier() == _["ethereum"]["mainnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["ethereum"]["mainnet"]["finger_print"]
    assert python_hdwallet.path() == _["ethereum"]["mainnet"]["path"]
    assert python_hdwallet.address() == _["ethereum"]["mainnet"]["address"]

    python_hdwallet.clean_derivation()

    python_hdwallet.from_index(44, harden=True)
    python_hdwallet.from_index(60, harden=True)
    python_hdwallet.from_index(0, harden=True)
    python_hdwallet.from_index(0)
    python_hdwallet.from_index(0)

    assert python_hdwallet.cryptocurrency() == _["ethereum"]["mainnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["ethereum"]["mainnet"]["symbol"]
    assert python_hdwallet.network() == _["ethereum"]["mainnet"]["network"]
    assert python_hdwallet.entropy() == _["ethereum"]["mainnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["ethereum"]["mainnet"]["mnemonic"]
    assert python_hdwallet.language() == _["ethereum"]["mainnet"]["language"]
    assert python_hdwallet.passphrase() == _["ethereum"]["mainnet"]["passphrase"]
    assert python_hdwallet.seed() == _["ethereum"]["mainnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["ethereum"]["mainnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["ethereum"]["mainnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["ethereum"]["mainnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["ethereum"]["mainnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["ethereum"]["mainnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["ethereum"]["mainnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["ethereum"]["mainnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["ethereum"]["mainnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["ethereum"]["mainnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["ethereum"]["mainnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["ethereum"]["mainnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["ethereum"]["mainnet"]["private_key"]
    assert python_hdwallet.public_key() == _["ethereum"]["mainnet"]["public_key"]
    assert python_hdwallet.wif() == _["ethereum"]["mainnet"]["wif"]
    assert python_hdwallet.identifier() == _["ethereum"]["mainnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["ethereum"]["mainnet"]["finger_print"]
    assert python_hdwallet.path() == _["ethereum"]["mainnet"]["path"]
    assert python_hdwallet.address() == _["ethereum"]["mainnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["ethereum"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
