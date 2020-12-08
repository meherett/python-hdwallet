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


def test_from_wallet_important_format():

    hdwallet: HDWallet = HDWallet(
        symbol=_["litecoin"]["mainnet"]["symbol"]
    )
    
    hdwallet.from_wif(
        wif=_["litecoin"]["mainnet"]["wif"]
    )

    assert hdwallet.cryptocurrency() == _["litecoin"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["litecoin"]["mainnet"]["symbol"]
    assert hdwallet.network() == _["litecoin"]["mainnet"]["network"]
    assert hdwallet.strength() is None
    assert hdwallet.entropy() is None
    assert hdwallet.mnemonic() is None
    assert hdwallet.language() is None
    assert hdwallet.passphrase() is None
    assert hdwallet.seed() is None
    assert hdwallet.root_xprivate_key(encoded=False) is None
    assert hdwallet.root_xprivate_key() is None
    assert hdwallet.root_xpublic_key(encoded=False) is None
    assert hdwallet.root_xpublic_key() is None
    assert hdwallet.xprivate_key(encoded=False) is None
    assert hdwallet.xprivate_key() is None
    assert hdwallet.xpublic_key(encoded=False) is None
    assert hdwallet.xpublic_key() is None
    assert hdwallet.uncompressed() == _["litecoin"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["litecoin"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() is None
    assert hdwallet.private_key() == _["litecoin"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["litecoin"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["litecoin"]["mainnet"]["wif"]
    assert hdwallet.identifier() == _["litecoin"]["mainnet"]["identifier"]
    assert hdwallet.finger_print() == _["litecoin"]["mainnet"]["finger_print"]
    assert hdwallet.path() is None
    assert hdwallet.address() == _["litecoin"]["mainnet"]["address"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["litecoin"]["mainnet"]

    dumps["strength"] = None
    dumps["entropy"] = None
    dumps["mnemonic"] = None
    dumps["language"] = None
    dumps["passphrase"] = None
    dumps["seed"] = None
    dumps["root_xprivate_key"] = None
    dumps["root_xpublic_key"] = None
    dumps["xprivate_key"] = None
    dumps["xpublic_key"] = None
    dumps["chain_code"] = None
    dumps["path"] = None
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
