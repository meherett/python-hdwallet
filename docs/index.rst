=================================
Hierarchical Deterministic Wallet
=================================

|Build Status| |PyPI Version| |Documentation Status| |PyPI License| |PyPI Python Version| |Coverage Status|

.. |Build Status| image:: https://travis-ci.org/meherett/python-hdwallet.svg?branch=master
   :target: https://travis-ci.org/meherett/python-hdwallet?branch=master

.. |PyPI Version| image:: https://img.shields.io/pypi/v/hdwallet.svg?color=blue
   :target: https://pypi.org/project/hdwallet

.. |Documentation Status| image:: https://readthedocs.org/projects/hdwallet/badge/?version=master
   :target: https://hdwallet.readthedocs.io/en/master/?badge=master

.. |PyPI License| image:: https://img.shields.io/pypi/l/hdwallet?color=black
   :target: https://pypi.org/project/hdwallet

.. |PyPI Python Version| image:: https://img.shields.io/pypi/pyversions/hdwallet.svg
   :target: https://pypi.org/project/hdwallet

.. |Coverage Status| image:: https://coveralls.io/repos/github/meherett/python-hdwallet/badge.svg?branch=master
   :target: https://coveralls.io/github/meherett/python-hdwallet?branch=master

Python-based library for the implementation of a hierarchical deterministic wallet generator for over 140+ multiple cryptocurrencies.
It allows the handling of multiple coins, multiple accounts, external and internal chains per account and millions of addresses per the chain.

Simple Bitcoin mainnet HDWallet generator:

::

    #!/usr/bin/env python3

    from hdwallet import HDWallet
    from hdwallet.utils import generate_entropy
    from hdwallet.symbols import BTC as SYMBOL
    from typing import Optional

    import json

    # Choose strength 128, 160, 192, 224 or 256
    STRENGTH: int = 160  # Default is 128
    # Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
    LANGUAGE: str = "korean"  # Default is english
    # Generate new entropy hex string
    ENTROPY: str = generate_entropy(strength=STRENGTH)
    # Secret passphrase for mnemonic
    PASSPHRASE: Optional[str] = None  # "meherett"

    # Initialize Bitcoin mainnet HDWallet
    hdwallet: HDWallet = HDWallet(symbol=SYMBOL, use_default_path=False)
    # Get Bitcoin HDWallet from entropy
    hdwallet.from_entropy(
        entropy=ENTROPY, language=LANGUAGE, passphrase=PASSPHRASE
    )

    # Derivation from path
    # hdwallet.from_path("m/44'/0'/0'/0/0")
    # Or derivation from index
    hdwallet.from_index(44, hardened=True)
    hdwallet.from_index(0, hardened=True)
    hdwallet.from_index(0, hardened=True)
    hdwallet.from_index(0)
    hdwallet.from_index(0)

    # Print all Bitcoin HDWallet information's
    print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

.. raw:: html

   <details open>
        <summary>Output</summary>

.. code-block:: python

   {
       "cryptocurrency": "Bitcoin",
       "symbol": "BTC",
       "network": "mainnet",
       "strength": 160,
       "entropy": "c5b0d0ee698f3f72b6265f1bc591f8f2d7afa6dd",
       "mnemonic": "주일 액수 명단 천둥 해수욕장 전망 추천 직업 그룹 단위 신체 파란색 시청 천천히 스트레스",
       "language": "korean",
       "passphrase": null,
       "seed": "5a9b9667ccd07b3c641b1ba95e9119dd1d5a3034fd46cd2f27fc1f160c7dcd824fc0ab4710a9ae90582dffc3b0803bcbc0a8160feeaab4c70511c5035859decf",
       "root_xprivate_key": "xprv9s21ZrQH143K2qMHU8aghJ4MoQR5g5mowXbeP2vCP937bseZGX929dmJudL7u4xRxtKvh58pxz1PhtCbWW2yUH14jdduKVMV9FkBMpM2Hyw",
       "root_xpublic_key": "xpub661MyMwAqRbcFKRkaA7h4S16MSFa5YVfJkXFBRKowUa6Ufyhp4TGhS5nkvkLXSmdNjoszzDkU26WW2rg1zBsQBt6Pv3T8oLEAExGHD3hcQs",
       "xprivate_key": "xprvA2YyMZWyPK2xo4eZgyypp2CzcHnxNzGbruGg7vmgaAVCtBtrjwzuhXJBNM3FrwBh85ajxHErNR6ByN77WJARpC1HDC7kTwa2yr7Mu9Pz5Qq",
       "xpublic_key": "xpub6FYKm53sDgbG1Yj2o1WqBA9jAKdSnSzTE8CGvKBJ8W2BkzE1HVKAFKcfDcCHKpL5BQRg2HjbNSt55jpFshY7W1KFtp7zjB3DhNAmiFv6kzB",
       "uncompressed": "081016370b45d7e23bd89b07d6886036f5e4df9a129eee3b488c177ba7881856e24d337b280f9d32539a22445e567543b39b708edf5289442f36dcde958a3433",
       "compressed": "03081016370b45d7e23bd89b07d6886036f5e4df9a129eee3b488c177ba7881856",
       "chain_code": "cf9ee427ed8073e009a5743056e8cf19167f67ca5082c2c6635b391e9a4e0b0d",
       "private_key": "f79495fda777197ce73551bcd8e162ceca19167575760d3cc2bced4bf2a213dc",
       "public_key": "03081016370b45d7e23bd89b07d6886036f5e4df9a129eee3b488c177ba7881856",
       "wif": "L5WyVfBu8Sz3iGZtrwJVSP2wDJmu7HThGd1EGekFBnviWgzLXpJd",
       "finger_print": "ac13e305",
       "semantic": "p2pkh",
       "path": "m/44'/0'/0'/0/0",
       "hash": "ac13e305a88bd9968f1c058fcf5d9a6b1b9ef484",
       "addresses": {
           "p2pkh": "1Ggs3kkNrPPWoW17iDFQWgMdw3CD8BzBiv",
           "p2sh": "3GQVUFePz517Hf61Vsa9H2tHj5jw5y6ngV",
           "p2wpkh": "bc1q4sf7xpdg30vedrcuqk8u7hv6dvdeaayy3uw5cj",
           "p2wpkh_in_p2sh": "3JyV5aSgdVYEjQodPWHfvehQ5227EDr3sN",
           "p2wsh": "bc1qnk0s9q4379n6v9vg0lnhdu5qhjyx99u2xm238pmckmjg9v29q54saddzp9",
           "p2wsh_in_p2sh": "3MmsEoP7GLHzuLVgkAtcRtyXLTWh8zNAcd"
       }
   }

.. raw:: html

   </details>

For more info see the BIP specs.

.. list-table::
   :widths: 10 185
   :header-rows: 1

   * - BIP's
     - Titles
   * - `BIP39 <https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki>`_
     - Mnemonic code for generating deterministic keys
   * - `BIP85 <https://github.com/bitcoin/bips/blob/master/bip-0085.mediawiki>`_
     - Deterministic Entropy From BIP32 Keychains
   * - `BIP32 <https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki>`_
     - Hierarchical Deterministic Wallets
   * - `BIP44 <https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki>`_
     - Multi-Account Hierarchy for Deterministic Wallets
   * - `BIP49 <https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki>`_
     - Derivation scheme for P2WPKH-nested-in-P2SH based accounts
   * - `BIP84 <https://github.com/bitcoin/bips/blob/master/bip-0084.mediawiki>`_
     - Derivation scheme for P2WPKH based accounts
   * - `BIP141 <https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki>`_
     - Segregated Witness (Consensus layer)
