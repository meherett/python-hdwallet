#!/usr/bin/env python3

import json
import os

from hdwallet import HDWallet
from hdwallet.symbols import DASH, DASHTEST

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_dash_mainnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["dash"]["mainnet"]["symbol"]
    )
    
    hdwallet.from_entropy(
        entropy=_["dash"]["mainnet"]["entropy"],
        passphrase=_["dash"]["mainnet"]["passphrase"],
        language=_["dash"]["mainnet"]["language"]
    ).from_path(
        path=_["dash"]["mainnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["dash"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["dash"]["mainnet"]["symbol"] == DASH
    assert hdwallet.network() == _["dash"]["mainnet"]["network"]
    assert hdwallet.strength() == _["dash"]["mainnet"]["strength"]
    assert hdwallet.entropy() == _["dash"]["mainnet"]["entropy"]
    assert hdwallet.mnemonic() == _["dash"]["mainnet"]["mnemonic"]
    assert hdwallet.language() == _["dash"]["mainnet"]["language"]
    assert hdwallet.passphrase() == _["dash"]["mainnet"]["passphrase"]
    assert hdwallet.seed() == _["dash"]["mainnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["dash"]["mainnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["dash"]["mainnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["dash"]["mainnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["dash"]["mainnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["dash"]["mainnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["dash"]["mainnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["dash"]["mainnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["dash"]["mainnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["dash"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["dash"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() == _["dash"]["mainnet"]["chain_code"]
    assert hdwallet.private_key() == _["dash"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["dash"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["dash"]["mainnet"]["wif"]
    assert hdwallet.identifier() == _["dash"]["mainnet"]["identifier"]
    assert hdwallet.finger_print() == _["dash"]["mainnet"]["finger_print"]
    assert hdwallet.path() == _["dash"]["mainnet"]["path"]
    assert hdwallet.address() == _["dash"]["mainnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["dash"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps


def test_dash_testnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["dash"]["testnet"]["symbol"]
    )

    hdwallet.from_entropy(
        entropy=_["dash"]["testnet"]["entropy"],
        passphrase=_["dash"]["testnet"]["passphrase"],
        language=_["dash"]["testnet"]["language"]
    ).from_path(
        path=_["dash"]["testnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["dash"]["testnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["dash"]["testnet"]["symbol"] == DASHTEST
    assert hdwallet.network() == _["dash"]["testnet"]["network"]
    assert hdwallet.strength() == _["dash"]["testnet"]["strength"]
    assert hdwallet.entropy() == _["dash"]["testnet"]["entropy"]
    assert hdwallet.mnemonic() == _["dash"]["testnet"]["mnemonic"]
    assert hdwallet.language() == _["dash"]["testnet"]["language"]
    assert hdwallet.passphrase() == _["dash"]["testnet"]["passphrase"]
    assert hdwallet.seed() == _["dash"]["testnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["dash"]["testnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["dash"]["testnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["dash"]["testnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["dash"]["testnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["dash"]["testnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["dash"]["testnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["dash"]["testnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["dash"]["testnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["dash"]["testnet"]["uncompressed"]
    assert hdwallet.compressed() == _["dash"]["testnet"]["compressed"]
    assert hdwallet.chain_code() == _["dash"]["testnet"]["chain_code"]
    assert hdwallet.private_key() == _["dash"]["testnet"]["private_key"]
    assert hdwallet.public_key() == _["dash"]["testnet"]["public_key"]
    assert hdwallet.wif() == _["dash"]["testnet"]["wif"]
    assert hdwallet.identifier() == _["dash"]["testnet"]["identifier"]
    assert hdwallet.finger_print() == _["dash"]["testnet"]["finger_print"]
    assert hdwallet.path() == _["dash"]["testnet"]["path"]
    assert hdwallet.address() == _["dash"]["testnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["dash"]["testnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
