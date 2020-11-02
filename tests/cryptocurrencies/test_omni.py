#!/usr/bin/env python3

import json
import os

from python_hdwallet import PythonHDWallet
from python_hdwallet.symbols import OMNI, OMNITEST

# Test Values
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_ = json.loads(values.read())
values.close()


def test_omni_mainnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["omni"]["mainnet"]["symbol"]
    )
    
    python_hdwallet.from_entropy(
        entropy=_["omni"]["mainnet"]["entropy"],
        passphrase=_["omni"]["mainnet"]["passphrase"],
        language=_["omni"]["mainnet"]["language"]
    ).from_path(
        path=_["omni"]["mainnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["omni"]["mainnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["omni"]["mainnet"]["symbol"] == OMNI
    assert python_hdwallet.network() == _["omni"]["mainnet"]["network"]
    assert python_hdwallet.strength() == _["omni"]["mainnet"]["strength"]
    assert python_hdwallet.entropy() == _["omni"]["mainnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["omni"]["mainnet"]["mnemonic"]
    assert python_hdwallet.language() == _["omni"]["mainnet"]["language"]
    assert python_hdwallet.passphrase() == _["omni"]["mainnet"]["passphrase"]
    assert python_hdwallet.seed() == _["omni"]["mainnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["omni"]["mainnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["omni"]["mainnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["omni"]["mainnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["omni"]["mainnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["omni"]["mainnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["omni"]["mainnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["omni"]["mainnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["omni"]["mainnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["omni"]["mainnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["omni"]["mainnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["omni"]["mainnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["omni"]["mainnet"]["private_key"]
    assert python_hdwallet.public_key() == _["omni"]["mainnet"]["public_key"]
    assert python_hdwallet.wif() == _["omni"]["mainnet"]["wif"]
    assert python_hdwallet.identifier() == _["omni"]["mainnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["omni"]["mainnet"]["finger_print"]
    assert python_hdwallet.path() == _["omni"]["mainnet"]["path"]
    assert python_hdwallet.address() == _["omni"]["mainnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["omni"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps


def test_omni_testnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["omni"]["testnet"]["symbol"]
    )

    python_hdwallet.from_entropy(
        entropy=_["omni"]["testnet"]["entropy"],
        passphrase=_["omni"]["testnet"]["passphrase"],
        language=_["omni"]["testnet"]["language"]
    ).from_path(
        path=_["omni"]["testnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["omni"]["testnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["omni"]["testnet"]["symbol"] == OMNITEST
    assert python_hdwallet.network() == _["omni"]["testnet"]["network"]
    assert python_hdwallet.strength() == _["omni"]["testnet"]["strength"]
    assert python_hdwallet.entropy() == _["omni"]["testnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["omni"]["testnet"]["mnemonic"]
    assert python_hdwallet.language() == _["omni"]["testnet"]["language"]
    assert python_hdwallet.passphrase() == _["omni"]["testnet"]["passphrase"]
    assert python_hdwallet.seed() == _["omni"]["testnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["omni"]["testnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["omni"]["testnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["omni"]["testnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["omni"]["testnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["omni"]["testnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["omni"]["testnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["omni"]["testnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["omni"]["testnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["omni"]["testnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["omni"]["testnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["omni"]["testnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["omni"]["testnet"]["private_key"]
    assert python_hdwallet.public_key() == _["omni"]["testnet"]["public_key"]
    assert python_hdwallet.wif() == _["omni"]["testnet"]["wif"]
    assert python_hdwallet.identifier() == _["omni"]["testnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["omni"]["testnet"]["finger_print"]
    assert python_hdwallet.path() == _["omni"]["testnet"]["path"]
    assert python_hdwallet.address() == _["omni"]["testnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["omni"]["testnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
