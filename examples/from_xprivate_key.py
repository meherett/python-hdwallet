#!/usr/bin/env python3

from hdwallet import HDWallet as HDWallet
from hdwallet.utils import is_root_xprivate_key
from hdwallet.symbols import BTC

import json

# Strict for root xpublic key
STRICT: bool = True
# Bitcoin root xprivate key
XPRIVATE_KEY: str = "xprv9s21ZrQH143K24t96gCaezzt1QQmnqiEGm8m6TP8yb8e3TmGfkCgcLEVss" \
                    "kufMW9R4KH27pD1kyyEfJkYz1eiPwjhFzB4gtabH3PzMSmXSM"
# Bitcoin non-root xprivate key
# XPRIVATE_KEY: str = "yprvAMZNWbcSVmxMiVoKgQuKmemTpEz8dJs3v8hmgkRVUjncqkXsgoxyqZ8rDb" \
#                     "eXzMqRQZEsTcB4T5iQQx7WazLyy3KiHZrdcHo6DmGAibeMxQV"

if STRICT:
    # Check root xprivate key
    assert is_root_xprivate_key(xprivate_key=XPRIVATE_KEY, symbol=BTC), "Invalid Root XPrivate Key."

# Initialize Bitcoin mainnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=BTC)
# Get Bitcoin HDWallet from xprivate key
hdwallet.from_xprivate_key(xprivate_key=XPRIVATE_KEY, strict=STRICT)

# Derivation from path
# hdwallet.from_path("m/44'/0'/0'/0/0")
# Or derivation from index
hdwallet.from_index(44, hardened=True)
hdwallet.from_index(0, hardened=True)
hdwallet.from_index(0, hardened=True)
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
print("Semantic:", hdwallet.semantic())
print("Path:", hdwallet.path())
print("Hash:", hdwallet.hash())
print("P2PKH Address:", hdwallet.p2pkh_address())
print("P2SH Address:", hdwallet.p2sh_address())
print("P2WPKH Address:", hdwallet.p2wpkh_address())
print("P2WPKH In P2SH Address:", hdwallet.p2wpkh_in_p2sh_address())
print("P2WSH Address:", hdwallet.p2wsh_address())
print("P2WSH In P2SH Address:", hdwallet.p2wsh_in_p2sh_address())
