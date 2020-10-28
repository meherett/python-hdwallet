#!/usr/bin/env python3

from python_hdwallet import PythonHDWallet
from python_hdwallet.symbols import ETH

import json

# Ethereum xprivate key
XPRIVATE_KEY = "xprvA3KRgVDh45mbQT1VmWPx73YeAWM4629Q2D9pMuqjFMnjTqDGhKiww6H" \
               "532rgYRNj37fngd4Mvp7GfUD8rKeQzUZjCWeisT92tX8FfjWx3BL"

# Initialize Ethereum mainnet HDWallet
python_hdwallet: PythonHDWallet = PythonHDWallet(symbol=ETH)
# Get Ethereum HDWallet from xprivate key
python_hdwallet.from_xprivate_key(xprivate_key=XPRIVATE_KEY)

# Print all Ethereum HDWallet information's
print(json.dumps(python_hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", python_hdwallet.cryptocurrency())
print("Symbol:", python_hdwallet.symbol())
print("Network:", python_hdwallet.network())
print("XPrivate Key:", python_hdwallet.xprivate_key())
print("XPublic Key:", python_hdwallet.xpublic_key())
print("Uncompressed:", python_hdwallet.uncompressed())
print("Compressed:", python_hdwallet.compressed())
print("Chain Code:", python_hdwallet.chain_code())
print("Private Key:", python_hdwallet.private_key())
print("Public Key:", python_hdwallet.public_key())
print("Wallet Important Format:", python_hdwallet.wif())
print("Finger Print:", python_hdwallet.finger_print())
print("Address:", python_hdwallet.address())
