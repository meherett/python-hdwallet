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


def test_from_public_key():

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin"]["testnet"]["symbol"]
    )
    
    hdwallet.from_public_key(
        public_key=_["bitcoin"]["testnet"]["public_key"]
    )

    assert hdwallet.cryptocurrency() == _["bitcoin"]["testnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["bitcoin"]["testnet"]["symbol"]
    assert hdwallet.network() == _["bitcoin"]["testnet"]["network"]
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
    assert hdwallet.uncompressed() == _["bitcoin"]["testnet"]["uncompressed"]
    assert hdwallet.compressed() == _["bitcoin"]["testnet"]["compressed"]
    assert hdwallet.chain_code() is None
    assert hdwallet.private_key() is None
    assert hdwallet.public_key(compressed=True) == _["bitcoin"]["testnet"]["public_key"]
    assert hdwallet.public_key(compressed=True, private_key=_["bitcoin"]["testnet"]["private_key"]) == _["bitcoin"]["testnet"]["public_key"]
    assert hdwallet.public_key(compressed=False) == _["bitcoin"]["testnet"]["uncompressed"]
    assert hdwallet.public_key(compressed=False, private_key=_["bitcoin"]["testnet"]["private_key"]) == _["bitcoin"]["testnet"]["uncompressed"]
    assert hdwallet.wif() is None
    assert hdwallet.finger_print() == _["bitcoin"]["testnet"]["finger_print"]
    assert hdwallet.semantic() is None
    assert hdwallet.path() == None
    assert hdwallet.hash() == _["bitcoin"]["testnet"]["hash"]
    assert hdwallet.p2pkh_address() == _["bitcoin"]["testnet"]["addresses"]["p2pkh"]
    assert hdwallet.p2sh_address() == _["bitcoin"]["testnet"]["addresses"]["p2sh"]
    assert hdwallet.p2wpkh_address() == _["bitcoin"]["testnet"]["addresses"]["p2wpkh"]
    assert hdwallet.p2wpkh_in_p2sh_address() == _["bitcoin"]["testnet"]["addresses"]["p2wpkh_in_p2sh"]
    assert hdwallet.p2wsh_address() == _["bitcoin"]["testnet"]["addresses"]["p2wsh"]
    assert hdwallet.p2wsh_in_p2sh_address() == _["bitcoin"]["testnet"]["addresses"]["p2wsh_in_p2sh"]

    assert isinstance(hdwallet.dumps(), dict)

    dumps: dict = _["bitcoin"]["testnet"]

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
    dumps["private_key"] = None
    dumps["wif"] = None
    dumps["path"] = None
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
