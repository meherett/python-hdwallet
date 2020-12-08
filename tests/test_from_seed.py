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


def test_from_seed():

    hdwallet: HDWallet = HDWallet(
        symbol=_["dash"]["testnet"]["symbol"]
    )
    
    hdwallet.from_seed(
        seed=_["dash"]["testnet"]["seed"]
    ).from_path(
        path=_["dash"]["testnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["dash"]["testnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["dash"]["testnet"]["symbol"]
    assert hdwallet.network() == _["dash"]["testnet"]["network"]
    assert hdwallet.strength() is None
    assert hdwallet.entropy() is None
    assert hdwallet.mnemonic() is None
    assert hdwallet.language() is None
    assert hdwallet.passphrase() is None
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

    dumps["strength"] = None
    dumps["entropy"] = None
    dumps["mnemonic"] = None
    dumps["language"] = None
    dumps["passphrase"] = None
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
