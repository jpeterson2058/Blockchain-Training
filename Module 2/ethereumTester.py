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

# Access information for the most recent block
w3.eth.get_block("latest")

# Print a list of accounts on the blockchain
print(w3.eth.accounts)

# Access the balance of an account using the address

balance = w3.eth.get_balance("0xaBbACadABa000000000000000000000000000000")

# Convert balance from wei to ether
w3.fromWei(balance, "ether")
