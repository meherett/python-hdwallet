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


def test_from_xprivate_key():

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )
    hdwallet.from_xprivate_key(
        xprivate_key=_["bitcoin"]["mainnet"]["root_xprivate_key"], strict=True
    )
    hdwallet.from_path(
        path=_["bitcoin"]["mainnet"]["path"]
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
    assert hdwallet.root_xprivate_key(encoded=False) == _["bitcoin"]["mainnet"]["root_xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["bitcoin"]["mainnet"]["root_xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["bitcoin"]["mainnet"]["root_xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["bitcoin"]["mainnet"]["root_xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["bitcoin"]["mainnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["bitcoin"]["mainnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["bitcoin"]["mainnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["bitcoin"]["mainnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["bitcoin"]["mainnet"]["uncompressed"]
    assert hdwallet.compressed() == _["bitcoin"]["mainnet"]["compressed"]
    assert hdwallet.chain_code() == _["bitcoin"]["mainnet"]["chain_code"]
    assert hdwallet.private_key() == _["bitcoin"]["mainnet"]["private_key"]
    assert hdwallet.public_key() == _["bitcoin"]["mainnet"]["public_key"]
    assert hdwallet.wif() == _["bitcoin"]["mainnet"]["wif"]
    assert hdwallet.finger_print() == _["bitcoin"]["mainnet"]["finger_print"]
    assert hdwallet.semantic() == _["bitcoin"]["mainnet"]["semantic"]
    assert hdwallet.path() == _["bitcoin"]["mainnet"]["path"]
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
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin"]["testnet"]["symbol"]
    )

    hdwallet.from_xprivate_key(
        xprivate_key=_["bitcoin"]["testnet"]["xprivate_key"], strict=False
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
    assert hdwallet.root_xprivate_key(encoded=False) == _["bitcoin"]["testnet"]["xprivate_key_hex"]
    assert hdwallet.root_xprivate_key() == _["bitcoin"]["testnet"]["xprivate_key"]
    assert hdwallet.root_xpublic_key(encoded=False) == _["bitcoin"]["testnet"]["xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["bitcoin"]["testnet"]["xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) == _["bitcoin"]["testnet"]["xprivate_key_hex"]
    assert hdwallet.xprivate_key() == _["bitcoin"]["testnet"]["xprivate_key"]
    assert hdwallet.xpublic_key(encoded=False) == _["bitcoin"]["testnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["bitcoin"]["testnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["bitcoin"]["testnet"]["uncompressed"]
    assert hdwallet.compressed() == _["bitcoin"]["testnet"]["compressed"]
    assert hdwallet.chain_code() == _["bitcoin"]["testnet"]["chain_code"]
    assert hdwallet.private_key() == _["bitcoin"]["testnet"]["private_key"]
    assert hdwallet.public_key() == _["bitcoin"]["testnet"]["public_key"]
    assert hdwallet.wif() == _["bitcoin"]["testnet"]["wif"]
    assert hdwallet.finger_print() == _["bitcoin"]["testnet"]["finger_print"]
    assert hdwallet.semantic() == _["bitcoin"]["testnet"]["semantic"]
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
    dumps["path"] = None
    dumps["root_xprivate_key"] = _["bitcoin"]["testnet"]["xprivate_key"]
    dumps["root_xpublic_key"] = _["bitcoin"]["testnet"]["xpublic_key"]
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
