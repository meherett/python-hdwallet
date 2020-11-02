#!/usr/bin/env python3

import json
import os

from python_hdwallet import PythonHDWallet
from python_hdwallet.symbols import BTC, BTCTEST

# Test Values
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_ = json.loads(values.read())
values.close()


def test_bitcoin_mainnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )

    python_hdwallet.from_entropy(
        entropy=_["bitcoin"]["mainnet"]["entropy"],
        passphrase=_["bitcoin"]["mainnet"]["passphrase"],
        language=_["bitcoin"]["mainnet"]["language"]
    ).from_path(
        path=_["bitcoin"]["mainnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["bitcoin"]["mainnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["bitcoin"]["mainnet"]["symbol"] == BTC
    assert python_hdwallet.network() == _["bitcoin"]["mainnet"]["network"]
    assert python_hdwallet.strength() == _["bitcoin"]["mainnet"]["strength"]
    assert python_hdwallet.entropy() == _["bitcoin"]["mainnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["bitcoin"]["mainnet"]["mnemonic"]
    assert python_hdwallet.language() == _["bitcoin"]["mainnet"]["language"]
    assert python_hdwallet.passphrase() == _["bitcoin"]["mainnet"]["passphrase"]
    assert python_hdwallet.seed() == _["bitcoin"]["mainnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["bitcoin"]["mainnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["bitcoin"]["mainnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["bitcoin"]["mainnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["bitcoin"]["mainnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["bitcoin"]["mainnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["bitcoin"]["mainnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["bitcoin"]["mainnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["bitcoin"]["mainnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["bitcoin"]["mainnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["bitcoin"]["mainnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["bitcoin"]["mainnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["bitcoin"]["mainnet"]["private_key"]
    assert python_hdwallet.public_key() == _["bitcoin"]["mainnet"]["public_key"]
    assert python_hdwallet.wif() == _["bitcoin"]["mainnet"]["wif"]
    assert python_hdwallet.identifier() == _["bitcoin"]["mainnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["bitcoin"]["mainnet"]["finger_print"]
    assert python_hdwallet.path() == _["bitcoin"]["mainnet"]["path"]
    assert python_hdwallet.address() == _["bitcoin"]["mainnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["bitcoin"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps


def test_bitcoin_testnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["bitcoin"]["testnet"]["symbol"]
    )

    python_hdwallet.from_entropy(
        entropy=_["bitcoin"]["testnet"]["entropy"],
        passphrase=_["bitcoin"]["testnet"]["passphrase"],
        language=_["bitcoin"]["testnet"]["language"]
    ).from_path(
        path=_["bitcoin"]["testnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["bitcoin"]["testnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["bitcoin"]["testnet"]["symbol"] == BTCTEST
    assert python_hdwallet.network() == _["bitcoin"]["testnet"]["network"]
    assert python_hdwallet.strength() == _["bitcoin"]["testnet"]["strength"]
    assert python_hdwallet.entropy() == _["bitcoin"]["testnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["bitcoin"]["testnet"]["mnemonic"]
    assert python_hdwallet.language() == _["bitcoin"]["testnet"]["language"]
    assert python_hdwallet.passphrase() == _["bitcoin"]["testnet"]["passphrase"]
    assert python_hdwallet.seed() == _["bitcoin"]["testnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["bitcoin"]["testnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["bitcoin"]["testnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["bitcoin"]["testnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["bitcoin"]["testnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["bitcoin"]["testnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["bitcoin"]["testnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["bitcoin"]["testnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["bitcoin"]["testnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["bitcoin"]["testnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["bitcoin"]["testnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["bitcoin"]["testnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["bitcoin"]["testnet"]["private_key"]
    assert python_hdwallet.public_key() == _["bitcoin"]["testnet"]["public_key"]
    assert python_hdwallet.wif() == _["bitcoin"]["testnet"]["wif"]
    assert python_hdwallet.identifier() == _["bitcoin"]["testnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["bitcoin"]["testnet"]["finger_print"]
    assert python_hdwallet.path() == _["bitcoin"]["testnet"]["path"]
    assert python_hdwallet.address() == _["bitcoin"]["testnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["bitcoin"]["testnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
