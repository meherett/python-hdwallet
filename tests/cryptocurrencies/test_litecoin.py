#!/usr/bin/env python3

import json
import os

from hdwallet import HDWallet
from hdwallet.symbols import LTC, LTCTEST

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_litecoin_mainnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["litecoin"]["mainnet"]["symbol"]
    )
    
    hdwallet.from_entropy(
        entropy=_["litecoin"]["mainnet"]["entropy"],
        passphrase=_["litecoin"]["mainnet"]["passphrase"],
        language=_["litecoin"]["mainnet"]["language"]
    ).from_path(
        path=_["litecoin"]["mainnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["litecoin"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["litecoin"]["mainnet"]["symbol"] == LTC
    assert hdwallet.network() == _["litecoin"]["mainnet"]["network"]
    assert hdwallet.strength() == _["litecoin"]["mainnet"]["strength"]
    assert hdwallet.entropy() == _["litecoin"]["mainnet"]["entropy"]
    assert hdwallet.mnemonic() == _["litecoin"]["mainnet"]["mnemonic"]
    assert hdwallet.language() == _["litecoin"]["mainnet"]["language"]
    assert hdwallet.passphrase() == _["litecoin"]["mainnet"]["passphrase"]
    assert hdwallet.seed() == _["litecoin"]["mainnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["litecoin"]["mainnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["litecoin"]["mainnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["litecoin"]["mainnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["litecoin"]["mainnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["litecoin"]["mainnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["litecoin"]["mainnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["litecoin"]["mainnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["litecoin"]["mainnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["litecoin"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["litecoin"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() == _["litecoin"]["mainnet"]["chain_code"]
    assert hdwallet.private_key() == _["litecoin"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["litecoin"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["litecoin"]["mainnet"]["wif"]
    assert hdwallet.identifier() == _["litecoin"]["mainnet"]["identifier"]
    assert hdwallet.finger_print() == _["litecoin"]["mainnet"]["finger_print"]
    assert hdwallet.path() == _["litecoin"]["mainnet"]["path"]
    assert hdwallet.address() == _["litecoin"]["mainnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["litecoin"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps


def test_litecoin_testnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["litecoin"]["testnet"]["symbol"]
    )

    hdwallet.from_entropy(
        entropy=_["litecoin"]["testnet"]["entropy"],
        passphrase=_["litecoin"]["testnet"]["passphrase"],
        language=_["litecoin"]["testnet"]["language"]
    ).from_path(
        path=_["litecoin"]["testnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["litecoin"]["testnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["litecoin"]["testnet"]["symbol"] == LTCTEST
    assert hdwallet.network() == _["litecoin"]["testnet"]["network"]
    assert hdwallet.strength() == _["litecoin"]["testnet"]["strength"]
    assert hdwallet.entropy() == _["litecoin"]["testnet"]["entropy"]
    assert hdwallet.mnemonic() == _["litecoin"]["testnet"]["mnemonic"]
    assert hdwallet.language() == _["litecoin"]["testnet"]["language"]
    assert hdwallet.passphrase() == _["litecoin"]["testnet"]["passphrase"]
    assert hdwallet.seed() == _["litecoin"]["testnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["litecoin"]["testnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["litecoin"]["testnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["litecoin"]["testnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["litecoin"]["testnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["litecoin"]["testnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["litecoin"]["testnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["litecoin"]["testnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["litecoin"]["testnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["litecoin"]["testnet"]["uncompressed"]
    assert hdwallet.compressed() == _["litecoin"]["testnet"]["compressed"]
    assert hdwallet.chain_code() == _["litecoin"]["testnet"]["chain_code"]
    assert hdwallet.private_key() == _["litecoin"]["testnet"]["private_key"]
    assert hdwallet.public_key() == _["litecoin"]["testnet"]["public_key"]
    assert hdwallet.wif() == _["litecoin"]["testnet"]["wif"]
    assert hdwallet.identifier() == _["litecoin"]["testnet"]["identifier"]
    assert hdwallet.finger_print() == _["litecoin"]["testnet"]["finger_print"]
    assert hdwallet.path() == _["litecoin"]["testnet"]["path"]
    assert hdwallet.address() == _["litecoin"]["testnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["litecoin"]["testnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
