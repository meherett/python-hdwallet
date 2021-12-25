#!/usr/bin/env python3

import pytest

from hdwallet.cryptocurrencies import BitcoinMainnet
from hdwallet.derivations import (
    Derivation, BIP32Derivation, BIP44Derivation, BIP49Derivation, BIP84Derivation, BIP141Derivation
)
from hdwallet.exceptions import SemanticError


def test_derivations():

    assert str(
        Derivation(path="m/44'/0'/0'/0/0", semantic="p2pkh")
    ) == "m/44'/0'/0'/0/0"
    assert str(
        Derivation(semantic="p2pkh").from_path(
            path="m/44'/0'/0'/0/0"
        )
    ) == "m/44'/0'/0'/0/0"
    assert str(
        Derivation(semantic="p2pkh").from_index(
            index=44, hardened=True
        ).from_index(
            index=0, hardened=True
        ).from_index(
            index=0, hardened=True
        ).from_index(
            index=0, hardened=False
        ).from_index(
            index=0, hardened=False
        )
    ) == "m/44'/0'/0'/0/0"
    assert str(
        Derivation(path="m/44'/0'/0'/0/0", semantic="p2pkh").clean_derivation()
    ) == "\0\0\0\0"

    assert str(
        BIP32Derivation(purpose=44, coin_type=0, account=0, change=False, address=0)
    ) == "m/44'/0'/0'/0/0"
    assert str(
        BIP32Derivation(purpose=(44, False), coin_type=(0, False), account=0, change=False, address=0)
    ) == "m/44/0/0'/0/0"

    bip32_derivation: BIP32Derivation = BIP32Derivation().from_purpose(
        purpose=44, hardened=True
    ).from_coin_type(
        coin_type=0, hardened=True
    ).from_account(
        account=0, hardened=True
    ).from_change(
        change=False
    ).from_address(
        address=0, hardened=False
    )
    assert str(bip32_derivation) == "m/44'/0'/0'/0/0"
    assert bip32_derivation.purpose() == "44'"
    assert bip32_derivation.coin_type() == "0'"
    assert bip32_derivation.account() == "0'"
    assert bip32_derivation.change() == 0
    assert bip32_derivation.address() == "0"
    assert bip32_derivation.SEMANTIC == "p2pkh"

    bip32_derivation: BIP32Derivation = BIP32Derivation(
        purpose=(44, True), coin_type=(0, True), account=(0, True), change=False, address=(0, False)
    )
    assert str(bip32_derivation) == "m/44'/0'/0'/0/0"
    assert bip32_derivation.purpose() == "44'"
    assert bip32_derivation.coin_type() == "0'"
    assert bip32_derivation.account() == "0'"
    assert bip32_derivation.change() == 0
    assert bip32_derivation.address() == "0"
    assert bip32_derivation.SEMANTIC == "p2pkh"

    bip44_derivation: BIP44Derivation = BIP44Derivation(
        cryptocurrency=BitcoinMainnet
    ).from_account(
        account=0, hardened=True
    ).from_change(
        change=False
    ).from_address(
        address=0, hardened=False
    )
    assert str(bip44_derivation) == "m/44'/0'/0'/0/0"
    assert bip44_derivation.purpose() == "44'"
    assert bip44_derivation.coin_type() == "0'"
    assert bip44_derivation.account() == "0'"
    assert bip44_derivation.change() == 0
    assert bip44_derivation.address() == "0"
    assert bip44_derivation.SEMANTIC == "p2pkh"

    bip44_derivation: BIP44Derivation = BIP44Derivation(
        cryptocurrency=BitcoinMainnet, account=(0, True), change=False, address=(0, False)
    )
    assert str(bip44_derivation) == "m/44'/0'/0'/0/0"
    assert bip44_derivation.purpose() == "44'"
    assert bip44_derivation.coin_type() == "0'"
    assert bip44_derivation.account() == "0'"
    assert bip44_derivation.change() == 0
    assert bip44_derivation.address() == "0"
    assert bip44_derivation.SEMANTIC == "p2pkh"

    bip49_derivation: BIP49Derivation = BIP49Derivation(
        cryptocurrency=BitcoinMainnet
    ).from_account(
        account=0, hardened=True
    ).from_change(
        change=False
    ).from_address(
        address=0, hardened=False
    )
    assert str(bip49_derivation) == "m/49'/0'/0'/0/0"
    assert bip49_derivation.purpose() == "49'"
    assert bip49_derivation.coin_type() == "0'"
    assert bip49_derivation.account() == "0'"
    assert bip49_derivation.change() == 0
    assert bip49_derivation.address() == "0"
    assert bip49_derivation.SEMANTIC == "p2wpkh_in_p2sh"

    bip49_derivation: BIP49Derivation = BIP49Derivation(
        cryptocurrency=BitcoinMainnet, account=(0, True), change=False, address=(0, False)
    )
    assert str(bip49_derivation) == "m/49'/0'/0'/0/0"
    assert bip49_derivation.purpose() == "49'"
    assert bip49_derivation.coin_type() == "0'"
    assert bip49_derivation.account() == "0'"
    assert bip49_derivation.change() == 0
    assert bip49_derivation.address() == "0"
    assert bip49_derivation.SEMANTIC == "p2wpkh_in_p2sh"

    bip84_derivation: BIP84Derivation = BIP84Derivation(
        cryptocurrency=BitcoinMainnet
    ).from_account(
        account=0, hardened=True
    ).from_change(
        change=False
    ).from_address(
        address=0, hardened=False
    )
    assert str(bip84_derivation) == "m/84'/0'/0'/0/0"
    assert bip84_derivation.purpose() == "84'"
    assert bip84_derivation.coin_type() == "0'"
    assert bip84_derivation.account() == "0'"
    assert bip84_derivation.change() == 0
    assert bip84_derivation.address() == "0"
    assert bip84_derivation.SEMANTIC == "p2wpkh"

    bip84_derivation: BIP84Derivation = BIP84Derivation(
        cryptocurrency=BitcoinMainnet, account=(0, True), change=False, address=(0, False)
    )
    assert str(bip84_derivation) == "m/84'/0'/0'/0/0"
    assert bip84_derivation.purpose() == "84'"
    assert bip84_derivation.coin_type() == "0'"
    assert bip84_derivation.account() == "0'"
    assert bip84_derivation.change() == 0
    assert bip84_derivation.address() == "0"
    assert bip84_derivation.SEMANTIC == "p2wpkh"

    bip141_derivation: BIP141Derivation = BIP141Derivation(
        cryptocurrency=BitcoinMainnet, semantic="p2wsh_in_p2sh"
    )
    assert str(bip141_derivation) == "m/44'/0'/0'/0/0"
    assert bip141_derivation.SEMANTIC == "p2wsh_in_p2sh"

    with pytest.raises(SemanticError, match="Wrong extended semantic, choose only the following options 'p2wpkh', 'p2wpkh_in_p2sh', 'p2wsh' or 'p2wsh_in_p2sh' semantics."):
        BIP141Derivation(
            cryptocurrency=BitcoinMainnet, semantic="p2pkh"
        )
