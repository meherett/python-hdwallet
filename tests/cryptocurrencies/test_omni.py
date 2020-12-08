#!/usr/bin/env python3

import json
import os

from hdwallet import HDWallet
from hdwallet.symbols import OMNI, OMNITEST

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_omni_mainnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["omni"]["mainnet"]["symbol"]
    )
    
    hdwallet.from_entropy(
        entropy=_["omni"]["mainnet"]["entropy"],
        passphrase=_["omni"]["mainnet"]["passphrase"],
        language=_["omni"]["mainnet"]["language"]
    ).from_path(
        path=_["omni"]["mainnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["omni"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["omni"]["mainnet"]["symbol"] == OMNI
    assert hdwallet.network() == _["omni"]["mainnet"]["network"]
    assert hdwallet.strength() == _["omni"]["mainnet"]["strength"]
    assert hdwallet.entropy() == _["omni"]["mainnet"]["entropy"]
    assert hdwallet.mnemonic() == _["omni"]["mainnet"]["mnemonic"]
    assert hdwallet.language() == _["omni"]["mainnet"]["language"]
    assert hdwallet.passphrase() == _["omni"]["mainnet"]["passphrase"]
    assert hdwallet.seed() == _["omni"]["mainnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["omni"]["mainnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["omni"]["mainnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["omni"]["mainnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["omni"]["mainnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["omni"]["mainnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["omni"]["mainnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["omni"]["mainnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["omni"]["mainnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["omni"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["omni"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() == _["omni"]["mainnet"]["chain_code"]
    assert hdwallet.private_key() == _["omni"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["omni"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["omni"]["mainnet"]["wif"]
    assert hdwallet.identifier() == _["omni"]["mainnet"]["identifier"]
    assert hdwallet.finger_print() == _["omni"]["mainnet"]["finger_print"]
    assert hdwallet.path() == _["omni"]["mainnet"]["path"]
    assert hdwallet.address() == _["omni"]["mainnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["omni"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps


def test_omni_testnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["omni"]["testnet"]["symbol"]
    )

    hdwallet.from_entropy(
        entropy=_["omni"]["testnet"]["entropy"],
        passphrase=_["omni"]["testnet"]["passphrase"],
        language=_["omni"]["testnet"]["language"]
    ).from_path(
        path=_["omni"]["testnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["omni"]["testnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["omni"]["testnet"]["symbol"] == OMNITEST
    assert hdwallet.network() == _["omni"]["testnet"]["network"]
    assert hdwallet.strength() == _["omni"]["testnet"]["strength"]
    assert hdwallet.entropy() == _["omni"]["testnet"]["entropy"]
    assert hdwallet.mnemonic() == _["omni"]["testnet"]["mnemonic"]
    assert hdwallet.language() == _["omni"]["testnet"]["language"]
    assert hdwallet.passphrase() == _["omni"]["testnet"]["passphrase"]
    assert hdwallet.seed() == _["omni"]["testnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["omni"]["testnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["omni"]["testnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["omni"]["testnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["omni"]["testnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["omni"]["testnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["omni"]["testnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["omni"]["testnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["omni"]["testnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["omni"]["testnet"]["uncompressed"]
    assert hdwallet.compressed() == _["omni"]["testnet"]["compressed"]
    assert hdwallet.chain_code() == _["omni"]["testnet"]["chain_code"]
    assert hdwallet.private_key() == _["omni"]["testnet"]["private_key"]
    assert hdwallet.public_key() == _["omni"]["testnet"]["public_key"]
    assert hdwallet.wif() == _["omni"]["testnet"]["wif"]
    assert hdwallet.identifier() == _["omni"]["testnet"]["identifier"]
    assert hdwallet.finger_print() == _["omni"]["testnet"]["finger_print"]
    assert hdwallet.path() == _["omni"]["testnet"]["path"]
    assert hdwallet.address() == _["omni"]["testnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["omni"]["testnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
