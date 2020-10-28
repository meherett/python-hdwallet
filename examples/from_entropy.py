#!/usr/bin/env python3

from python_hdwallet import PythonHDWallet
from python_hdwallet.utils import generate_entropy
from python_hdwallet.symbols import BTC
from typing import Optional

import json

# Choose strength 128, 160, 192, 224 or 256
STRENGTH: int = 128  # Default is 128
# Choose language english, french, italian, spanish, chinese_simplified, chinese_traditional, japanese or korean
LANGUAGE: str = "korean"  # Default is english
# Generate new entropy seed
ENTROPY: str = generate_entropy(strength=STRENGTH)
# Secret passphrase/password for mnemonic
PASSPHRASE: Optional[str] = None  # str("meherett")

# Initialize Bitcoin hdwallet
python_hdwallet: PythonHDWallet = PythonHDWallet(symbol=BTC)
# Get Bitcoin hdwallet from entropy
python_hdwallet.from_entropy(
    entropy=ENTROPY, passphrase=PASSPHRASE, language=LANGUAGE
)

# Derivation from path
# python_hdwallet.from_path("m/44'/0'/0'/0/0")
# Or derivation from index
python_hdwallet.from_index(44, harden=True)
python_hdwallet.from_index(0, harden=True)
python_hdwallet.from_index(0, harden=True)
python_hdwallet.from_index(0)
python_hdwallet.from_index(0)

# Print all Bitcoin hdwallet information's
# print(json.dumps(python_hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", python_hdwallet.cryptocurrency())
print("Symbol:", python_hdwallet.symbol())
print("Network:", python_hdwallet.network())
print("Entropy:", python_hdwallet.entropy())
print("Mnemonic:", python_hdwallet.mnemonic())
print("Language:", python_hdwallet.language())
print("Passphrase:", python_hdwallet.passphrase())
print("Seed:", python_hdwallet.seed())
print("Root XPrivate Key:", python_hdwallet.root_xprivate_key())
print("Root XPublic Key:", python_hdwallet.root_xpublic_key())
print("XPrivate Key:", python_hdwallet.xprivate_key())
print("XPublic Key:", python_hdwallet.xpublic_key())
print("Uncompressed:", python_hdwallet.uncompressed())
print("Compressed:", python_hdwallet.compressed())
print("Chain Code:", python_hdwallet.chain_code())
print("Private Key:", python_hdwallet.private_key())
print("Public Key:", python_hdwallet.public_key())
print("Wallet Important Format:", python_hdwallet.wif())
print("Finger Print:", python_hdwallet.finger_print())
print("Path:", python_hdwallet.path())
print("Address:", python_hdwallet.address())
