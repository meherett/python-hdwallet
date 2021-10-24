#!/usr/bin/env python3

from hdwallet import HDWallet as HDWallet
from hdwallet.utils import is_root_xpublic_key
from hdwallet.symbols import BTC

import json

# Strict for root xpublic key
STRICT: bool = True
# Bitcoin root xpublic key
XPUBLIC_KEY: str = "xpub661MyMwAqRbcEqD3v24ZWHGDMqqAfbDbmnUFJXfbpxGZaAshq7evA7fB75CHFbNHSot" \
                   "LadDZw6M6ic4ZkdN6jQ2KMGR66Z2EybgdLFjNrpf"
# Bitcoin non-root xpublic key
# XPUBLIC_KEY: str = "zpub6uxKjJ8pnanQKU2betFrDPVmcVUvVgyAhgWS74iaN7yUE8RADoRRnztyVEQtnzi9Fh1Vp" \
#                    "6iJ8RT6mMqjGnS6AxGjud3P2DLzpMHUw2zT1n2"

if STRICT:
    # Check root xpublic key
    assert is_root_xpublic_key(xpublic_key=XPUBLIC_KEY, symbol=BTC), "Invalid Root XPublic Key."

# Initialize Bitcoin mainnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=BTC)
# Get Bitcoin HDWallet from xpublic key
hdwallet.from_xpublic_key(xpublic_key=XPUBLIC_KEY, strict=STRICT)

# Derivation from path
# hdwallet.from_path("m/44/0/0/0/0")
# Or derivation from index
hdwallet.from_index(44, hardened=False)
hdwallet.from_index(0, hardened=False)
hdwallet.from_index(0, hardened=False)
hdwallet.from_index(0)
hdwallet.from_index(0)

# Print all Bitcoin HDWallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Network:", hdwallet.network())
print("Root XPublic Key:", hdwallet.root_xpublic_key())
print("XPublic Key:", hdwallet.xpublic_key())
print("Uncompressed:", hdwallet.uncompressed())
print("Compressed:", hdwallet.compressed())
print("Chain Code:", hdwallet.chain_code())
print("Public Key:", hdwallet.public_key())
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
