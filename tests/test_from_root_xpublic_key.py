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


def test_from_root_xpublic_key():

    hdwallet: HDWallet = HDWallet(
        symbol=_["bitcoin"]["mainnet"]["symbol"]
    )
    hdwallet.from_root_xpublic_key(
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
