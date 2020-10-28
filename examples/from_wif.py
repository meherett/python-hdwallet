#!/usr/bin/env python3

from python_hdwallet import PythonHDWallet
from python_hdwallet.symbols import BTCTEST

import json

# Bitcoin wallet important format
WALLET_IMPORTANT_FORMAT: str = "cVpnZ6XRfL5VVggwZDyndAU5KGVdT2TP1j1HB3td6ZKWCbh5wYvf"

# Initialize Bitcoin testnet HDWallet
python_hdwallet: PythonHDWallet = PythonHDWallet(symbol=BTCTEST)
# Get Bitcoin HDWallet from wallet important format
python_hdwallet.from_wif(wif=WALLET_IMPORTANT_FORMAT)

# Print all Bitcoin HDWallet information's
# print(json.dumps(python_hdwallet.dumps(), indent=4, ensure_ascii=False))

print("Cryptocurrency:", python_hdwallet.cryptocurrency())
print("Symbol:", python_hdwallet.symbol())
print("Network:", python_hdwallet.network())
print("Uncompressed:", python_hdwallet.uncompressed())
print("Compressed:", python_hdwallet.compressed())
print("Private Key:", python_hdwallet.private_key())
print("Public Key:", python_hdwallet.public_key())
print("Wallet Important Format:", python_hdwallet.wif())
print("Finger Print:", python_hdwallet.finger_print())
print("Address:", python_hdwallet.address())
