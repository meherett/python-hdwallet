#!/usr/bin/env python3


from hdwallet.cli.__main__ import main as cli_main


def test_strengths(cli_tester):

    hdwallet = cli_tester.invoke(
        cli_main, [
            "list", "strengths"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output

    hdwallet = cli_tester.invoke(
        cli_main, [
            "l", "strengths"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output

    hdwallet = cli_tester.invoke(
        cli_main, [
            "list", "s"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output

    hdwallet = cli_tester.invoke(
        cli_main, [
            "l", "s"
        ]
    )

    assert hdwallet.exit_code == 0
    assert hdwallet.output
