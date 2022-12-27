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

# Create the public and private keys associated with a new Ethereum account
private, public = wallet.derive_account('eth')

# Display the private key
private

# Create and Ethereum account by passing the private key via the Account object
account = Account.privateKeyToAccount(private)

# Print the account address associated with the Ethereum account
print(account.address)
