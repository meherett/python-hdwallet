===================
Installing HDWallet
===================

The easiest way to install ``hdwallet`` is via pip:

::

    $ pip install hdwallet


To install ``hdwallet`` command line interface globally, for Linux `sudo` may be required:

::

    $ pip install hdwallet[cli]


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


If you want to run the latest version of the code, you can install from git:

::

    $ pip install git+git://github.com/meherett/python-hdwallet.git


For the versions available, see the `tags on this repository <https://github.com/meherett/python-hdwallet/tags>`_.

Development
===========

We welcome pull requests. To get started, just fork this `github repository <https://github.com/meherett/python-hdwallet>`_, clone it locally, and run:

::

    $ pip install -e .[cli,tests,docs] -r requirements.txt
