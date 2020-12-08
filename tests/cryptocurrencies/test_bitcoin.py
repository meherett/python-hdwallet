#!/usr/bin/env python3

import json
import os

from hdwallet import HDWallet
from hdwallet.symbols import BTC, BTCTEST

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_bitcoin_mainnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )

    hdwallet.from_entropy(
        entropy=_["bitcoin"]["mainnet"]["entropy"],
        passphrase=_["bitcoin"]["mainnet"]["passphrase"],
        language=_["bitcoin"]["mainnet"]["language"]
    ).from_path(
        path=_["bitcoin"]["mainnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["bitcoin"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["bitcoin"]["mainnet"]["symbol"] == BTC
    assert hdwallet.network() == _["bitcoin"]["mainnet"]["network"]
    assert hdwallet.strength() == _["bitcoin"]["mainnet"]["strength"]
    assert hdwallet.entropy() == _["bitcoin"]["mainnet"]["entropy"]
    assert hdwallet.mnemonic() == _["bitcoin"]["mainnet"]["mnemonic"]
    assert hdwallet.language() == _["bitcoin"]["mainnet"]["language"]
    assert hdwallet.passphrase() == _["bitcoin"]["mainnet"]["passphrase"]
    assert hdwallet.seed() == _["bitcoin"]["mainnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["bitcoin"]["mainnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["bitcoin"]["mainnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["bitcoin"]["mainnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["bitcoin"]["mainnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["bitcoin"]["mainnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["bitcoin"]["mainnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["bitcoin"]["mainnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["bitcoin"]["mainnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["bitcoin"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["bitcoin"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() == _["bitcoin"]["mainnet"]["chain_code"]
    assert hdwallet.private_key() == _["bitcoin"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["bitcoin"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["bitcoin"]["mainnet"]["wif"]
    assert hdwallet.identifier() == _["bitcoin"]["mainnet"]["identifier"]
    assert hdwallet.finger_print() == _["bitcoin"]["mainnet"]["finger_print"]
    assert hdwallet.path() == _["bitcoin"]["mainnet"]["path"]
    assert hdwallet.address() == _["bitcoin"]["mainnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["bitcoin"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps


def test_bitcoin_testnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin"]["testnet"]["symbol"]
    )

    hdwallet.from_entropy(
        entropy=_["bitcoin"]["testnet"]["entropy"],
        passphrase=_["bitcoin"]["testnet"]["passphrase"],
        language=_["bitcoin"]["testnet"]["language"]
    ).from_path(
        path=_["bitcoin"]["testnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["bitcoin"]["testnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["bitcoin"]["testnet"]["symbol"] == BTCTEST
    assert hdwallet.network() == _["bitcoin"]["testnet"]["network"]
    assert hdwallet.strength() == _["bitcoin"]["testnet"]["strength"]
    assert hdwallet.entropy() == _["bitcoin"]["testnet"]["entropy"]
    assert hdwallet.mnemonic() == _["bitcoin"]["testnet"]["mnemonic"]
    assert hdwallet.language() == _["bitcoin"]["testnet"]["language"]
    assert hdwallet.passphrase() == _["bitcoin"]["testnet"]["passphrase"]
    assert hdwallet.seed() == _["bitcoin"]["testnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["bitcoin"]["testnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["bitcoin"]["testnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["bitcoin"]["testnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["bitcoin"]["testnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["bitcoin"]["testnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["bitcoin"]["testnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["bitcoin"]["testnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["bitcoin"]["testnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["bitcoin"]["testnet"]["uncompressed"]
    assert hdwallet.compressed() == _["bitcoin"]["testnet"]["compressed"]
    assert hdwallet.chain_code() == _["bitcoin"]["testnet"]["chain_code"]
    assert hdwallet.private_key() == _["bitcoin"]["testnet"]["private_key"]
    assert hdwallet.public_key() == _["bitcoin"]["testnet"]["public_key"]
    assert hdwallet.wif() == _["bitcoin"]["testnet"]["wif"]
    assert hdwallet.identifier() == _["bitcoin"]["testnet"]["identifier"]
    assert hdwallet.finger_print() == _["bitcoin"]["testnet"]["finger_print"]
    assert hdwallet.path() == _["bitcoin"]["testnet"]["path"]
    assert hdwallet.address() == _["bitcoin"]["testnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["bitcoin"]["testnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
