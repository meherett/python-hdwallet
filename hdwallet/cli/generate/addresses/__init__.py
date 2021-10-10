#!/usr/bin/env python

from typing import Optional

from hdwallet.cli.generate.addresses.addresses import generate_hdwallet_addresses
from hdwallet.cli import click


@click.command("addresses", options_metavar="[OPTIONS]",
               short_help="Select Addresses for generation HDWallet addresses.")
@click.option("-s", "--symbol", type=str, required=True,
              help="Set Cryptocurrency ticker symbol.")
@click.option("-sg", "--strength", type=int, default=128,
              help="Set Strength for entropy, choose strength 128, 160, 192, 224 or 256 only.", show_default=True)
@click.option("-e", "--entropy", type=str, default=None,
              help="Set Master key from entropy hex string.", show_default=True)
@click.option("-m", "--mnemonic", type=str, default=None,
              help="Set Master key from mnemonic words.", show_default=True)
@click.option("-l", "--language", type=str, default="english",
              help="Set Language for mnemonic, choose language english, french, italian, spanish, "
                   "chinese_simplified, chinese_traditional, japanese or korean only.", show_default=True)
@click.option("-pa", "--passphrase", type=str, default=None,
              help="Set Passphrase for mnemonic.", show_default=True)
@click.option("-sd", "--seed", type=str, default=None,
              help="Set Master key from seed hex string.", show_default=True)
@click.option("-xprv", "--xprivate-key", type=str, default=None,
              help="Set Master key from xprivate key.", show_default=True)
@click.option("-xpub", "--xpublic-key", type=str, default=None,
              help="Set Master key from xpublic key.", show_default=True)
@click.option("-st", "--strict", type=bool, default=False,
              help="Set Strict for root keys.", show_default=True)
@click.option("-ac", "--account", type=int, default=0,
              help="Set derivation from account.", show_default=True)
@click.option("-ch", "--change", type=bool, default=False,
              help="Set Derivation from change.", show_default=True)
@click.option("-p", "--path", type=str, default=None,
              help="Set Master key derivation path.", show_default=True)
@click.option("-se", "--semantic", type=str, default="p2pkh",
              help="Set Semantic for xprivate and xpublic keys.", show_default=True)
@click.option("-h", "--hardened", type=bool, default=False,
              help="Set Hardened for addresses.", show_default=True)
@click.option("-si", "--start-index", type=int, default=0,
              help="Set Start from address index.", show_default=True)
@click.option("-ei", "--end-index", type=int, default=20,
              help="Set End to address index.", show_default=True)
@click.option("-sh", "--show", type=str, default="path,addresses:p2pkh,public_key,wif",
              help="Set Value key of generated HDWallet data to show.", show_default=True)
def addresses(
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
    return generate_hdwallet_addresses(
        symbol=symbol,
        strength=strength,
        entropy=entropy,
        mnemonic=mnemonic,
        language=language,
        passphrase=passphrase,
        seed=seed,
        xprivate_key=xprivate_key,
        xpublic_key=xpublic_key,
        strict=strict,
        account=account,
        change=change,
        path=path,
        semantic=semantic,
        start_index=start_index,
        end_index=end_index,
        hardened=hardened,
        show=show
    )
