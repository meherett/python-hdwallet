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


def test_hdwallet(cli_tester):

    hdwallet = cli_tester.invoke(
        cli_main, [
            "generate",
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

    assert hdwallet.exit_code == 0
    assert hdwallet.output == str(json.dumps(dumps, indent=4, ensure_ascii=False)) + "\n"
