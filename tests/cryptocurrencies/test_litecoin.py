#!/usr/bin/env python3

import json
import os

from python_hdwallet import PythonHDWallet
from python_hdwallet.symbols import LTC, LTCTEST

# Test Values
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_ = json.loads(values.read())
values.close()


def test_litecoin_mainnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["litecoin"]["mainnet"]["symbol"]
    )
    
    python_hdwallet.from_entropy(
        entropy=_["litecoin"]["mainnet"]["entropy"],
        passphrase=_["litecoin"]["mainnet"]["passphrase"],
        language=_["litecoin"]["mainnet"]["language"]
    ).from_path(
        path=_["litecoin"]["mainnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["litecoin"]["mainnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["litecoin"]["mainnet"]["symbol"] == LTC
    assert python_hdwallet.network() == _["litecoin"]["mainnet"]["network"]
    assert python_hdwallet.strength() == _["litecoin"]["mainnet"]["strength"]
    assert python_hdwallet.entropy() == _["litecoin"]["mainnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["litecoin"]["mainnet"]["mnemonic"]
    assert python_hdwallet.language() == _["litecoin"]["mainnet"]["language"]
    assert python_hdwallet.passphrase() == _["litecoin"]["mainnet"]["passphrase"]
    assert python_hdwallet.seed() == _["litecoin"]["mainnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["litecoin"]["mainnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["litecoin"]["mainnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["litecoin"]["mainnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["litecoin"]["mainnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["litecoin"]["mainnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["litecoin"]["mainnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["litecoin"]["mainnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["litecoin"]["mainnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["litecoin"]["mainnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["litecoin"]["mainnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["litecoin"]["mainnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["litecoin"]["mainnet"]["private_key"]
    assert python_hdwallet.public_key() == _["litecoin"]["mainnet"]["public_key"]
    assert python_hdwallet.wif() == _["litecoin"]["mainnet"]["wif"]
    assert python_hdwallet.identifier() == _["litecoin"]["mainnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["litecoin"]["mainnet"]["finger_print"]
    assert python_hdwallet.path() == _["litecoin"]["mainnet"]["path"]
    assert python_hdwallet.address() == _["litecoin"]["mainnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["litecoin"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps


def test_litecoin_testnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["litecoin"]["testnet"]["symbol"]
    )

    python_hdwallet.from_entropy(
        entropy=_["litecoin"]["testnet"]["entropy"],
        passphrase=_["litecoin"]["testnet"]["passphrase"],
        language=_["litecoin"]["testnet"]["language"]
    ).from_path(
        path=_["litecoin"]["testnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["litecoin"]["testnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["litecoin"]["testnet"]["symbol"] == LTCTEST
    assert python_hdwallet.network() == _["litecoin"]["testnet"]["network"]
    assert python_hdwallet.strength() == _["litecoin"]["testnet"]["strength"]
    assert python_hdwallet.entropy() == _["litecoin"]["testnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["litecoin"]["testnet"]["mnemonic"]
    assert python_hdwallet.language() == _["litecoin"]["testnet"]["language"]
    assert python_hdwallet.passphrase() == _["litecoin"]["testnet"]["passphrase"]
    assert python_hdwallet.seed() == _["litecoin"]["testnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["litecoin"]["testnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["litecoin"]["testnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["litecoin"]["testnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["litecoin"]["testnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["litecoin"]["testnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["litecoin"]["testnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["litecoin"]["testnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["litecoin"]["testnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["litecoin"]["testnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["litecoin"]["testnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["litecoin"]["testnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["litecoin"]["testnet"]["private_key"]
    assert python_hdwallet.public_key() == _["litecoin"]["testnet"]["public_key"]
    assert python_hdwallet.wif() == _["litecoin"]["testnet"]["wif"]
    assert python_hdwallet.identifier() == _["litecoin"]["testnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["litecoin"]["testnet"]["finger_print"]
    assert python_hdwallet.path() == _["litecoin"]["testnet"]["path"]
    assert python_hdwallet.address() == _["litecoin"]["testnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["litecoin"]["testnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
