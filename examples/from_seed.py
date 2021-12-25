#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.symbols import DOGE as SYMBOL

import json

# Mnemonic words seed
SEED: str = "b3337a2fe409afbb257b504e4c09d36b57c32c452b71a0ed413298a5172f727a06bf660548" \
            "8723bc545a4bd51f5cd29a3e8bd1433bd1d26e6bf866ff53d1493f"

# Initialize Dogecoin mainnet HDWallet
hdwallet: HDWallet = HDWallet(symbol=SYMBOL)
# Get Dogecoin HDWallet from seed
hdwallet.from_seed(seed=SEED)

# Derivation from path
# hdwallet.from_path("m/44'/3'/0'/0/0")
# Or derivation from index
hdwallet.from_index(44, hardened=True)
hdwallet.from_index(3, hardened=True)
hdwallet.from_index(0, hardened=True)
hdwallet.from_index(0)
hdwallet.from_index(0)

# Print all Dogecoin HDWallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Network:", hdwallet.network())
print("Seed:", hdwallet.seed())
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
