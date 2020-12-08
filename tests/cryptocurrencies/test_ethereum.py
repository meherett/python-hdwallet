#!/usr/bin/env python3

import json
import os

from hdwallet import HDWallet
from hdwallet.symbols import ETH, ETHTEST

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_ethereum_mainnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["ethereum"]["mainnet"]["symbol"]
    )
    
    hdwallet.from_entropy(
        entropy=_["ethereum"]["mainnet"]["entropy"],
        passphrase=_["ethereum"]["mainnet"]["passphrase"],
        language=_["ethereum"]["mainnet"]["language"]
    ).from_path(
        path=_["ethereum"]["mainnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["ethereum"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["ethereum"]["mainnet"]["symbol"] == ETH
    assert hdwallet.network() == _["ethereum"]["mainnet"]["network"]
    assert hdwallet.strength() == _["ethereum"]["mainnet"]["strength"]
    assert hdwallet.entropy() == _["ethereum"]["mainnet"]["entropy"]
    assert hdwallet.mnemonic() == _["ethereum"]["mainnet"]["mnemonic"]
    assert hdwallet.language() == _["ethereum"]["mainnet"]["language"]
    assert hdwallet.passphrase() == _["ethereum"]["mainnet"]["passphrase"]
    assert hdwallet.seed() == _["ethereum"]["mainnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["ethereum"]["mainnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["ethereum"]["mainnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["ethereum"]["mainnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["ethereum"]["mainnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["ethereum"]["mainnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["ethereum"]["mainnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["ethereum"]["mainnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["ethereum"]["mainnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["ethereum"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["ethereum"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() == _["ethereum"]["mainnet"]["chain_code"]
    assert hdwallet.private_key() == _["ethereum"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["ethereum"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["ethereum"]["mainnet"]["wif"]
    assert hdwallet.identifier() == _["ethereum"]["mainnet"]["identifier"]
    assert hdwallet.finger_print() == _["ethereum"]["mainnet"]["finger_print"]
    assert hdwallet.path() == _["ethereum"]["mainnet"]["path"]
    assert hdwallet.address() == _["ethereum"]["mainnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["ethereum"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps


def test_ethereum_testnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["ethereum"]["testnet"]["symbol"]
    )

    hdwallet.from_entropy(
        entropy=_["ethereum"]["testnet"]["entropy"],
        passphrase=_["ethereum"]["testnet"]["passphrase"],
        language=_["ethereum"]["testnet"]["language"]
    ).from_path(
        path=_["ethereum"]["testnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["ethereum"]["testnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["ethereum"]["testnet"]["symbol"] == ETHTEST
    assert hdwallet.network() == _["ethereum"]["testnet"]["network"]
    assert hdwallet.strength() == _["ethereum"]["testnet"]["strength"]
    assert hdwallet.entropy() == _["ethereum"]["testnet"]["entropy"]
    assert hdwallet.mnemonic() == _["ethereum"]["testnet"]["mnemonic"]
    assert hdwallet.language() == _["ethereum"]["testnet"]["language"]
    assert hdwallet.passphrase() == _["ethereum"]["testnet"]["passphrase"]
    assert hdwallet.seed() == _["ethereum"]["testnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["ethereum"]["testnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["ethereum"]["testnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["ethereum"]["testnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["ethereum"]["testnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["ethereum"]["testnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["ethereum"]["testnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["ethereum"]["testnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["ethereum"]["testnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["ethereum"]["testnet"]["uncompressed"]
    assert hdwallet.compressed() == _["ethereum"]["testnet"]["compressed"]
    assert hdwallet.chain_code() == _["ethereum"]["testnet"]["chain_code"]
    assert hdwallet.private_key() == _["ethereum"]["testnet"]["private_key"]
    assert hdwallet.public_key() == _["ethereum"]["testnet"]["public_key"]
    assert hdwallet.wif() == _["ethereum"]["testnet"]["wif"]
    assert hdwallet.identifier() == _["ethereum"]["testnet"]["identifier"]
    assert hdwallet.finger_print() == _["ethereum"]["testnet"]["finger_print"]
    assert hdwallet.path() == _["ethereum"]["testnet"]["path"]
    assert hdwallet.address() == _["ethereum"]["testnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["ethereum"]["testnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
