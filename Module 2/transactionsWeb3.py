#Import the Web3 Library
from web3 import Web3

# Import the RPC Provider
from web3 import EthereumTesterProvider

#Create an instance of Web3
w3 = Web3()

# Create an instance of the EthereumTesterProvider
provider = EthereumTesterProvider()

#Update the Web3 instance to include the provider
w3 = Web3(provider)

# Access a list of accounts on the blockchain
w3.eth.accounts

# Set the sender address
sender = ("0xaBbACadABa000000000000000000000000000000")

# Set the receiver address
receiver = ("0xaBbACaDaBA000000000000000000000000000001")

# Set the units of gas
gas = 21,000

# Convert balance from ether to wei
value = w3.toWei(200,"ether")

# Send the transaction to the blockchain
w3.eth.send_transaction({'to': receiver, 'from': sender, 'gas': gas, 'value': value})
