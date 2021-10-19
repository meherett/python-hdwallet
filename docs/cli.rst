============================
Command Line Interface (CLI)
============================

After you have installed, type ``hdwallet`` to verify that it worked:

::

    $ hdwallet
    Usage: hdwallet [OPTIONS] COMMAND [ARGS]...

    Options:
      -v, --version  Show HDWallet version and exit.
      -h, --help     Show this message and exit.

    Commands:
      generate (g)  Select Generate for HDWallet.
      list (l)      Select List for HDWallet information.



.. click:: hdwallet.cli.__main__:main
  :prog: hdwallet
  :show-nested: