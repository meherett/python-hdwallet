#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.symbols import ETH

import json

# Ethereum xprivate key
XPRIVATE_KEY = "xprvA3KRgVDh45mbQT1VmWPx73YeAWM4629Q2D9pMuqjFMnjTqDGhKiww6H" \
               "532rgYRNj37fngd4Mvp7GfUD8rKeQzUZjCWeisT92tX8FfjWx3BL"

# Initialize Ethereum mainnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=ETH)
# Get Ethereum HDWallet from xprivate key
hdwallet.from_xprivate_key(xprivate_key=XPRIVATE_KEY)

# Print all Ethereum HDWallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Network:", hdwallet.network())
print("XPrivate Key:", hdwallet.xprivate_key())
print("XPublic Key:", hdwallet.xpublic_key())
print("Uncompressed:", hdwallet.uncompressed())
print("Compressed:", hdwallet.compressed())
print("Chain Code:", hdwallet.chain_code())
print("Private Key:", hdwallet.private_key())
print("Public Key:", hdwallet.public_key())
print("Wallet Important Format:", hdwallet.wif())
print("Finger Print:", hdwallet.finger_print())
print("Semantic:", hdwallet.semantic())
print("Path:", hdwallet.path())
print("Hash:", hdwallet.hash())
print("P2PKH Address:", hdwallet.p2pkh_address())
print("P2SH Address:", hdwallet.p2sh_address())
print("P2WPKH Address:", hdwallet.p2wpkh_address())
print("P2WPKH In P2SH Address:", hdwallet.p2wpkh_in_p2sh_address())
print("P2WSH Address:", hdwallet.p2wsh_address())
print("P2WSH In P2SH Address:", hdwallet.p2wsh_in_p2sh_address())
