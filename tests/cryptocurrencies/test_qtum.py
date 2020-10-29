#!/usr/bin/env python3

import json
import os

from python_hdwallet import PythonHDWallet
from python_hdwallet.symbols import QTUM, QTUMTEST

# Test Values
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_ = json.loads(values.read())
values.close()


def test_qtum_mainnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["qtum"]["mainnet"]["symbol"]
    )
    
    python_hdwallet.from_entropy(
        entropy=_["qtum"]["mainnet"]["entropy"],
        passphrase=_["qtum"]["mainnet"]["passphrase"],
        language=_["qtum"]["mainnet"]["language"]
    ).from_path(
        path=_["qtum"]["mainnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["qtum"]["mainnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["qtum"]["mainnet"]["symbol"] == QTUM
    assert python_hdwallet.network() == _["qtum"]["mainnet"]["network"]
    assert python_hdwallet.entropy() == _["qtum"]["mainnet"]["entropy"]
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

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps


def test_qtum_testnet():

    python_hdwallet: PythonHDWallet = PythonHDWallet(
        symbol=_["qtum"]["testnet"]["symbol"]
    )

    python_hdwallet.from_entropy(
        entropy=_["qtum"]["testnet"]["entropy"],
        passphrase=_["qtum"]["testnet"]["passphrase"],
        language=_["qtum"]["testnet"]["language"]
    ).from_path(
        path=_["qtum"]["testnet"]["path"]
    )

    assert python_hdwallet.cryptocurrency() == _["qtum"]["testnet"]["cryptocurrency"]
    assert python_hdwallet.symbol() == _["qtum"]["testnet"]["symbol"] == QTUMTEST
    assert python_hdwallet.network() == _["qtum"]["testnet"]["network"]
    assert python_hdwallet.entropy() == _["qtum"]["testnet"]["entropy"]
    assert python_hdwallet.mnemonic() == _["qtum"]["testnet"]["mnemonic"]
    assert python_hdwallet.language() == _["qtum"]["testnet"]["language"]
    assert python_hdwallet.passphrase() == _["qtum"]["testnet"]["passphrase"]
    assert python_hdwallet.seed() == _["qtum"]["testnet"]["seed"]
    assert python_hdwallet.root_xprivate_key(encoded=False) == _["qtum"]["testnet"]["root_xprivate_key_hex"]
    assert python_hdwallet.root_xprivate_key() == _["qtum"]["testnet"]["root_xprivate_key"]
    assert python_hdwallet.root_xpublic_key(encoded=False) == _["qtum"]["testnet"]["root_xpublic_key_hex"]
    assert python_hdwallet.root_xpublic_key() == _["qtum"]["testnet"]["root_xpublic_key"]
    assert python_hdwallet.xprivate_key(encoded=False) == _["qtum"]["testnet"]["xprivate_key_hex"]
    assert python_hdwallet.xprivate_key() == _["qtum"]["testnet"]["xprivate_key"]
    assert python_hdwallet.xpublic_key(encoded=False) == _["qtum"]["testnet"]["xpublic_key_hex"]
    assert python_hdwallet.xpublic_key() == _["qtum"]["testnet"]["xpublic_key"]
    assert python_hdwallet.uncompressed() == _["qtum"]["testnet"]["uncompressed"]
    assert python_hdwallet.compressed() == _["qtum"]["testnet"]["compressed"]
    assert python_hdwallet.chain_code() == _["qtum"]["testnet"]["chain_code"]
    assert python_hdwallet.private_key() == _["qtum"]["testnet"]["private_key"]
    assert python_hdwallet.public_key() == _["qtum"]["testnet"]["public_key"]
    assert python_hdwallet.wif() == _["qtum"]["testnet"]["wif"]
    assert python_hdwallet.identifier() == _["qtum"]["testnet"]["identifier"]
    assert python_hdwallet.finger_print() == _["qtum"]["testnet"]["finger_print"]
    assert python_hdwallet.path() == _["qtum"]["testnet"]["path"]
    assert python_hdwallet.address() == _["qtum"]["testnet"]["address"]

    assert isinstance(python_hdwallet.dumps(), dict)

    dumps: dict = _["qtum"]["testnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert python_hdwallet.dumps() == dumps
