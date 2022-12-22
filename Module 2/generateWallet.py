# Imports

import os
from dotenv import load_dotenv
load_dotenv()
from mnemonic import Mnemonic
from bip44 import Wallet
from web3 import Account

# Load the value of the MNEMONIC variable from the .env file
mnemonic = os.getenv("MNEMONIC")

# Evaluate the contents of the mnemonic variable
#Create a new mnemonic seed phrase if the value of mneominc equals NONE
if mnemonic is None:
    mnemo = Mnemonic("english")
    mnemonic = mnemo.generate(strength=128)

# Display the value of the mnemonic variable
display(mnemonic)

# Generate a wallet
wallet = Wallet(mnemonic)
wallet
