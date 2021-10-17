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


def test_from_entropy():

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )
    
    hdwallet.from_entropy(
        entropy=_["bitcoin"]["mainnet"]["entropy"],
        passphrase=_["bitcoin"]["mainnet"]["passphrase"],
        language=_["bitcoin"]["mainnet"]["language"]
    )

    hdwallet.from_path(
        path=_["bitcoin"]["mainnet"]["path"]
    )

    assert hdwallet.cryptocurrency() == _["bitcoin"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["bitcoin"]["mainnet"]["symbol"]
    assert hdwallet.network() == _["bitcoin"]["mainnet"]["network"]
    assert hdwallet.strength() == _["bitcoin"]["testnet"]["strength"]
    assert hdwallet.entropy() == _["bitcoin"]["mainnet"]["entropy"]
    assert hdwallet.mnemonic() == _["bitcoin"]["mainnet"]["mnemonic"]
    assert hdwallet.language() == _["bitcoin"]["mainnet"]["language"]
    assert hdwallet.passphrase() == _["bitcoin"]["mainnet"]["passphrase"]
    assert hdwallet.seed() == _["bitcoin"]["mainnet"]["seed"]
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

    hdwallet.clean_derivation()

    hdwallet.from_index(44, hardened=True)
    hdwallet.from_index(0, hardened=True)
    hdwallet.from_index(0, hardened=True)
    hdwallet.from_index(0, hardened=False)
    hdwallet.from_index(0, hardened=False)

    assert hdwallet.cryptocurrency() == _["bitcoin"]["mainnet"]["cryptocurrency"]
    assert hdwallet.symbol() == _["bitcoin"]["mainnet"]["symbol"]
    assert hdwallet.network() == _["bitcoin"]["mainnet"]["network"]
    assert hdwallet.strength() == _["bitcoin"]["testnet"]["strength"]
    assert hdwallet.entropy() == _["bitcoin"]["mainnet"]["entropy"]
    assert hdwallet.mnemonic() == _["bitcoin"]["mainnet"]["mnemonic"]
    assert hdwallet.language() == _["bitcoin"]["mainnet"]["language"]
    assert hdwallet.passphrase() == _["bitcoin"]["mainnet"]["passphrase"]
    assert hdwallet.seed() == _["bitcoin"]["mainnet"]["seed"]
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

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
