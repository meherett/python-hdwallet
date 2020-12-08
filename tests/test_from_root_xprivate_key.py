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


def test_from_root_xprivate_key():

    hdwallet: HDWallet = HDWallet(
        symbol=_["dogecoin"]["mainnet"]["symbol"]
    )
    
    hdwallet.from_root_xprivate_key(
        root_xprivate_key=_["dogecoin"]["mainnet"]["root_xprivate_key"]
    ).from_path(
        path=_["dogecoin"]["mainnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["dogecoin"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["dogecoin"]["mainnet"]["symbol"]
    assert hdwallet.network() == _["dogecoin"]["mainnet"]["network"]
    assert hdwallet.strength() is None
    assert hdwallet.entropy() is None
    assert hdwallet.mnemonic() is None
    assert hdwallet.language() is None
    assert hdwallet.passphrase() is None
    assert hdwallet.seed() is None
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

    dumps["strength"] = None
    dumps["entropy"] = None
    dumps["mnemonic"] = None
    dumps["language"] = None
    dumps["passphrase"] = None
    dumps["seed"] = None
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
