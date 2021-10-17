#!/usr/bin/env python3

from hdwallet.cli.__main__ import main as cli_main
from hdwallet import __version__


def test_hdwallet_cli(cli_tester):

    assert cli_tester.invoke(cli_main).exit_code == 0

    assert cli_tester.invoke(cli_main, ["generate"]).exit_code == 0

    version = cli_tester.invoke(cli_main, ["--version"])
    assert version.exit_code == 0
    assert version.output == "%s\n" % __version__
