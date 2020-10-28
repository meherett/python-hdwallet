#!/usr/bin/env python3

from python_hdwallet import PythonHDWallet
from python_hdwallet.cryptocurrencies import EthereumMainnet  # Alias EthereumTestnet
from python_hdwallet.utils import generate_mnemonic
from typing import Optional

# Generate english mnemonic words
MNEMONIC: str = generate_mnemonic(language="english", strength=128)
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

# Get Ethereum HDWallet information's from address index
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
