#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet  # Equal to EthereumTestnet
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
