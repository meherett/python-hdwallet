#!/usr/bin/env python3

import json
import os

from python_hdwallet import PythonHDWallet
from python_hdwallet.symbols import DASH, DASHTEST

# Test Values
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_ = json.loads(values.read())
values.close()


def test_dash_mainnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["dash"]["mainnet"]["symbol"]
    )
    
    python_hdwallet.from_entropy(
        entropy=_["dash"]["mainnet"]["entropy"],
        passphrase=_["dash"]["mainnet"]["passphrase"],
        language=_["dash"]["mainnet"]["language"]
    ).from_path(
        path=_["dash"]["mainnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["dash"]["mainnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["dash"]["mainnet"]["symbol"] == DASH
    assert python_hdwallet.network() == _["dash"]["mainnet"]["network"]
    assert python_hdwallet.strength() == _["dash"]["mainnet"]["strength"]
    assert python_hdwallet.entropy() == _["dash"]["mainnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["dash"]["mainnet"]["mnemonic"]
    assert python_hdwallet.language() == _["dash"]["mainnet"]["language"]
    assert python_hdwallet.passphrase() == _["dash"]["mainnet"]["passphrase"]
    assert python_hdwallet.seed() == _["dash"]["mainnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["dash"]["mainnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["dash"]["mainnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["dash"]["mainnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["dash"]["mainnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["dash"]["mainnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["dash"]["mainnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["dash"]["mainnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["dash"]["mainnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["dash"]["mainnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["dash"]["mainnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["dash"]["mainnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["dash"]["mainnet"]["private_key"]
    assert python_hdwallet.public_key() == _["dash"]["mainnet"]["public_key"]
    assert python_hdwallet.wif() == _["dash"]["mainnet"]["wif"]
    assert python_hdwallet.identifier() == _["dash"]["mainnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["dash"]["mainnet"]["finger_print"]
    assert python_hdwallet.path() == _["dash"]["mainnet"]["path"]
    assert python_hdwallet.address() == _["dash"]["mainnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["dash"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps


def test_dash_testnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["dash"]["testnet"]["symbol"]
    )

    python_hdwallet.from_entropy(
        entropy=_["dash"]["testnet"]["entropy"],
        passphrase=_["dash"]["testnet"]["passphrase"],
        language=_["dash"]["testnet"]["language"]
    ).from_path(
        path=_["dash"]["testnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["dash"]["testnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["dash"]["testnet"]["symbol"] == DASHTEST
    assert python_hdwallet.network() == _["dash"]["testnet"]["network"]
    assert python_hdwallet.strength() == _["dash"]["testnet"]["strength"]
    assert python_hdwallet.entropy() == _["dash"]["testnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["dash"]["testnet"]["mnemonic"]
    assert python_hdwallet.language() == _["dash"]["testnet"]["language"]
    assert python_hdwallet.passphrase() == _["dash"]["testnet"]["passphrase"]
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

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
