# Hierarchical Deterministic Wallet

[![Build Status](https://travis-ci.org/meherett/python-hdwallet.svg?branch=master)](https://travis-ci.org/meherett/python-hdwallet?branch=master)
[![PyPI Version](https://img.shields.io/pypi/v/hdwallet.svg?color=blue)](https://pypi.org/project/hdwallet)
[![Documentation Status](https://readthedocs.org/projects/hdwallet/badge/?version=master)](https://hdwallet.readthedocs.io/en/master/?badge=master)
[![PyPI Python Version](https://img.shields.io/pypi/pyversions/hdwallet.svg)](https://pypi.org/project/hdwallet)
[![Coverage Status](https://coveralls.io/repos/github/meherett/python-hdwallet/badge.svg?branch=master)](https://coveralls.io/github/meherett/python-hdwallet?branch=master)

Python-based library for the implementation of a hierarchical deterministic wallet generator for multiple cryptocurrencies.

## Available Cryptocurrencies

This library simplifies the process of creating a new HDWallet's for:

| Cryptocurrencies                                                  | Symbols             | Mainnet | Testnet | Coin Type | Default Paths        |
| :---------------------------------------------------------------- | :-----------------: | :-----: | :-----: | :-------: | :------------------: |
| [Bitcoin](https://github.com/bitcoin/bitcoin)                     |  `BTC`, `BTCTEST`   | Yes     | Yes     | 0         | `m/44'/0'/0'/0/0`    |
| [Bitcoin Cash](https://github.com/bitcoincashorg/bitcoincash.org) |  `BCH`              | Yes     | No      | 145       | `m/44'/145'/0'/0/0`  |
| [Bitcoin Gold](https://github.com/BTCGPU/BTCGPU)                  |  `BTG`              | Yes     | No      | 156       | `m/44'/156'/0'/0/0`  |
| [Ethereum](https://github.com/ethereum/go-ethereum)               |  `ETH`, `ETHTEST`   | Yes     | Yes     | 60        | `m/44'/60'/0'/0/0`   |
| [Dogecoin](https://github.com/dogecoin/dogecoin)                  |  `DOGE`, `DOGETEST` | Yes     | Yes     | 3         | `m/44'/3'/0'/0/0`    |
| [XinFin](https://github.com/XinFinOrg/XDPoSChain)                 |  `XDC`, `XDCTEST`   | Yes     | Yes     | 550       | `m/44'/550'/0'/0/0`  |
| [Litecoin](https://github.com/litecoin-project/litecoin)          |  `LTC`, `LTCTEST`   | Yes     | Yes     | 2         | `m/44'/2'/0'/0/0`    |
| [Navcoin](https://github.com/navcoin/navcoin-core)                |  `NAV`              | Yes     | No      | 130       | `m/44'/130'/0'/0/0`  |
| [Shadow Cash](https://github.com/shadowproject/shadow)            |  `SDC`, `SDCTEST`   | Yes     | Yes     | 35        | `m/44'/35'/0'/0/0`   |
| [Viacoin](https://github.com/viacoin/viacore-viacoin)             |  `VIA`, `VIATEST`   | Yes     | Yes     | 14        | `m/44'/14'/0'/0/0`   |
| [Omni](https://github.com/omnilayer/omnicore)                     |  `OMNI`, `OMNITEST` | Yes     | Yes     | 200       | `m/44'/200'/0'/0/0`  |
| [Dash](https://github.com/dashpay/dash)                           |  `DASH`, `DASHTEST` | Yes     | Yes     | 5         | `m/44'/5'/0'/0/0`    |
| [Qtum](https://github.com/qtumproject/qtum)                       |  `QTUM`, `QTUMTEST` | Yes     | Yes     | 2301      | `m/44'/2301'/0'/0/0` |

> **NOTICE:** All Cryptocurrencies testnet networks default paths are set to **`m/44'/1'/0'/0/0`** value.

## Installation

PIP to install HDWallet globally, for Linux `sudo` may be required:

```
$ pip install hdwallet
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

from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import BTC
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
hdwallet: HDWallet = HDWallet(symbol=BTC)
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
```

<details>
  <summary>Output</summary><br/>

```json5
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
```
</details>

Ethereum cryptocurrency mainnet [Ganache-CLI](https://github.com/trufflesuite/ganache-cli) wallet look's like:

```python
#!/usr/bin/env python3

from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet  # Alias EthereumTestnet
from hdwallet.derivations import BIP44Derivation
from hdwallet.utils import generate_mnemonic
from typing import Optional

# Generate english mnemonic words
MNEMONIC: str = generate_mnemonic(language="english", strength=128)
# Secret passphrase/password for mnemonic
PASSPHRASE: Optional[str] = None  # str("meherett")

# Initialize Ethereum mainnet BIP44HDWallet
bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=EthereumMainnet)
# Get Ethereum BIP44HDWallet from mnemonic
bip44_hdwallet.from_mnemonic(
    mnemonic=MNEMONIC, passphrase=PASSPHRASE
)
# Clean default BIP44 derivation indexes/paths
bip44_hdwallet.clean_derivation()

print("Mnemonic:", bip44_hdwallet.mnemonic())
print("Base HD Path:  m/44'/60'/0'/0/{address_index}", "\n")

# Get Ethereum BIP44HDWallet information's from address index
for address_index in range(10):
    # Derivation from Ethereum BIP44 derivation path
    bip44_derivation: BIP44Derivation = BIP44Derivation(
        cryptocurrency=EthereumMainnet, account=0, change=False, address=address_index
    )
    # Drive Ethereum BIP44HDWallet
    bip44_hdwallet.from_path(path=bip44_derivation)
    # Print address_index, path, address and private_key
    print(f"({address_index}) {bip44_hdwallet.path()} {bip44_hdwallet.address()} 0x{bip44_hdwallet.private_key()}")
    # Clean derivation indexes/paths
    bip44_hdwallet.clean_derivation()
```

<details>
  <summary>Output</summary><br/>

```shell script
Mnemonic: bright demand olive glance crater key head glory quantum leisure intact age
Base HD Path:  m/44'/60'/0'/0/{address_index} 

(0) m/44'/60'/0'/0/0 0x3a149f0c5dc5c0F1E29e573215C23710dE9c4f87 0xa45f9af43912fdd5e88c492226be082029f257681d4b3e73b68be535d2fb0526
(1) m/44'/60'/0'/0/1 0x9e8A4fD9bA74DbB0c7F465EF56b47489793AA102 0x6e5ab2a3ae20c7b3a1c0645b03689e88e8cdff16f6a39d6a420bfebc20e8a941
(2) m/44'/60'/0'/0/2 0x08Eb0646ddc52E12a03215b94b244B674e9D7a0F 0x938caf07197eda13679bfd88df7e5f6eac3cd9f9248ed445f1a0e084a3e9417c
(3) m/44'/60'/0'/0/3 0x6dB1Ac10bbbE7bdc6bcB246E2Dd36884c346CbE8 0x304e9bebaeef3f4ae7c4d2ef268f40f503d8f47fd2621a575d8f73f49762cbc0
(4) m/44'/60'/0'/0/4 0xd528281f804D950c743Ca48FCcC3D76A3d9AcD5C 0x82a0284b443ec73884806ac9450f09110d8dba024120985431b80a520b3f2911
(5) m/44'/60'/0'/0/5 0xaF24cc02Fd5E0285237677cDDD00ae8E4a9d6E5E 0xb03c61e992f5475222295077a89cf35011984dcdcd1da3666ebffc9ebefe22a9
(6) m/44'/60'/0'/0/6 0x55A972f207DB3498DCBbD97062472A5c10b3266b 0xc003175828a6f768610fb2396b3fcec7fa1957770de2462b9e6d3a0a23346c76
(7) m/44'/60'/0'/0/7 0x7e62C187e597Fc544D5769a38A8e026F5529c81B 0x04bfcff46587fd98e682e3b7acff720051b1b0bee3309fb13703338bbde211cd
(8) m/44'/60'/0'/0/8 0x7aF4A78000032a3FBaF4Ac5a5f64a50FF69f0442 0x1b642b77519cf6e6107827e4773a15975edda6471ff90735e2fc0cf7d8560ac8
(9) m/44'/60'/0'/0/9 0x379a25BB89043f8b875A73eA61aF4F7b70cD73e5 0x4f9fb333faf8ecf8f22d212a0b1c946e4d4c32fa0b7794326038d464b241d771
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

## BIP Implementation's

For more info see the BIP specs.

[**BIP39** spec](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) **·** Mnemonic code for generating deterministic keys

[**BIP85** spec](https://github.com/bitcoin/bips/blob/master/bip-0085.mediawiki) **·** Deterministic Entropy From BIP32 Keychains

[**BIP32** spec](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki) **·**  Hierarchical Deterministic Wallets

[**BIP44** spec](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) **·**  Multi-Account Hierarchy for Deterministic Wallets

[**BIP49** spec](https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki) **·**  Derivation scheme for P2WPKH-nested-in-P2SH based accounts

[**BIP84** spec](https://github.com/bitcoin/bips/blob/master/bip-0048.mediawiki) **·**  Derivation scheme for P2WPKH based accounts

[**BIP141** spec](https://github.com/bitcoin/bips/blob/master/bip-0014.mediawiki) **·**  Segregated Witness (Consensus layer)

## License

Distributed under the [ISC](https://github.com/meherett/python-hdwallet/blob/master/LICENSE) license. See ``LICENSE`` for more information.
