#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.utils import is_root_xprivate_key
from hdwallet.symbols import BTC

import json

# Bitcoin hdwallet root xprivate key
ROOT_XPRIVATE_KEY = "xprv9s21ZrQH143K24t96gCaezzt1QQmnqiEGm8m6TP8yb8e3TmGfkCgcLEVss" \
                    "kufMW9R4KH27pD1kyyEfJkYz1eiPwjhFzB4gtabH3PzMSmXSM"

# Check root xprivate key
assert is_root_xprivate_key(xprivate_key=ROOT_XPRIVATE_KEY, symbol=BTC)

# Initialize Bitcoin hdwallet
hdwallet = HDWallet(symbol=BTC)
# Get Bitcoin hdwallet from root xprivate key
hdwallet.from_root_xprivate_key(root_xprivate_key=ROOT_XPRIVATE_KEY)

# Derivation from path
# hdwallet.from_path("m/44'/0'/0'/0/0")
# Or derivation from index
hdwallet.from_index(44, harden=True)
hdwallet.from_index(0, harden=True)
hdwallet.from_index(0, harden=True)
hdwallet.from_index(0)
hdwallet.from_index(0)

# Print all hdwallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Root XPrivate Key:", hdwallet.root_xprivate_key())
print("Root XPublic Key:", hdwallet.root_xpublic_key())
print("XPrivate Key:", hdwallet.xprivate_key())
print("XPublic Key:", hdwallet.xpublic_key())
print("Uncompressed:", hdwallet.uncompressed())
print("Compressed:", hdwallet.compressed())
print("Chain Code:", hdwallet.chain_code())
print("Private Key:", hdwallet.private_key())
print("Public Key:", hdwallet.public_key())
print("Wallet Important Format:", hdwallet.wif())
print("Finger Print:", hdwallet.finger_print())
print("Path:", hdwallet.path())
print("Address:", hdwallet.address())
