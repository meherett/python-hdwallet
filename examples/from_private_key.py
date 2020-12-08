#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.symbols import QTUM

import json

# Qtum private key
PRIVATE_KEY: str = "f86d5afe2a457c29357485ebf853a1e5ff5f6fcf1ba4d7d1412665e01449902e"

# Initialize Qtum mainnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=QTUM)
# Get Qtum HDWallet from private key
hdwallet.from_private_key(private_key=PRIVATE_KEY)

# Print all Qtum HDWallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Network:", hdwallet.network())
print("Uncompressed:", hdwallet.uncompressed())
print("Compressed:", hdwallet.compressed())
print("Private Key:", hdwallet.private_key())
print("Public Key:", hdwallet.public_key())
print("Wallet Important Format:", hdwallet.wif())
print("Finger Print:", hdwallet.finger_print())
print("Address:", hdwallet.address())
