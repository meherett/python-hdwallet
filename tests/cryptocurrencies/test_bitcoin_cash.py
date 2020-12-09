#!/usr/bin/env python3

import json
import os

from hdwallet import HDWallet
from hdwallet.symbols import BCH

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_bitcoin_cash_mainnet():

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin_cash"]["mainnet"]["symbol"]
    )

    hdwallet.from_entropy(
        entropy=_["bitcoin_cash"]["mainnet"]["entropy"],
        passphrase=_["bitcoin_cash"]["mainnet"]["passphrase"],
        language=_["bitcoin_cash"]["mainnet"]["language"]
    ).from_path(
        path=_["bitcoin_cash"]["mainnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["bitcoin_cash"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["bitcoin_cash"]["mainnet"]["symbol"] == BCH
    assert hdwallet.network() == _["bitcoin_cash"]["mainnet"]["network"]
    assert hdwallet.strength() == _["bitcoin_cash"]["mainnet"]["strength"]
    assert hdwallet.entropy() == _["bitcoin_cash"]["mainnet"]["entropy"]
    assert hdwallet.mnemonic() == _["bitcoin_cash"]["mainnet"]["mnemonic"]
    assert hdwallet.language() == _["bitcoin_cash"]["mainnet"]["language"]
    assert hdwallet.passphrase() == _["bitcoin_cash"]["mainnet"]["passphrase"]
    assert hdwallet.seed() == _["bitcoin_cash"]["mainnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["bitcoin_cash"]["mainnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["bitcoin_cash"]["mainnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["bitcoin_cash"]["mainnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["bitcoin_cash"]["mainnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["bitcoin_cash"]["mainnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["bitcoin_cash"]["mainnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["bitcoin_cash"]["mainnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["bitcoin_cash"]["mainnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["bitcoin_cash"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["bitcoin_cash"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() == _["bitcoin_cash"]["mainnet"]["chain_code"]
    assert hdwallet.private_key() == _["bitcoin_cash"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["bitcoin_cash"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["bitcoin_cash"]["mainnet"]["wif"]
    assert hdwallet.identifier() == _["bitcoin_cash"]["mainnet"]["identifier"]
    assert hdwallet.finger_print() == _["bitcoin_cash"]["mainnet"]["finger_print"]
    assert hdwallet.path() == _["bitcoin_cash"]["mainnet"]["path"]
    assert hdwallet.address() == _["bitcoin_cash"]["mainnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["bitcoin_cash"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
