#!/usr/bin/env python3

import json
import os

from python_hdwallet import PythonHDWallet
from python_hdwallet.symbols import DOGE, DOGETEST

# Test Values
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_ = json.loads(values.read())
values.close()


def test_dogecoin_mainnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["dogecoin"]["mainnet"]["symbol"]
    )
    
    python_hdwallet.from_entropy(
        entropy=_["dogecoin"]["mainnet"]["entropy"],
        passphrase=_["dogecoin"]["mainnet"]["passphrase"],
        language=_["dogecoin"]["mainnet"]["language"]
    ).from_path(
        path=_["dogecoin"]["mainnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["dogecoin"]["mainnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["dogecoin"]["mainnet"]["symbol"] == DOGE
    assert python_hdwallet.network() == _["dogecoin"]["mainnet"]["network"]
    assert python_hdwallet.strength() == _["dogecoin"]["mainnet"]["strength"]
    assert python_hdwallet.entropy() == _["dogecoin"]["mainnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["dogecoin"]["mainnet"]["mnemonic"]
    assert python_hdwallet.language() == _["dogecoin"]["mainnet"]["language"]
    assert python_hdwallet.passphrase() == _["dogecoin"]["mainnet"]["passphrase"]
    assert python_hdwallet.seed() == _["dogecoin"]["mainnet"]["seed"]
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

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps


def test_dogecoin_testnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["dogecoin"]["testnet"]["symbol"]
    )

    python_hdwallet.from_entropy(
        entropy=_["dogecoin"]["testnet"]["entropy"],
        passphrase=_["dogecoin"]["testnet"]["passphrase"],
        language=_["dogecoin"]["testnet"]["language"]
    ).from_path(
        path=_["dogecoin"]["testnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["dogecoin"]["testnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["dogecoin"]["testnet"]["symbol"] == DOGETEST
    assert python_hdwallet.network() == _["dogecoin"]["testnet"]["network"]
    assert python_hdwallet.strength() == _["dogecoin"]["testnet"]["strength"]
    assert python_hdwallet.entropy() == _["dogecoin"]["testnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["dogecoin"]["testnet"]["mnemonic"]
    assert python_hdwallet.language() == _["dogecoin"]["testnet"]["language"]
    assert python_hdwallet.passphrase() == _["dogecoin"]["testnet"]["passphrase"]
    assert python_hdwallet.seed() == _["dogecoin"]["testnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["dogecoin"]["testnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["dogecoin"]["testnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["dogecoin"]["testnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["dogecoin"]["testnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["dogecoin"]["testnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["dogecoin"]["testnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["dogecoin"]["testnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["dogecoin"]["testnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["dogecoin"]["testnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["dogecoin"]["testnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["dogecoin"]["testnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["dogecoin"]["testnet"]["private_key"]
    assert python_hdwallet.public_key() == _["dogecoin"]["testnet"]["public_key"]
    assert python_hdwallet.wif() == _["dogecoin"]["testnet"]["wif"]
    assert python_hdwallet.identifier() == _["dogecoin"]["testnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["dogecoin"]["testnet"]["finger_print"]
    assert python_hdwallet.path() == _["dogecoin"]["testnet"]["path"]
    assert python_hdwallet.address() == _["dogecoin"]["testnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["dogecoin"]["testnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
