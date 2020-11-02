# Python-HDWallet

[![Build Status](https://travis-ci.org/meherett/python-hdwallet.svg?branch=master)](https://travis-ci.org/meherett/python-hdwallet?branch=master)
[![PyPI Version](https://img.shields.io/pypi/v/python-hdwallet.svg?color=blue)](https://pypi.org/project/python-hdwallet)
[![PyPI Python Version](https://img.shields.io/pypi/pyversions/python-hdwallet.svg)](https://pypi.org/project/python-hdwallet)
[![Coverage Status](https://coveralls.io/repos/github/meherett/python-hdwallet/badge.svg?branch=master)](https://coveralls.io/github/meherett/python-hdwallet?branch=master)

Python-based library for the implementation of a [Hierarchical Deterministic (HD)](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki) wallet generator for Cryptocurrencies.

## Available Cryptocurrencies

This library simplify the process of creating new HDWallet's for:

| Cryptocurrencies                                         | Symbols             | Mainnet | Testnet | Coin Type | Default Paths       |
| :------------------------------------------------------- | :-----------------: | :-----: | :-----: | :-------: | :-----------------: |
| [Bitcoin](https://github.com/bitcoin/bitcoin)            |  `BTC`, `BTCTEST`   | Yes     | Yes     | 0         | `m/44'/0'/0'/0/0`   |
| [Ethereum](https://github.com/ethereum/go-ethereum)      |  `ETH`, `ETHTEST`   | Yes     | Yes     | 60        | `m/44'/60'/0'/0/0`  |
| [Dogecoin](https://github.com/dogecoin/dogecoin)         |  `DOGE`, `DOGETEST` | Yes     | Yes     | 3         | `m/44'/3'/0'/0/0`   |
| [Litecoin](https://github.com/litecoin-project/litecoin) |  `LTC`, `LTCTEST`   | Yes     | Yes     | 2         | `m/44'/2'/0'/0/0`   |
| [Omni](https://github.com/omnilayer/omnicore)            |  `OMNI`, `OMNITEST` | Yes     | Yes     | 200       | `m/44'/200'/0'/0/0` |
| [Dash](https://github.com/dashpay/dash)                  |  `DASH`, `DASHTEST` | Yes     | Yes     | 5         | `m/44'/5'/0'/0/0`   |
| [Qtum](https://github.com/qtumproject/qtum)              |  `QTUM`, `QTUMTEST` | Yes     | Yes     | 88        | `m/44'/88'/0'/0/0`  |

 [BIP44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) Path | `m/44'/coin_type'/{account}'/{change}/{address}`
 ---------------------------------------------------------------------------: | :-----------------------------------------------

> **NOTICE:** All Cryptocurrencies testnet network default paths are set to `m/44'/1'/0'/0/0` except Ethereum and also Ethereum cryptocurrency `ETHTEST` testnet is an alias of `ETH` mainnet network.

## Installation

```
$ pip install python-hdwallet
```

If you want to run the latest version of the code, you can install from git:

```
$ pip install git+git://github.com/meherett/python-hdwallet.git
```

For the versions available, see the [tags on this repository](https://github.com/meherett/python-hdwallet/tags).

## Development

We welcome pull requests. To get started, just fork this repository, clone it locally, and run:

```
$ pip install -e .[tests] -r requirements.txt
```

## Quick Start

Simple Bitcoin cryptocurrency mainnet HDWallet generator:

```python
#!/usr/bin/env python3

from python_hdwallet import PythonHDWallet as HDWallet
from python_hdwallet.utils import generate_entropy
from python_hdwallet.symbols import BTC
from typing import Optional

import json

# Choose strength 128, 160, 192, 224 or 256
STRENGTH: int = 128  # Default is 128
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
LANGUAGE: str = "korean"  # Default is english
# Generate new entropy
ENTROPY: str = generate_entropy(strength=STRENGTH)
# Secret passphrase/password for mnemonic
PASSPHRASE: Optional[str] = None  # str("meherett")

# Initialize Bitcoin mainnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=BTC)
# Get Bitcoin HDWallet from entropy
hdwallet.from_entropy(
    entropy=ENTROPY, passphrase=PASSPHRASE, language=LANGUAGE
)

# Derivation from path
# hdwallet.from_path("m/44'/0'/0'/0/0")
# Or derivation from index
hdwallet.from_index(44, harden=True)
hdwallet.from_index(0, harden=True)
hdwallet.from_index(0, harden=True)
hdwallet.from_index(0)
hdwallet.from_index(0)

# Print all Bitcoin HDWallet information's
print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))
```

<details>
  <summary>Output</summary><br/>

```json5
{
    "cryptocurrency": "Bitcoin",
    "symbol": "BTC",
    "network": "mainnet",
    "entropy": "e79e3c68ec0fd87a1fb4289724e2f607",
    "strength": 128,
    "mnemonic": "페인트 할인 궁극적 최종 효율적 모습 실례 안방 오직 냉동 정말 고급",
    "language": "korean",
    "passphrase": null,
    "seed": "f134313acb31294a7ab9a931106390fc14af858aea142cafcb0c75077436c07964e81269a1e700c0593da0d844de64c0cb2b3fbbe722f4ae0fd105c788bea6ad",
    "root_xprivate_key": "xprv9s21ZrQH143K324MxoQyDscpGqomWQtxkrr5v98GjfrTs2tkLq5RDYqxAjck9dRKfnPNFDoFqStXjd1bQDAY5BaX67DuscMAgd41fjQwAdX",
    "root_xpublic_key": "xpub661MyMwAqRbcFW8q4pwyb1ZYpseFuscp85mgiXXtJ1PSjqDttNPfmMAS217EJP7gQMRK3SUwzsxsqC3a4Bw26WptqcZJZ1oTZCzPPfhT44N",
    "xprivate_key": "xprvA2cCSUDr4fqf3UDgmr4hFCKoeNeQRrnYDqBtCcVYbLbLBfaAFUUiufrJ3HjZwDRChhPGYZQVRvscgj6WjEq8DJnvmREaBfji3jt69QQa9MN",
    "xpublic_key": "xpub6FbYqykju3PxFxJ9ssbhcLGYCQUtqKWPb47UzzuA9g8K4TuJo1nyTUAmtYGEwRmykqvdbHSogUBmmtWt67ppVa1MKf2FZELaZtdSZC2oxEo",
    "uncompressed": "5403e9ec33b1a4eba028cc5ce65bc783c4a69e7e5eac2d6b7e0b3f3ecf429e908678d0584b5a175c13234289c7419c27650d362a98010cf1a884817296033b84",
    "compressed": "025403e9ec33b1a4eba028cc5ce65bc783c4a69e7e5eac2d6b7e0b3f3ecf429e90",
    "chain_code": "2d99e2234657dfbf423b09b89f2431fbef32aa80e231fa7ca879f35b852a00a4",
    "private_key": "961384849e0aefd7e7fd90a5757b6f10a02e2ef02f488244dc48ec6cae8b8d48",
    "public_key": "025403e9ec33b1a4eba028cc5ce65bc783c4a69e7e5eac2d6b7e0b3f3ecf429e90",
    "wif": "L2FSSfvrrcwJXp8M5ACdXk3VQyfqHsa8ct2jH29mmV2RfbnMtSq9",
    "identifier": "61e3b1f3044374c5f54294f4cfcfeaede2eedf83",
    "finger_print": "61e3b1f3",
    "path": "m/44'/0'/0'/0/0",
    "address": "19vbK9Cqoqc9otknvGP6jmLxXkFigZAdrQ"
}
```
</details>

Ethereum cryptocurrency testnet [Ganache-CLI/TestRPC](https://github.com/trufflesuite/ganache-cli) wallet look's like:

```python
#!/usr/bin/env python3

from python_hdwallet import PythonHDWallet
from python_hdwallet.cryptocurrencies import EthereumMainnet  # Alias EthereumTestnet
from python_hdwallet.utils import generate_mnemonic
from typing import Optional

# Choose strength 128, 160, 192, 224 or 256
STRENGTH: int = 128  # Default is 128
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
LANGUAGE: str = "italian"  # Default is english
# Generate new mnemonic words
MNEMONIC: str = generate_mnemonic(language=STRENGTH, strength=LANGUAGE)
# Secret passphrase/password for mnemonic
PASSPHRASE: Optional[str] = None  # str("meherett")

# Initialize Ethereum mainnet HDWallet
python_hdwallet: PythonHDWallet = PythonHDWallet(cryptocurrency=EthereumMainnet)
# Get Ethereum HDWallet from mnemonic
python_hdwallet.from_mnemonic(
    mnemonic=MNEMONIC, passphrase=PASSPHRASE
)

print("Mnemonic:", python_hdwallet.mnemonic())
print("Base HD Path:  m/44'/60'/0'/0/{address_index}", "\n")

# Get Ethereum HDWallet information's from address indexes
for address_index in range(10):
    # Derivation from Ethereum BIP44 path
    python_hdwallet.from_path(
        path=EthereumMainnet.BIP44_PATH.format(
            account=0, change=0, address=address_index
        )
    )
    # Print address_index, path, address and private_key
    print(f"({address_index}) {python_hdwallet.path()} {python_hdwallet.address()} 0x{python_hdwallet.private_key()}")
    # Clean derivation indexes/path
    python_hdwallet.clean_derivation()
```

<details>
  <summary>Output</summary><br/>

```shell script
Mnemonic: obvious private cheap artwork cradle alone useless trust globe home scrub receive
Base HD Path:  m/44'/60'/0'/0/{address_index} 

(0) m/44'/60'/0'/0/0 0x03F3aFCA8d7F8D947FCb3de008053A7d22Ff44c9 0xa40e21e99464006be1f00146be864fb7ff4dfcfe2d7b8f3450edc778db9af462
(1) m/44'/60'/0'/0/1 0x9e68BDDe22BEfBc027133415DE5a9d8091c80AAa 0x9db6c57bb27260442e7741982f57eaf0d3dbabbd5d0cf44012f140212068dd24
(2) m/44'/60'/0'/0/2 0x973D9c9173bf927c8E9dC4c7d0371ea4278baD7C 0x59b6c9c20b7bb02a168256963e7cc96deca3499b290b14b26254e815956bca7a
(3) m/44'/60'/0'/0/3 0x40498150AAfC4359db68Ecf3c9086f357772691a 0x2f0173d5592e7193f6a08217dbbc3e1daadbc6fece37a199cef213bd5e0984c3
(4) m/44'/60'/0'/0/4 0x7493373d186A4C24f66cf519dA8837686b8817e8 0xb5293b9bea3a9a4fdfec54b07b128fc47ddbbe1ca9b9c036dd8a1905b4b74a5d
(5) m/44'/60'/0'/0/5 0x8Db556BBD5baaBc51EAbFbE5F3E621113435779c 0xc5093d734e2b3d045a546c4af6567dc7ae3a8ea597b3aa00e740886495797044
(6) m/44'/60'/0'/0/6 0x581dFbFB6705274D49c91Badef09d94134d81bDc 0xcf2e664d33fd18e8e64b4c5b19e1351f8d77f5e9e3836d2f40dad81dfb56e118
(7) m/44'/60'/0'/0/7 0x39Da3993353e83B71C677695717963757B138BB7 0x0442f8a12c3e47fc279b6fd5b9f3cc3d1dba1acb648ffd80742f728aaf4745fb
(8) m/44'/60'/0'/0/8 0x88DFf10366547EF5C27fdBb22D476198e5a021E4 0x1bc73d9763b6ec48652137cc18adc0c8302ff3c44eabeaf7aca8ceaa2634a42f
(9) m/44'/60'/0'/0/9 0x196D893126fDA7f433fD0A5F49855D031C54f8D4 0xc72b824601bcb1088a62c09b7bc5c14c63a69de1fcfe5bb39eb3f6524f322522
```
</details>

[Click this to see more examples](https://github.com/meherett/python-hdwallet/blob/master/examples).

## Testing

You can run the tests with:

```
$ pytest
```

Or use `tox` to run the complete suite against the full set of build targets, or pytest to run specific 
tests against a specific version of Python.

## License

Distributed under the [ISC](https://github.com/meherett/python-hdwallet/blob/master/LICENSE) license. See ``LICENSE`` for more information.
