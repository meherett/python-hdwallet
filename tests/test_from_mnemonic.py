#!/usr/bin/env python3

import json
import os

from hdwallet import HDWallet

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_from_mnemonic():

    hdwallet: HDWallet = HDWallet(
        symbol=_["qtum"]["mainnet"]["symbol"]
    )
    
    hdwallet.from_mnemonic(
        mnemonic=_["qtum"]["mainnet"]["mnemonic"],
        passphrase=_["qtum"]["mainnet"]["passphrase"],
        language=_["qtum"]["mainnet"]["language"]
    ).from_path(
        path=_["qtum"]["mainnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["qtum"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["qtum"]["mainnet"]["symbol"]
    assert hdwallet.network() == _["qtum"]["mainnet"]["network"]
    assert hdwallet.strength() == _["qtum"]["mainnet"]["strength"]
    assert hdwallet.entropy() == _["qtum"]["mainnet"]["entropy"]
    assert hdwallet.mnemonic() == _["qtum"]["mainnet"]["mnemonic"]
    assert hdwallet.language() == _["qtum"]["mainnet"]["language"]
    assert hdwallet.passphrase() == _["qtum"]["mainnet"]["passphrase"]
    assert hdwallet.seed() == _["qtum"]["mainnet"]["seed"]
    assert hdwallet.root_xprivate_key(encoded=False) == _["qtum"]["mainnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["qtum"]["mainnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["qtum"]["mainnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["qtum"]["mainnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["qtum"]["mainnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["qtum"]["mainnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["qtum"]["mainnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["qtum"]["mainnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["qtum"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["qtum"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() == _["qtum"]["mainnet"]["chain_code"]
    assert hdwallet.private_key() == _["qtum"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["qtum"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["qtum"]["mainnet"]["wif"]
    assert hdwallet.identifier() == _["qtum"]["mainnet"]["identifier"]
    assert hdwallet.finger_print() == _["qtum"]["mainnet"]["finger_print"]
    assert hdwallet.path() == _["qtum"]["mainnet"]["path"]
    assert hdwallet.address() == _["qtum"]["mainnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["qtum"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
