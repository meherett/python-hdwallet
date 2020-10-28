#!/usr/bin/env python3

from python_hdwallet import PythonHDWallet
from python_hdwallet.symbols import DOGE

import json

# Mnemonic words seed
SEED: str = "b3337a2fe409afbb257b504e4c09d36b57c32c452b71a0ed413298a5172f727a06bf660548" \
            "8723bc545a4bd51f5cd29a3e8bd1433bd1d26e6bf866ff53d1493f"

# Initialize Dogecoin mainnet HDWallet
python_hdwallet: PythonHDWallet = PythonHDWallet(symbol=DOGE)
# Get Dogecoin HDWallet from seed
python_hdwallet.from_seed(seed=SEED)

# Derivation from path
# python_hdwallet.from_path("m/44'/3'/0'/0/0")
# Or derivation from index
python_hdwallet.from_index(44, harden=True)
python_hdwallet.from_index(3, harden=True)
python_hdwallet.from_index(0, harden=True)
python_hdwallet.from_index(0)
python_hdwallet.from_index(0)

# Print all Dogecoin HDWallet information's
# print(json.dumps(python_hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", python_hdwallet.cryptocurrency())
print("Symbol:", python_hdwallet.symbol())
print("Network:", python_hdwallet.network())
print("Seed:", python_hdwallet.seed())
print("Root XPrivate Key:", python_hdwallet.root_xprivate_key())
print("Root XPublic Key:", python_hdwallet.root_xpublic_key())
print("XPrivate Key:", python_hdwallet.xprivate_key())
print("XPublic Key:", python_hdwallet.xpublic_key())
print("Uncompressed:", python_hdwallet.uncompressed())
print("Compressed:", python_hdwallet.compressed())
print("Chain Code:", python_hdwallet.chain_code())
print("Private Key:", python_hdwallet.private_key())
print("Public Key:", python_hdwallet.public_key())
print("Wallet Important Format:", python_hdwallet.wif())
print("Finger Print:", python_hdwallet.finger_print())
print("Path:", python_hdwallet.path())
print("Address:", python_hdwallet.address())
