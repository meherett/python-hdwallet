#!/usr/bin/env python3

from hdwallet.hdwallet import HDWallet
from hdwallet.symbols import ETH

import pytest


__ = [
    "Ethereum Mainnet",
    "ETH",
    "50f002376c81c96e430b48f1fe71df57",
    "éluder incendie libre sécréter beurre persil amovible fleur tuteur unique gyrostat ouragan",
    "french",
    None,
    "13b7ca020ebef980ef82b0a6781b8ea1d7fd06f36a18f245f75028c3e8d57b1c3e9645d33f54b9da94b8e364b248d0baeb8d8f84055f4cd92a76de45e2ddb926",
    "xprv9s21ZrQH143K2RiaPFYikhd24P4oUCsbyLb73ZEuEFQUmzLCZmgxS6AGGRRtBG85FVN2LtFcQw9gpvEBKhJUZ69XEM4B8T4YLu3ibprrVct",
    "0488ade400000000000000000024fdb2ae59622189865974b5fd71f7228e6211d30eb0f99b4c0ba09c2aef7d2500698d8ad7df120e990a12bcfef5964d9aedd3da6510e0e844afe49f91c1eeedbc",
    "xpub661MyMwAqRbcEuo3VH5j7qZkcQuHsfbTLZWhqweWnawTenfM7K1CytUk7hZRjwJXRWPbXCmbu7BbNNsjZhQDTsAQLbFR4xGAtLxSDsYMBKz",
    "0488b21e00000000000000000024fdb2ae59622189865974b5fd71f7228e6211d30eb0f99b4c0ba09c2aef7d2502fa5e590bb3ed4bf8f2131c40c197fead5b65f636dedba84566e12209129aaafa",
    "xprvA3YBYJQAwK1RxevG9biFSyXvfFM8cBwe5FgBBBjxAiXkKQ916mAUrcwP1yA7c8xPy7YcLwCcotgoNNZBpfoyFK3TZPYNWXP5mBFw3Tvaz86",
    "0488ade405974908b600000000deb4dd2ce6dbd56d02f4777a7420c7707b742dc9f4fee4513e9546e7b6440053005828a436fd1e75fa9361e992cae5a00649c06fbbc4332e7bff5d6b778745db5b",
    "xpub6GXXwow4mgZjB8zjFdFFp7UfDHBd1efVSUbmya9Zj44jCCU9eJUjQRFrsGJQEKt8EYdGgketpUUeSW4n6hc1DxcAsqoAwDM9prsJmU1VTdi",
    "0488b21e05974908b600000000deb4dd2ce6dbd56d02f4777a7420c7707b742dc9f4fee4513e9546e7b6440053036e5b33eb081f2effde60552fc62849c9252425ad801116333030f4388ef688a9",
    "6e5b33eb081f2effde60552fc62849c9252425ad801116333030f4388ef688a9ac64685881a5dc5688136e5046f313f98d11a250e63e3ffd2d09345199b013d7",
    "036e5b33eb081f2effde60552fc62849c9252425ad801116333030f4388ef688a9",
    "deb4dd2ce6dbd56d02f4777a7420c7707b742dc9f4fee4513e9546e7b6440053",
    "5828a436fd1e75fa9361e992cae5a00649c06fbbc4332e7bff5d6b778745db5b",
    "036e5b33eb081f2effde60552fc62849c9252425ad801116333030f4388ef688a9",
    "KzB5bKAXGXNfcVfv2nvjNbMFjEG1tWcqFzMJaTWkGR17K1xxSFHf",
    "9540976495967d747ff2b7283a3889f2a233f211",
    "95409764",
    "m/44'/60'/0'/0/0",
    "0x67b354C27f16Cfe6E96a5De8454655bD6AFf0a0B"
]


def test_from_entropy():

    hdwallet = HDWallet(symbol=ETH)
    
    hdwallet.from_entropy(entropy=__[2], passphrase=__[5], language=__[4])

    hdwallet.from_path(path=__[23])

    assert hdwallet.cryptocurrency() == __[0]
    assert hdwallet.symbol() == __[1]
    assert hdwallet.entropy() == __[2]
    assert hdwallet.mnemonic() == __[3]
    assert hdwallet.language() == __[4]
    assert hdwallet.passphrase() == __[5]
    assert hdwallet.seed() == __[6]
    assert hdwallet.root_xprivate_key() == __[7]
    assert hdwallet.root_xprivate_key(encoded=False) == __[8]
    assert hdwallet.root_xpublic_key() == __[9]
    assert hdwallet.root_xpublic_key(encoded=False) == __[10]
    assert hdwallet.xprivate_key() == __[11]
    assert hdwallet.xprivate_key(encoded=False) == __[12]
    assert hdwallet.xpublic_key() == __[13]
    assert hdwallet.xpublic_key(encoded=False) == __[14]
    assert hdwallet.uncompressed() == __[15]
    assert hdwallet.compressed() == __[16]
    assert hdwallet.chain_code() == __[17]
    assert hdwallet.private_key() == __[18]
    assert hdwallet.public_key() == __[19]
    assert hdwallet.wif() == __[20]
    assert hdwallet.identifier() == __[21]
    assert hdwallet.finger_print() == __[22]
    assert hdwallet.path() == __[23]
    assert hdwallet.address() == __[24]
    assert hdwallet.dumps() == {
        "cryptocurrency": __[0],
        "symbol": __[1],
        "entropy": __[2],
        "mnemonic": __[3],
        "language": __[4],
        "passphrase": __[5],
        "seed": __[6],
        "root_xprivate_key": __[7],
        "root_xpublic_key": __[9],
        "xprivate_key": __[11],
        "xpublic_key": __[13],
        "uncompressed": __[15],
        "compressed": __[16],
        "chain_code": __[17],
        "private_key": __[18],
        "public_key": __[19],
        "wif": __[20],
        "identifier": __[21],
        "finger_print": __[22],
        "path": __[23],
        "address": __[24]
    }

    with pytest.raises(ValueError, match=r"Invalid language value, .*"):
        hdwallet.from_entropy(entropy=__[2], passphrase=__[5], language="amharic")
