#!/usr/bin/env python3

from python_hdwallet import PythonHDWallet
from python_hdwallet.symbols import QTUM

import json

# Qtum private key
PRIVATE_KEY: str = "f86d5afe2a457c29357485ebf853a1e5ff5f6fcf1ba4d7d1412665e01449902e"

# Initialize Qtum mainnet HDWallet
python_hdwallet: PythonHDWallet = PythonHDWallet(symbol=QTUM)
# Get Qtum HDWallet from private key
python_hdwallet.from_private_key(private_key=PRIVATE_KEY)

# Print all Qtum HDWallet information's
# print(json.dumps(python_hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", python_hdwallet.cryptocurrency())
print("Symbol:", python_hdwallet.symbol())
print("Network:", python_hdwallet.network())
print("Uncompressed:", python_hdwallet.uncompressed())
print("Compressed:", python_hdwallet.compressed())
print("Private Key:", python_hdwallet.private_key())
print("Public Key:", python_hdwallet.public_key())
print("Wallet Important Format:", python_hdwallet.wif())
print("Finger Print:", python_hdwallet.finger_print())
print("Address:", python_hdwallet.address())
