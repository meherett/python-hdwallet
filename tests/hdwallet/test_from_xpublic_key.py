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


def test_from_xpublic_key():

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )
    hdwallet.from_xpublic_key(
        xpublic_key=_["bitcoin"]["mainnet"]["root_xpublic_key"], strict=True
    )
    hdwallet.from_path(
        path="m/44/0/0/0/0"
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
    assert hdwallet.root_xpublic_key(encoded=False) == "0488b21e000000000000000000ad41ef910cdcae932cb4060777b4284ee38f5b29c5fb60fda8416f298a14702c02949b9f64223e124eb9a8383fba0b21b5845fcfbdc84dec7692d21c716410eab0"
    assert hdwallet.root_xpublic_key() == "xpub661MyMwAqRbcGGUtsoFw2d6ARvD2ABd7z327zxt2XiBBwMx9GAuNrrE7tbRuWF5MjjZ1BzDsRdaSHc9nVKAgHzQrv6pwYW3Hd7LSzbh8sWS"
    assert hdwallet.xprivate_key(encoded=False) is None
    assert hdwallet.xprivate_key() is None
    assert hdwallet.xpublic_key(encoded=False) == "0488b21e052c0269af000000006c95c19e932b9e8f3d834e874526768ca1b3d89933ad71fd8253bcca67ac283d038f24175db513b40c75503c25040e5f0ea4d38e912d1f83daf5fd8c4b9512ad87"
    assert hdwallet.xpublic_key() == "xpub6FjoSaU1JaG6fC6wTYmb1mJzaZxSunxASN7nTRHhFynh33gKRfmmNrtQ82s8YouLCrEniskjumfACiiTyVmi4aXyLL8HvLdZc8mjKsbzT9z"
    assert hdwallet.uncompressed() == "8f24175db513b40c75503c25040e5f0ea4d38e912d1f83daf5fd8c4b9512ad8750a64d9e0ee3555225e4130c7e36a443ec20330bf0be1e4de913e31e00202993"
    assert hdwallet.compressed() == "038f24175db513b40c75503c25040e5f0ea4d38e912d1f83daf5fd8c4b9512ad87"
    assert hdwallet.chain_code() == "6c95c19e932b9e8f3d834e874526768ca1b3d89933ad71fd8253bcca67ac283d"
    assert hdwallet.private_key() is None
    assert hdwallet.public_key() == "038f24175db513b40c75503c25040e5f0ea4d38e912d1f83daf5fd8c4b9512ad87"
    assert hdwallet.wif() is None
    assert hdwallet.finger_print() == "4e749a26"
    assert hdwallet.semantic() == "p2pkh"
    assert hdwallet.path() == "m/44/0/0/0/0"
    assert hdwallet.hash() == "4e749a26934bca5091a05ee6f55e7d0e21482647"
    assert hdwallet.p2pkh_address() == "189qPd6J81ns9LEGx6kun7Xtg1bJV8GJXh"
    assert hdwallet.p2sh_address() == "3C71bNRojv3Gc7zHvWygas4AFt34rKezcF"
    assert hdwallet.p2wpkh_address() == "bc1qfe6f5f5nf099pydqtmn02hnapcs5sfj86dpqjm"
    assert hdwallet.p2wpkh_in_p2sh_address() == "3NykoodgJ7Li43JPt5xsezQz8xfwwwFZUs"
    assert hdwallet.p2wsh_address() == "bc1qazm6kznlgs06exh4cq2qxh567xrffppwujje5zg84upnng4essusd08nhz"
    assert hdwallet.p2wsh_in_p2sh_address() == "32yGj8ncXBBTjXqg188ZHxd1xffoQDcjin"

    assert isinstance(hdwallet.dumps(), dict)

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin"]["testnet"]["symbol"]
    )

    hdwallet.from_xpublic_key(
        xpublic_key=_["bitcoin"]["testnet"]["xpublic_key"], strict=False
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
    assert hdwallet.root_xpublic_key(encoded=False) == _["bitcoin"]["testnet"]["xpublic_key_hex"]
    assert hdwallet.root_xpublic_key() == _["bitcoin"]["testnet"]["xpublic_key"]
    assert hdwallet.xprivate_key(encoded=False) is None
    assert hdwallet.xprivate_key() is None
    assert hdwallet.xpublic_key(encoded=False) == _["bitcoin"]["testnet"]["xpublic_key_hex"]
    assert hdwallet.xpublic_key() == _["bitcoin"]["testnet"]["xpublic_key"]
    assert hdwallet.uncompressed() == _["bitcoin"]["testnet"]["uncompressed"]
    assert hdwallet.uncompressed(compressed=_["bitcoin"]["testnet"]["compressed"]) == _["bitcoin"]["testnet"]["uncompressed"]
    assert hdwallet.compressed() == _["bitcoin"]["testnet"]["compressed"]
    assert hdwallet.compressed(uncompressed=_["bitcoin"]["testnet"]["uncompressed"]) == _["bitcoin"]["testnet"]["compressed"]
    assert hdwallet.chain_code() == _["bitcoin"]["testnet"]["chain_code"]
    assert hdwallet.private_key() is None
    assert hdwallet.public_key() == _["bitcoin"]["testnet"]["public_key"]
    assert hdwallet.wif() is None
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
    dumps["root_xprivate_key"] = None
    dumps["xprivate_key"] = None
    dumps["private_key"] = None
    dumps["wif"] = None
    dumps["path"] = None
    dumps["root_xpublic_key"] = _["bitcoin"]["testnet"]["xpublic_key"]
    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    assert hdwallet.dumps() == dumps
