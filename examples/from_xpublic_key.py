#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.symbols import ETH

import json

# Ethereum xpublic key
XPUBLIC_KEY = "xpub6GYVAAuBNfDxWKfSoNPR262M6uW7wWTuxE6LLRtgdBZkvmgzWFGhk41NKHydAxa" \
              "6RMZP3pY2318KG4iUfZa22nUA4q8hfrqhrDpBUJcfvWu"

# Initialize Ethereum mainnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=ETH)
# Get Ethereum HDWallet from xpublic key
hdwallet.from_xpublic_key(xpublic_key=XPUBLIC_KEY)

# Print all Ethereum HDWallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Network:", hdwallet.network())
print("XPublic Key:", hdwallet.xpublic_key())
print("Uncompressed:", hdwallet.uncompressed())
print("Compressed:", hdwallet.compressed())
print("Chain Code:", hdwallet.chain_code())
print("Public Key:", hdwallet.public_key())
print("Finger Print:", hdwallet.finger_print())
print("Semantic:", hdwallet.semantic())
print("Hash:", hdwallet.hash())
print("P2PKH Address:", hdwallet.p2pkh_address())
print("P2SH Address:", hdwallet.p2sh_address())
print("P2WPKH Address:", hdwallet.p2wpkh_address())
print("P2WPKH In P2SH Address:", hdwallet.p2wpkh_in_p2sh_address())
print("P2WSH Address:", hdwallet.p2wsh_address())
print("P2WSH In P2SH Address:", hdwallet.p2wsh_in_p2sh_address())
