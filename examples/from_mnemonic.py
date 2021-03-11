#!/usr/bin/env python3

from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import LitecoinMainnet as Cryptocurrency
from hdwallet.utils import generate_mnemonic, is_mnemonic

import json

# Choose strength 128, 160, 192, 224 or 256
STRENGTH: int = 160  # Default is 128
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
LANGUAGE: str = "italian"  # Default is english
# Generate new mnemonic words
MNEMONIC: str = generate_mnemonic(language=LANGUAGE, strength=STRENGTH)
# Secret passphrase/password for mnemonic
PASSPHRASE: str = "meherett"

# Check mnemonic words
assert is_mnemonic(mnemonic=MNEMONIC, language=LANGUAGE)

# Initialize Litecoin mainnet HDWallet
bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(
    cryptocurrency=Cryptocurrency, account=0, change=False, address=0
)
# Get Litecoin HDWallet from mnemonic
bip44_hdwallet.from_mnemonic(
    mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE
)

# Print all Litecoin HDWallet information's
# print(json.dumps(bip44_hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", bip44_hdwallet.cryptocurrency())
print("Symbol:", bip44_hdwallet.symbol())
print("Network:", bip44_hdwallet.network())
print("Strength:", bip44_hdwallet.strength())
print("Entropy:", bip44_hdwallet.entropy())
print("Mnemonic:", bip44_hdwallet.mnemonic())
print("Language:", bip44_hdwallet.language())
print("Passphrase:", bip44_hdwallet.passphrase())
print("Seed:", bip44_hdwallet.seed())
print("Root XPrivate Key:", bip44_hdwallet.root_xprivate_key())
print("Root XPublic Key:", bip44_hdwallet.root_xpublic_key())
print("XPrivate Key:", bip44_hdwallet.xprivate_key())
print("XPublic Key:", bip44_hdwallet.xpublic_key())
print("Uncompressed:", bip44_hdwallet.uncompressed())
print("Compressed:", bip44_hdwallet.compressed())
print("Chain Code:", bip44_hdwallet.chain_code())
print("Private Key:", bip44_hdwallet.private_key())
print("Public Key:", bip44_hdwallet.public_key())
print("Wallet Important Format:", bip44_hdwallet.wif())
print("Finger Print:", bip44_hdwallet.finger_print())
print("Semantic:", bip44_hdwallet.semantic())
print("Path:", bip44_hdwallet.path())
print("Hash:", bip44_hdwallet.hash())
print("P2PKH Address:", bip44_hdwallet.p2pkh_address())
print("P2SH Address:", bip44_hdwallet.p2sh_address())
print("P2WPKH Address:", bip44_hdwallet.p2wpkh_address())
print("P2WPKH In P2SH Address:", bip44_hdwallet.p2wpkh_in_p2sh_address())
print("P2WSH Address:", bip44_hdwallet.p2wsh_address())
print("P2WSH In P2SH Address:", bip44_hdwallet.p2wsh_in_p2sh_address())
