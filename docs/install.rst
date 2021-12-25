===================
Installing HDWallet
===================

The easiest way to install HDWallet is via pip:

::

    $ pip install hdwallet


If you want to run the latest version of the code, you can install from git:

::

    $ pip install git+git://github.com/meherett/python-hdwallet.git

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

For the versions available, see the `tags on this repository <https://github.com/meherett/python-hdwallet/tags>`_.

Development
===========

We welcome pull requests. To get started, just fork this `github repository <https://github.com/meherett/python-hdwallet>`_, clone it locally, and run:

::

    $ pip install -e . -r requirements.txt
