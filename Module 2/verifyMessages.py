# Imports

import os
from dotenv import load_dotenv
load_dotenv()
from mnemonic import Mnemonic
from bip44 import Wallet
from web3 import Account
from web3.auto import w3
from eth_account.messages import encode_defunct

# Our existing mnemonic phrase
mnemonic = 'elbow scale copper retreat surface jungle ocean bright square trap wage punch'

# Associating our wallet with the mnemonic phrase
wallet = Wallet(mnemonic)
wallet

# Create the public and private keys associated with a new Ethereum account
private, public = wallet.derive_account('eth')

# Create a message

msg = "Rollo owes William $100"

# Next we will encode our message from text format into a byte format.

message = encode_defunct(text=msg)

# Next we will use the w3.eth.account.sign_message to sign the message to make it legit
signed_message = w3.eth.account.sign_message(message, private_key=private)
signed_message

# Finally, we will validate the transaction's signature against my public key
w3.eth.account.recover_message(message, signature=signed_message.signature)
