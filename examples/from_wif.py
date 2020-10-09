#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.symbols import BTC

import json

# Bitcoin hdwallet important format
WALLET_IMPORTANT_FORMAT = "L5YcxkEN4Sc3L7Y8r6DzTstjdnwwhrAibU5kujeJixa8oLsAKk6Q"

# Initialize Bitcoin hdwallet
hdwallet = HDWallet(symbol=BTC)
# Get Bitcoin hdwallet from wif
hdwallet.from_wif(wif=WALLET_IMPORTANT_FORMAT)

# Print all hdwallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Uncompressed:", hdwallet.uncompressed())
print("Compressed:", hdwallet.compressed())
print("Private Key:", hdwallet.private_key())
print("Public Key:", hdwallet.public_key())
print("Wallet Important Format:", hdwallet.wif())
print("Finger Print:", hdwallet.finger_print())
print("Address:", hdwallet.address())
