#!/usr/bin/env python

from typing import Optional

from hdwallet import HDWallet
from hdwallet.derivations import (
    Derivation, BIP32Derivation
)
from hdwallet.cryptocurrencies import (
    Cryptocurrency, get_cryptocurrency
)
from hdwallet.utils import generate_mnemonic
from hdwallet.cli import (
    click, sys
)


def generate_addresses(
    symbol: str,
    strength: int,
    entropy: Optional[str],
    mnemonic: Optional[str],
    language: Optional[str],
    passphrase: Optional[str],
    seed: Optional[str],
    xprivate_key: Optional[str],
    xpublic_key: Optional[str],
    strict: bool,
    account: int,
    change: bool,
    path: Optional[str],
    semantic: str,
    start_index: int,
    end_index: int,
    hardened: bool,
    show: str
):
    try:
        hdwallet: HDWallet = HDWallet(
            symbol=symbol, semantic=semantic
        )
        if entropy:
            hdwallet.from_entropy(
                entropy=entropy, language=language, passphrase=passphrase
            )
        elif mnemonic:
            hdwallet.from_mnemonic(
                mnemonic=mnemonic, passphrase=passphrase
            )
        elif seed:
            hdwallet.from_seed(
                seed=seed
            )
        elif xprivate_key:
            hdwallet.from_xprivate_key(
                xprivate_key=xprivate_key, strict=strict
            )
        elif xpublic_key:
            hdwallet.from_xpublic_key(
                xpublic_key=xpublic_key, strict=strict
            )
        else:
            mnemonic = generate_mnemonic(language=language, strength=strength)
            hdwallet.from_mnemonic(
                mnemonic=mnemonic, language=language, passphrase=passphrase
            )

        for index in range(start_index, end_index):
            if path:
                derivation: Derivation = Derivation(path=path)
                derivation.from_index(index=index, hardened=hardened)
                hdwallet.from_path(path=derivation)
            else:
                cryptocurrency: Cryptocurrency = get_cryptocurrency(symbol=symbol)
                bip32_derivation: BIP32Derivation = BIP32Derivation(
                    purpose=(
                        44, False if xpublic_key else True
                    ),
                    coin_type=(
                        cryptocurrency.COIN_TYPE.INDEX,
                        False if xpublic_key else cryptocurrency.COIN_TYPE.HARDENED
                    ),
                    account=(
                        account, False if xpublic_key else True
                    ),
                    change=change,
                    address=index
                )
                hdwallet.from_path(path=bip32_derivation)

            rows: str = ""
            dumps = hdwallet.dumps()
            for i, key in enumerate([keys.split(":") for keys in show.split(",")]):
                rows += (
                    f"{dumps[key[0]][key[1]] if len(key) == 2 else dumps[key[0]]}"
                    if i == 0 else
                    f" {dumps[key[0]][key[1]] if len(key) == 2 else dumps[key[0]]}"
                )
            click.echo(rows)

            hdwallet.clean_derivation()

    except TimeoutError as exception:
        click.echo(click.style(f"Error: {str(exception)}"), err=True)
        sys.exit()
