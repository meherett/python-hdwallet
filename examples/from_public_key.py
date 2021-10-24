#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.symbols import ETH

import json

# Ethereum public key
PUBLIC_KEY = "034f6922d19e8134de23eb98396921c02cdcf67e8c0ff23dfd955839cd557afd10"

# Initialize Ethereum mainnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=ETH)
# Get Ethereum HDWallet from public key
hdwallet.from_public_key(public_key=PUBLIC_KEY)

# Print all Ethereum HDWallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Network:", hdwallet.network())
print("Uncompressed:", hdwallet.uncompressed())
print("Compressed:", hdwallet.compressed())
print("Public Key:", hdwallet.public_key())
print("Finger Print:", hdwallet.finger_print())
print("Hash:", hdwallet.hash())
print("P2PKH Address:", hdwallet.p2pkh_address())
print("P2SH Address:", hdwallet.p2sh_address())
print("P2WPKH Address:", hdwallet.p2wpkh_address())
print("P2WPKH In P2SH Address:", hdwallet.p2wpkh_in_p2sh_address())
print("P2WSH Address:", hdwallet.p2wsh_address())
print("P2WSH In P2SH Address:", hdwallet.p2wsh_in_p2sh_address())
