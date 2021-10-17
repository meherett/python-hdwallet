#!/usr/bin/env python3

import json
import os

from hdwallet.cli.__main__ import main as cli_main

# Test Values
base_path = os.path.dirname(__file__)
file_path = os.path.abspath(os.path.join(base_path, "..", "..", "values.json"))
values = open(file_path, "r", encoding="utf-8")
_ = json.loads(values.read())
values.close()


def test_addresses(cli_tester):

    hdwallet = cli_tester.invoke(
        cli_main, [
            "generate", "addresses",
            "--symbol", _["bitcoin"]["mainnet"]["symbol"],
            "--entropy", _["bitcoin"]["mainnet"]["entropy"],
            "--passphrase", _["bitcoin"]["mainnet"]["passphrase"],
            "--language", _["bitcoin"]["mainnet"]["language"]
        ]
    )

    dumps: dict = _["bitcoin"]["mainnet"]

    del dumps["root_xprivate_key_hex"]
    del dumps["root_xpublic_key_hex"]
    del dumps["xprivate_key_hex"]
    del dumps["xpublic_key_hex"]

    addresses: str = ""
    for address in _["bitcoin"]["addresses"]:
        addresses += f"{address}\n"

    assert hdwallet.exit_code == 0
    assert hdwallet.output == addresses

    hdwallet = cli_tester.invoke(
        cli_main, [
            "generate", "addresses",
            "--symbol", _["bitcoin"]["mainnet"]["symbol"],
            "--mnemonic", _["bitcoin"]["mainnet"]["mnemonic"],
            "--passphrase", _["bitcoin"]["mainnet"]["passphrase"],
            "--language", _["bitcoin"]["mainnet"]["language"]
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output == addresses

    hdwallet = cli_tester.invoke(
        cli_main, [
            "generate", "addresses",
            "--symbol", _["bitcoin"]["mainnet"]["symbol"],
            "--seed", _["bitcoin"]["mainnet"]["seed"]
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output == addresses

    hdwallet = cli_tester.invoke(
        cli_main, [
            "generate", "addresses",
            "--symbol", _["bitcoin"]["mainnet"]["symbol"],
            "--xprivate-key", _["bitcoin"]["mainnet"]["root_xprivate_key"]
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output == addresses

    hdwallet = cli_tester.invoke(
        cli_main, [
            "generate", "addresses",
            "--symbol", _["bitcoin"]["mainnet"]["symbol"],
            "--xpublic-key", _["bitcoin"]["mainnet"]["root_xpublic_key"]
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output
