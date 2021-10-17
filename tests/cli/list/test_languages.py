#!/usr/bin/env python3


from hdwallet.cli.__main__ import main as cli_main


def test_languages(cli_tester):

    hdwallet = cli_tester.invoke(
        cli_main, [
            "list", "languages"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output

    hdwallet = cli_tester.invoke(
        cli_main, [
            "l", "languages"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output

    hdwallet = cli_tester.invoke(
        cli_main, [
            "list", "l"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output

    hdwallet = cli_tester.invoke(
        cli_main, [
            "l", "l"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output
