#!/usr/bin/env python3


from hdwallet.cli.__main__ import main as cli_main


def test_cryptocurrencies(cli_tester):

    hdwallet = cli_tester.invoke(
        cli_main, [
            "list", "cryptocurrencies"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output

    hdwallet = cli_tester.invoke(
        cli_main, [
            "l", "cryptocurrencies"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output

    hdwallet = cli_tester.invoke(
        cli_main, [
            "list", "c"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output
    hdwallet = cli_tester.invoke(
        cli_main, [
            "l", "c"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output
