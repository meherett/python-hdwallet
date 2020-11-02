#!/usr/bin/env python3

from python_hdwallet import PythonHDWallet as HDWallet
from python_hdwallet.utils import generate_mnemonic, is_mnemonic
from python_hdwallet.cryptocurrencies import LitecoinMainnet

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
hdwallet: HDWallet = HDWallet(cryptocurrency=LitecoinMainnet)
# Get Litecoin HDWallet from mnemonic
hdwallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE)

# Derivation from path
hdwallet.from_path(path=LitecoinMainnet.DEFAULT_PATH)
# Or derivation from index
# hdwallet.from_index(44, harden=True)
# hdwallet.from_index(2, harden=True)
# hdwallet.from_index(0, harden=True)
# hdwallet.from_index(0)
# hdwallet.from_index(0)

# Print all Litecoin HDWallet information's
# print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", hdwallet.cryptocurrency())
print("Symbol:", hdwallet.symbol())
print("Network:", hdwallet.network())
print("Strength:", hdwallet.strength())
print("Mnemonic:", hdwallet.mnemonic())
print("Language:", hdwallet.language())
print("Passphrase:", hdwallet.passphrase())
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
print("Path:", hdwallet.path())
print("Address:", hdwallet.address())
