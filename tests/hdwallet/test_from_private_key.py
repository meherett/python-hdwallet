#!/usr/bin/env python3

import json
import os

from hdwallet import HDWallet

# Test Values
base_path: str = os.path.dirname(__file__)
file_path: str = os.path.abspath(os.path.join(base_path, "../values.json"))
values = open(file_path, "r", encoding="utf-8")
_: dict = json.loads(values.read())
values.close()


def test_from_private_key():

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )
    
    hdwallet.from_private_key(
        private_key=_["bitcoin"]["mainnet"]["private_key"]
    )

    assert hdwallet.cryptocurrency() == _["bitcoin"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["bitcoin"]["mainnet"]["symbol"]
    assert hdwallet.network() == _["bitcoin"]["mainnet"]["network"]
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
    assert hdwallet.uncompressed() == _["bitcoin"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["bitcoin"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() is None
    assert hdwallet.private_key() == _["bitcoin"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["bitcoin"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["bitcoin"]["mainnet"]["wif"]
    assert hdwallet.finger_print() == _["bitcoin"]["mainnet"]["finger_print"]
    assert hdwallet.semantic() is None
    assert hdwallet.path() == None
    assert hdwallet.hash() == _["bitcoin"]["mainnet"]["hash"]
    assert hdwallet.p2pkh_address() == _["bitcoin"]["mainnet"]["addresses"]["p2pkh"]
    assert hdwallet.p2sh_address() == _["bitcoin"]["mainnet"]["addresses"]["p2sh"]
    assert hdwallet.p2wpkh_address() == _["bitcoin"]["mainnet"]["addresses"]["p2wpkh"]
    assert hdwallet.p2wpkh_in_p2sh_address() == _["bitcoin"]["mainnet"]["addresses"]["p2wpkh_in_p2sh"]
    assert hdwallet.p2wsh_address() == _["bitcoin"]["mainnet"]["addresses"]["p2wsh"]
    assert hdwallet.p2wsh_in_p2sh_address() == _["bitcoin"]["mainnet"]["addresses"]["p2wsh_in_p2sh"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["bitcoin"]["mainnet"]

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
    dumps["semantic"] = None
    dumps["chain_code"] = None
    dumps["path"] = None
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
