#!/usr/bin/env python3

import json
import os

from hdwallet import HDWallet
from hdwallet.symbols import BTG

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_bitcoin_gold_mainnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin_gold"]["mainnet"]["symbol"]
    )

    hdwallet.from_entropy(
        entropy=_["bitcoin_gold"]["mainnet"]["entropy"],
        passphrase=_["bitcoin_gold"]["mainnet"]["passphrase"],
        language=_["bitcoin_gold"]["mainnet"]["language"]
    ).from_path(
        path=_["bitcoin_gold"]["mainnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["bitcoin_gold"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["bitcoin_gold"]["mainnet"]["symbol"] == BTG
    assert hdwallet.network() == _["bitcoin_gold"]["mainnet"]["network"]
    assert hdwallet.strength() == _["bitcoin_gold"]["mainnet"]["strength"]
    assert hdwallet.entropy() == _["bitcoin_gold"]["mainnet"]["entropy"]
    assert hdwallet.mnemonic() == _["bitcoin_gold"]["mainnet"]["mnemonic"]
    assert hdwallet.language() == _["bitcoin_gold"]["mainnet"]["language"]
    assert hdwallet.passphrase() == _["bitcoin_gold"]["mainnet"]["passphrase"]
    assert hdwallet.seed() == _["bitcoin_gold"]["mainnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["bitcoin_gold"]["mainnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["bitcoin_gold"]["mainnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["bitcoin_gold"]["mainnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["bitcoin_gold"]["mainnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["bitcoin_gold"]["mainnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["bitcoin_gold"]["mainnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["bitcoin_gold"]["mainnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["bitcoin_gold"]["mainnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["bitcoin_gold"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["bitcoin_gold"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() == _["bitcoin_gold"]["mainnet"]["chain_code"]
    assert hdwallet.private_key() == _["bitcoin_gold"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["bitcoin_gold"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["bitcoin_gold"]["mainnet"]["wif"]
    assert hdwallet.identifier() == _["bitcoin_gold"]["mainnet"]["identifier"]
    assert hdwallet.finger_print() == _["bitcoin_gold"]["mainnet"]["finger_print"]
    assert hdwallet.path() == _["bitcoin_gold"]["mainnet"]["path"]
    assert hdwallet.address() == _["bitcoin_gold"]["mainnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["bitcoin_gold"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
