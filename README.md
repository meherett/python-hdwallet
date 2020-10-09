# HDWallet

[![Build Status](https://travis-ci.org/meherett/hdwallet.svg?branch=master)](https://travis-ci.org/meherett/python-hdwallet)
[![PyPI Version](https://img.shields.io/pypi/v/python-hdwallet.svg?color=blue)](https://pypi.org/project/python-hdwallet)
[![Coverage Status](https://coveralls.io/repos/github/meherett/hdwallet/badge.svg?branch=master)](https://coveralls.io/github/meherett/hdwallet?branch=master)

The implementation of Hierarchical Deterministic (HD) wallet generator for Cryptocurrencies.

## Available Cryptocurrencies

This library simplify the process of creating new hdwallet's for:

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

> **Note**: 
> - All cryptocurrencies testnet default paths are `m/44'/1'/0'/0/0` except Ethereum.
> - Ethereum cryptocurrency testnet `ETHTEST` is alias of mainnet `ETH` network.

## Installation

```
$ pip install python-hdwallet
```

For the versions available, see the [tags on this repository](https://github.com/meherett/hdwallet/tags).

## Development

We welcome pull requests. To get started, just fork this repository, clone it locally, and run:

```
$ pip install -e .[tests] -r requirements.txt
```

## Quick Start

Simple Bitcoin Mainnet HDWallet

```python
#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.utils import generate_entropy
from hdwallet.symbols import BTC

import json

# Choose strength
ENTROPY = generate_entropy(strength=128)
# Secret passphrase/password
PASSPHRASE = None  # str("meherett")
# Choose language
LANGUAGE = "italian"

# Initialize Bitcoin mainnet hdwallet
hdwallet = HDWallet(symbol=BTC)
# Get Bitcoin mainnet hdwallet from entropy
hdwallet.from_entropy(entropy=ENTROPY, passphrase=PASSPHRASE, language=LANGUAGE)

# Derivation from path
# hdwallet.from_path("m/44'/0'/0'/0/0")
# Or derivation from index
hdwallet.from_index(44, harden=True)
hdwallet.from_index(0, harden=True)
hdwallet.from_index(0, harden=True)
hdwallet.from_index(0)
hdwallet.from_index(0)

# Print all hdwallet information's
print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))
```

<details>
  <summary>Output</summary><br/>

```json5
{
    "cryptocurrency": "Bitcoin Mainnet",
    "symbol": "BTC",
    "entropy": "04560b263f27f1cda4d3c520d621becb",
    "mnemonic": "agave recluta selvaggio mica migliore tipografo orologio mandorla brillante registro latenza ozio",
    "language": "italian",
    "passphrase": null,
    "seed": "ed200d00a447f2ec6720f519af9168c3cca5ad451ad5b8145cf1a9111db5a99aeae2f88af6f3ac256351ec5b45e369c4e3df394028905cb7e2f1e62f41be88a0",
    "root_xprivate_key": "xprv9s21ZrQH143K2BH4fWQABcGuXb5nXh4cfDgsg7QxAHtY9M9f8qye4kCoUTaWyFCPjj4bZdXh6jjzMohpF1bnwxG63EXeRqZ8yz3WkGUt48z",
    "root_xpublic_key": "xpub661MyMwAqRbcEfMXmXwAYkDe5cvGw9nU2ScUUVpZidRX29UogPHtcYXHKjotMuaBj1WpuyPidPst12JBzGuFxYNWQcfannoUDmAQYuY3GMr",
    "xprivate_key": "xprvA3R3meuA5YxMd3SGDjQrwfmH7FkSV4TqtQL26JLhpFYGjpXtyDVzQavaQWNMAW2koqwiC37XKVtSGkARSEWa3VGALBaDzLRNHKTfhiPHpkg",
    "xpublic_key": "xpub6GQQBAS3uvWeqXWjKkwsJoi1fHavtXBhFdFctgkKNb5Fccs3WkpExPF4FoACjncQ9Rx3e6WeyBo5HSB7v2eQRyniMBVuoVkeJGiDm8hNSTK",
    "uncompressed": "95ed04c4831460ab0cb4e64d61436708a21dda1f01978b92ae8b642418f6141c2c714e28d7824d74eaf9192ec79588b55f0102c67e27c5b89f77b82a378a92e9",
    "compressed": "0395ed04c4831460ab0cb4e64d61436708a21dda1f01978b92ae8b642418f6141c",
    "chain_code": "3a0148de27a383978071d331fd847ea211d5a72a62f7bac38f033c4bc69545c8",
    "private_key": "ae1f18ba8845464e02475c723d6c0aeaf9a7211199d962aa21729568ae08185b",
    "public_key": "0395ed04c4831460ab0cb4e64d61436708a21dda1f01978b92ae8b642418f6141c",
    "wif": "L34BQg5TtVG4RvnGyyjRz9cced1uAfD9seExSqTqZTo4JJhcb3Zf",
    "identifier": "481f61f400ef924f99ea1d732b56094e806629d0",
    "finger_print": "481f61f4",
    "path": "m/44'/0'/0'/0/0",
    "address": "17aMFKH2ymx3gbrzL4wsxWQFGd5fQgJ6qX"
}
```
</details>

Ethereum Ganache-CLI/TestRPC look's like

```python
#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet  # Alias EthereumTestnet
from hdwallet.utils import generate_mnemonic

# Initialize Ethereum hdwallet
hdwallet = HDWallet(cryptocurrency=EthereumMainnet)
# Get Ethereum hdwallet from mnemonic
hdwallet.from_mnemonic(mnemonic=generate_mnemonic(language="english"), passphrase=None)

print("Mnemonic:", hdwallet.mnemonic())
print("Base HD Path:  m/44'/60'/0'/0/{address_index}", "\n")

# Get hdwallet information's from address index
for address_index in range(10):
    # Derivation from BIP44 path
    hdwallet.from_path(
        path=EthereumMainnet.BIP44_PATH.format(
            account=0, change=0, address=address_index
        )
    )
    # Print address_index, path, address and private_key
    print(f"({address_index}) {hdwallet.path()} {hdwallet.address()} 0x{hdwallet.private_key()}")
    # Clean derivation indexes
    hdwallet.clean_derivation()
```

<details>
  <summary>Output</summary><br/>

```shell script
Mnemonic: pull unhappy item bag offer maximum crumble rabbit scheme liquid behave climb
Base HD Path:  m/44'/60'/0'/0/{address_index} 

(0) m/44'/60'/0'/0/0 0x75011172e67D9dc209aE545b5fb73f3F8Bc09054 0x91ee918a47a2669336f1f20311771c6de52cc8bed422034d8f8b3ea982fa914d
(1) m/44'/60'/0'/0/1 0xA1982c3C7Db50cfA9865e2D1fc24e594207804FD 0x81f87367d09315764c3283c3790a05ec78719fd52f8bead2f43c303da8922705
(2) m/44'/60'/0'/0/2 0x0F6519d6F3940264d648F2D2Fdb1e0A7026D2318 0x585dbd37d21659e7a58e14b071f808c9bdc45cb1b4482b1db14565b2ac306e34
(3) m/44'/60'/0'/0/3 0x3e2AfDAD8cC149f63d5eABD4A57C7023D3E87E32 0x24bd0d9dfaeb6b5d041a50d8f871d151fb13be39cd21bc3dfaba921f6a79617d
(4) m/44'/60'/0'/0/4 0x001009fF0d79C92d48Dd84F0C0116E841F2fe4EB 0x5132b891dbd13d911032d6906b0382fa71d2e6a3ed373d6231d6a451c4766b45
(5) m/44'/60'/0'/0/5 0x434502aAFBD8552Bb9a91BEE977f9AFE23567FfA 0x608e0ac9da9a8271f482a1bc1e6cba6691cefa368da9cc87f4a17493b009e217
(6) m/44'/60'/0'/0/6 0x63f49D630ABB14e7A78eb1D058dF9844F93e785e 0xe1277b7e265296e846de82dfcf034b08db40850cc8481c0558784f5ab404d1d2
(7) m/44'/60'/0'/0/7 0x7596EeaB5B5D3ABF7a8Df476e72e50e931774410 0xcb308a18075a7b1c1be63e03277a61535c34a04caf8525ca5df81de49ecfdb9d
(8) m/44'/60'/0'/0/8 0xd1cA22db58eA8A7B8e62FCdBD2aB00CD59A22741 0x67bf7b55b7d3e45a5bc8f0754cb27cbbae08bb49cfcac1e97f7246429fa70181
(9) m/44'/60'/0'/0/9 0x1af6A8384aea84890783eBCe59023556C487748d 0x9c240f98a00bf4a70f76fb9cf39146fd14d0a9de8c807a5ef08640fcc49061c9
```
</details>

[Click this to see more examples](https://github.com/meherett/hdwallet/blob/master/examples).

## Testing

You can run the tests with:

```
$ pytest
```

Or use `tox` to run the complete suite against the full set of build targets, or pytest to run specific 
tests against a specific version of Python.

## License

Distributed under the [ISC](https://github.com/meherett/hdwallet/blob/master/LICENSE) license. See ``LICENSE`` for more information.
