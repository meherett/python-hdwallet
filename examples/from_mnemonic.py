#!/usr/bin/env python3

from hdwallet import HDWallet
from hdwallet.utils import generate_mnemonic, is_mnemonic

import json

# HDWallet 12 word mnemonic
MNEMONIC = "병아리 실컷 여인 축제 극히 저녁 경찰 설사 할인 해물 시각 자가용"
# Or generate mnemonic by choose language and strength 128, 160, 192, 224 or 256
# MNEMONIC = generate_mnemonic(language="korean", strength=128)
# Secret passphrase/password
PASSPHRASE = None  # str("meherett")
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
LANGUAGE = "korean"  # default is english

# Checking mnemonic words
assert is_mnemonic(mnemonic=MNEMONIC, language=LANGUAGE), f"Invalid {LANGUAGE} mnemonic."

# Initialize hdwallet
hdwallet = HDWallet()
# Get Bitcoin hdwallet from mnemonic
hdwallet.from_mnemonic(mnemonic=MNEMONIC, passphrase=PASSPHRASE, language=LANGUAGE)

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
