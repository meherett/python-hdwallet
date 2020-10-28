#!/usr/bin/env python3

from python_hdwallet import PythonHDWallet as HDWallet
from python_hdwallet.utils import is_root_xprivate_key
from python_hdwallet.symbols import BTC

import json

# Bitcoin root xprivate key
ROOT_XPRIVATE_KEY: str = "xprv9s21ZrQH143K24t96gCaezzt1QQmnqiEGm8m6TP8yb8e3TmGfkCgcLEVss" \
                         "kufMW9R4KH27pD1kyyEfJkYz1eiPwjhFzB4gtabH3PzMSmXSM"

# Check root xprivate key
assert is_root_xprivate_key(xprivate_key=ROOT_XPRIVATE_KEY, symbol=BTC)

# Initialize Bitcoin mainnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=BTC)
# Get Bitcoin HDWallet from root xprivate key
hdwallet.from_root_xprivate_key(root_xprivate_key=ROOT_XPRIVATE_KEY)

# Derivation from path
# hdwallet.from_path("m/44'/0'/0'/0/0")
# Or derivation from index
hdwallet.from_index(44, harden=True)
hdwallet.from_index(0, harden=True)
hdwallet.from_index(0, harden=True)
hdwallet.from_index(0)
hdwallet.from_index(0)

# Print all Bitcoin HDWallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Network:", hdwallet.network())
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
