#!/usr/bin/env python

from typing import Optional

import json

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


def generate_hdwallet(
    symbol: str,
    strength: Optional[int],
    entropy: Optional[str],
    mnemonic: Optional[str],
    language: Optional[str],
    passphrase: Optional[str],
    seed: Optional[str],
    xprivate_key: Optional[str],
    xpublic_key: Optional[str],
    strict: Optional[bool],
    account: int,
    change: bool,
    address: int,
    path: Optional[str],
    private_key: Optional[str],
    public_key: Optional[str],
    wif: Optional[str],
    semantic: str
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
        elif private_key:
            hdwallet.from_private_key(
                private_key=private_key
            )
        elif public_key:
            hdwallet.from_public_key(
                public_key=public_key
            )
        elif wif:
            hdwallet.from_wif(
                wif=wif
            )
        else:
            mnemonic = generate_mnemonic(language=language, strength=strength)
            hdwallet.from_mnemonic(
                mnemonic=mnemonic, language=language, passphrase=passphrase
            )

        if wif or private_key or public_key:
            pass
        else:
            if path:
                derivation: Derivation = Derivation(path=path)
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
                    address=address
                )
                hdwallet.from_path(path=bip32_derivation)

        click.echo(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

    except Exception as exception:
        click.echo(click.style(f"Error: {str(exception)}"), err=True)
        sys.exit()
