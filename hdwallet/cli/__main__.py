#!/usr/bin/env python

from click_aliases import ClickAliasedGroup
from typing import Optional

from hdwallet import __version__
from hdwallet.cli.generate.hdwallet import generate_hdwallet
from hdwallet.cli.generate.addresses import generate_addresses
from hdwallet.cli.list.cryptocurrencies import list_cryptocurrencies
from hdwallet.cli.list.languages import list_languages
from hdwallet.cli.list.strengths import list_strengths
from hdwallet.cli import click


CONTEXT_SETTINGS = dict(
    help_option_names=["-h", "--help"],
)


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(__version__)
    ctx.exit()


@click.group(cls=ClickAliasedGroup,
             options_metavar="[OPTIONS]", context_settings=CONTEXT_SETTINGS)
@click.option("-v", "--version", is_flag=True, callback=print_version,
              expose_value=False, help="Show HDWallet version and exit.")
def main():
    pass


@main.group("generate", aliases=["g"], cls=ClickAliasedGroup, options_metavar="[OPTIONS]",
            short_help="Select Generate for HDWallet.", invoke_without_command=True)
@click.option("-s", "--symbol", type=str, default="BTC",
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
@click.option("-ad", "--address", type=int, default=0,
              help="Set Derivation from address.", show_default=True)
@click.option("-p", "--path", type=str, default=None,
              help="Set Master key derivation path.", show_default=True)
@click.option("-prv", "--private-key", type=str, default=None,
              help="Set Master key from private key.", show_default=True)
@click.option("-pub", "--public-key", type=str, default=None,
              help="Set Master key from public key.", show_default=True)
@click.option("-w", "--wif", type=str, default=None,
              help="Set Master key from wallet important format.", show_default=True)
@click.option("-sm", "--semantic", type=str, default="p2pkh",
              help="Set Semantic for xprivate and xpublic keys.", show_default=True)
@click.pass_context
def generate(
        context: click.core.Context,
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
        address: int,
        path: Optional[str],
        private_key: Optional[str],
        public_key: Optional[str],
        wif: Optional[str],
        semantic: str
):
    if context.invoked_subcommand is None:
        return generate_hdwallet(
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
            address=address,
            path=path,
            private_key=private_key,
            public_key=public_key,
            wif=wif,
            semantic=semantic
        )


@generate.command("addresses", aliases=["a"], options_metavar="[OPTIONS]",
                  short_help="Select Addresses for generation HDWallet addresses.")
@click.option("-s", "--symbol", type=str, default="BTC",
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
    return generate_addresses(
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


@main.group("list", aliases=["l"], cls=ClickAliasedGroup, options_metavar="[OPTIONS]",
            short_help="Select List for HDWallet information.", invoke_without_command=True)
def list():
    pass


@list.command("cryptocurrencies", aliases=["c"], options_metavar="[OPTIONS]",
              short_help="List Available cryptocurrencies of HDWallet.")
def cryptocurrencies():
    return list_cryptocurrencies()


@list.command("languages", aliases=["l"], options_metavar="[OPTIONS]",
              short_help="List Languages of mnemonic words.")
def languages():
    return list_languages()


@list.command("strengths", aliases=["s"], options_metavar="[OPTIONS]",
              short_help="List Strengths of mnemonic words.")
def strengths():
    return list_strengths()
