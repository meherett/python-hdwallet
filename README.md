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

[**BIP39**](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) Mnemonic code for generating deterministic keys:

| Entropy | Checksum | Entropy + Checksum | Mnemonic Length |
| :------ | :------: | :----------------: | :-------------: |
| 128     |  4       | 132                | 12              |
| 160     |  5       | 165                | 15              |
| 192     |  6       | 198                | 18              |
| 224     |  7       | 231                | 21              |
| 256     |  8       | 264                | 24              |

| [BIP44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) Path | `m/44'/coin_type'/{account}'/{change}/{address}` |
| ---------------------------------------------------------------------------: | :----------------------------------------------- |

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
STRENGTH: int = 160  # Default is 128
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
    "strength": 160,
    "entropy": "65e26aceca8c94c708728362288dace6100e8022",
    "mnemonic": "서민 관객 장례 예약 증세 상태 기침 별도 상대 민간 세월 직장 가방 무덤 에어컨",
    "language": "korean",
    "passphrase": null,
    "seed": "a9639475b35ba7b3af339d6da62e552d08e1e8e97ecfbf340cf5e2897449ae166a07300b2fe6272afabfa12880e11e9b2ff432249aa78c3973d4c2e7ef2cceea",
    "root_xprivate_key": "xprv9s21ZrQH143K2HPXATdaGimWKV2TLKqSxR3w7ZD3u7WxedKQeodczeC8BueKUu2kRREd8gytRJmx7LEjUSyAggdZJG9zG3osqSdotr7pZnv",
    "root_xpublic_key": "xpub661MyMwAqRbcEmTzGVAadriEsWrwjnZJKdyXuwcfTT3wXReZCLwsYSWc3DBActGNmx6KxNpxGFpETCqZ7KptShu7x1GtkmVoLziNP9kxM1w",
    "xprivate_key": "xprvA2UGc9Qbxhqkx1YzyVRNGBrHuoCcXgmAi9WKzTg4jZ9vDEEnkc8qNpTE3gdDG5SU3ESBxaixFQusuRmbgo4iNYkUTCUnMezNC2T6JtY9a2a",
    "xpublic_key": "xpub6FTd1ewVo5Q4AVdU5WxNdKo2Tq36w9V25NRvnr5gHtgu62ZwJ9T5vcmhtwka9yUDys5jzQmosevXGyP8VjUkkpZSjoPExptLw9djCRG1xjM",
    "uncompressed": "142968a08a5d0a4e02b436407909f8b4c7026d6bf75568632b2e26136baf5c41cae1aededfacd8e4729ba425ee035c638e26ebcd0c01b9f2b5ab82f33942bfe8",
    "compressed": "02142968a08a5d0a4e02b436407909f8b4c7026d6bf75568632b2e26136baf5c41",
    "chain_code": "95c132b5ad5d01613ce9385942a5c89d72d063832c56ab36e3585565f2c7f000",
    "private_key": "0775b991c4eec49e04c5fde700f5937c7460d89e96b1d0bb0fa2a2ab9bfa54d0",
    "public_key": "02142968a08a5d0a4e02b436407909f8b4c7026d6bf75568632b2e26136baf5c41",
    "wif": "KwUDF1wf29n9LUga7KxyTvF74ShhjNq9sbVR7wMGkrXMj4RapofF",
    "identifier": "8495d3ea533d635726a12322b83fbaf0a5d298ab",
    "finger_print": "8495d3ea",
    "path": "m/44'/0'/0'/0/0",
    "address": "1D63gYH5yjcCPhn2htvMyVh8hvRXxP4BQh"
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
LANGUAGE: str = "english"  # Default is english
# Generate new mnemonic words
MNEMONIC: str = generate_mnemonic(language=LANGUAGE, strength=STRENGTH)
# Secret passphrase/password for mnemonic
PASSPHRASE: Optional[str] = None  # str("meherett")

# Initialize Ethereum mainnet HDWallet
python_hdwallet: PythonHDWallet = PythonHDWallet(cryptocurrency=EthereumMainnet)
# Get Ethereum HDWallet from mnemonic
python_hdwallet.from_mnemonic(
    mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE
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
Mnemonic: laundry screen boy book wreck figure globe accuse minor tired person exile
Base HD Path:  m/44'/60'/0'/0/{address_index} 

(0) m/44'/60'/0'/0/0 0xD6e56e76bDDC557b0Ef92E42F3CFbe3f30a4C295 0xebea344cd7444f9283043fea739ba2763fdc05da663c77e793b6567765285514
(1) m/44'/60'/0'/0/1 0x88F762b29F3e066F34d683562685FFCCcbc1A666 0x173dc3299b30ae3a4d3c699cd7ab3c1eed1ecf711ca144be3fa1a50cce17de5d
(2) m/44'/60'/0'/0/2 0x32607A23156036BcDa285CD443fE9645FeDc648e 0x86386357decd59199fec92b36d58b5deffc6b836dc72e52bae5d5f960f0451ae
(3) m/44'/60'/0'/0/3 0xe0A1887DD307f5751394f02B165c5D47AF713A1E 0xadd3b8bdf73b1025233ec3cadd283563517b4365a790a3b39559b1ef694a3234
(4) m/44'/60'/0'/0/4 0xCAB507Cd8C10D0575Df32B884f18b67150D6A091 0xa4bf2c21e26a45fc1a21fb39472fdc08d3dff4f34b92e53c7bf4e7a5f3387e31
(5) m/44'/60'/0'/0/5 0x1E0f296e435CBD56e0FE0F387E5D68f1580c9E89 0xd1388aaf97b679121221f1816ad9e5b96fb82fb36afa3076d1628d05eb963dab
(6) m/44'/60'/0'/0/6 0x4012109D622Dd11BB2257DBB6Fb78B57358BD9d2 0x87d001a56a56eb572f7a84d21c7eb8eb1cf4d04f4883db28e517c559c6baa260
(7) m/44'/60'/0'/0/7 0x57eEf550A3F8F81dcaf566438d79a7fD8f980451 0xbfb1ec28ae643c917986306a548898ed981f6b849946c70a868e7e632e184407
(8) m/44'/60'/0'/0/8 0xfE2fB0091ff9494b30852A268110174a2C97E110 0xb59df0d4175f3d6660447aca955bdd417a28cef3a78efdf97ef8fe423b8b3fdc
(9) m/44'/60'/0'/0/9 0xD8714F4e98Abb554C84FD65D0F8c346D8b58307C 0xffeedf4dffe90692ef939e7a8a61ee966a73d957923695ffae2a519963895021
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
