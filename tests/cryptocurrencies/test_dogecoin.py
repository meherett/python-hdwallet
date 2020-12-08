#!/usr/bin/env python3

import json
import os

from hdwallet import HDWallet
from hdwallet.symbols import DOGE, DOGETEST

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_dogecoin_mainnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["dogecoin"]["mainnet"]["symbol"]
    )
    
    hdwallet.from_entropy(
        entropy=_["dogecoin"]["mainnet"]["entropy"],
        passphrase=_["dogecoin"]["mainnet"]["passphrase"],
        language=_["dogecoin"]["mainnet"]["language"]
    ).from_path(
        path=_["dogecoin"]["mainnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["dogecoin"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["dogecoin"]["mainnet"]["symbol"] == DOGE
    assert hdwallet.network() == _["dogecoin"]["mainnet"]["network"]
    assert hdwallet.strength() == _["dogecoin"]["mainnet"]["strength"]
    assert hdwallet.entropy() == _["dogecoin"]["mainnet"]["entropy"]
    assert hdwallet.mnemonic() == _["dogecoin"]["mainnet"]["mnemonic"]
    assert hdwallet.language() == _["dogecoin"]["mainnet"]["language"]
    assert hdwallet.passphrase() == _["dogecoin"]["mainnet"]["passphrase"]
    assert hdwallet.seed() == _["dogecoin"]["mainnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["dogecoin"]["mainnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["dogecoin"]["mainnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["dogecoin"]["mainnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["dogecoin"]["mainnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["dogecoin"]["mainnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["dogecoin"]["mainnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["dogecoin"]["mainnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["dogecoin"]["mainnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["dogecoin"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["dogecoin"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() == _["dogecoin"]["mainnet"]["chain_code"]
    assert hdwallet.private_key() == _["dogecoin"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["dogecoin"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["dogecoin"]["mainnet"]["wif"]
    assert hdwallet.identifier() == _["dogecoin"]["mainnet"]["identifier"]
    assert hdwallet.finger_print() == _["dogecoin"]["mainnet"]["finger_print"]
    assert hdwallet.path() == _["dogecoin"]["mainnet"]["path"]
    assert hdwallet.address() == _["dogecoin"]["mainnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["dogecoin"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps


def test_dogecoin_testnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["dogecoin"]["testnet"]["symbol"]
    )

    hdwallet.from_entropy(
        entropy=_["dogecoin"]["testnet"]["entropy"],
        passphrase=_["dogecoin"]["testnet"]["passphrase"],
        language=_["dogecoin"]["testnet"]["language"]
    ).from_path(
        path=_["dogecoin"]["testnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["dogecoin"]["testnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["dogecoin"]["testnet"]["symbol"] == DOGETEST
    assert hdwallet.network() == _["dogecoin"]["testnet"]["network"]
    assert hdwallet.strength() == _["dogecoin"]["testnet"]["strength"]
    assert hdwallet.entropy() == _["dogecoin"]["testnet"]["entropy"]
    assert hdwallet.mnemonic() == _["dogecoin"]["testnet"]["mnemonic"]
    assert hdwallet.language() == _["dogecoin"]["testnet"]["language"]
    assert hdwallet.passphrase() == _["dogecoin"]["testnet"]["passphrase"]
    assert hdwallet.seed() == _["dogecoin"]["testnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["dogecoin"]["testnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["dogecoin"]["testnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["dogecoin"]["testnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["dogecoin"]["testnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["dogecoin"]["testnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["dogecoin"]["testnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["dogecoin"]["testnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["dogecoin"]["testnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["dogecoin"]["testnet"]["uncompressed"]
    assert hdwallet.compressed() == _["dogecoin"]["testnet"]["compressed"]
    assert hdwallet.chain_code() == _["dogecoin"]["testnet"]["chain_code"]
    assert hdwallet.private_key() == _["dogecoin"]["testnet"]["private_key"]
    assert hdwallet.public_key() == _["dogecoin"]["testnet"]["public_key"]
    assert hdwallet.wif() == _["dogecoin"]["testnet"]["wif"]
    assert hdwallet.identifier() == _["dogecoin"]["testnet"]["identifier"]
    assert hdwallet.finger_print() == _["dogecoin"]["testnet"]["finger_print"]
    assert hdwallet.path() == _["dogecoin"]["testnet"]["path"]
    assert hdwallet.address() == _["dogecoin"]["testnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["dogecoin"]["testnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
