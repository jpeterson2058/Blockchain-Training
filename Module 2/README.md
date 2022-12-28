# My Blockchain Journey...continued


## Module 2

### Intro to Web3

Output from ethereumTester

['0xaBbACadABa000000000000000000000000000000', 
'0xaBbACaDaBA000000000000000000000000000001', 
'0xAbbAcaDaBA000000000000000000000000000002', 
'0xabBACadaBA000000000000000000000000000003', 
'0xabbAcADABa000000000000000000000000000004', 
'0xaBBACADABA000000000000000000000000000005', 
'0xaBbaCadaBA000000000000000000000000000006', 
'0xAbbAcAdaBA000000000000000000000000000007', 
'0xaBBAcadabA000000000000000000000000000008', 
'0xABbacaDabA000000000000000000000000000009']

/Users/joshuapeterson/opt/anaconda3/lib/python3.9/site-packages/eth_tester/backends/__init__.py:30: UserWarning: Ethereum Tester: No backend was explicitely set, and no *full* backends were available.  Falling back to the `MockBackend` which does not support all EVM functionality.  Please refer to the `eth-tester` documentation for information on what backends are available and how to set them.
  warnings.warn(UserWarning(

Decimal('1000000')

### Create an Ethereum Account

Output from the createEthAcct.py

'elbow scale copper retreat surface jungle ocean bright square trap wage punch'

### Create an Etherum Wallet

Output from generateWallet.py

<bip44.wallet.Wallet at 0x7f82cbe5adc0>

### Create a Public/Private Key in the Ethereum Account

Byte string

b'\xb0\xe8\x90v\x91\xcc\xbb\xbd\xb4\xd9%wH\x8a\xeb\xb6\x99\xfb\xa2\x1a\xbbv\x80Cs\xb2)\xe5\xd8\xd9\xb3\xe7'

### Create an Ethereum account by passing the private key to the account.  Here is the private key asssociated with the account.

0x9C6a38d5ab0b6BE3018187d659DdC04798147E42

### Message encoding and verification

Signed message

SignedMessage(messageHash=HexBytes('0x99da6da72447cf6e4e2d8ddfbd1a82457b584a9a507fbae974224e8ea85c4104'), r=46179275551383848529172213639480647748845273192290953692694751245883116945279, s=44943390202801640355685456852612466241580251862361697753709219274890365328817, v=28, signature=HexBytes('0x66188b31184646ce9eadd27a9973f622e8385d793ccefdf70f4ba8d13cc0ff7f635d0eb1bad1f863cb10927591b6128306d809c75b1941f982f1a51c49f75db11c'))

Validation of the transaction againt public key.

'0x9C6a38d5ab0b6BE3018187d659DdC04798147E42'

### Sign and send a Transaction on Ganache

We can see that the address ending in 9F2F has a balance of 101 ETH were previously it had 100.

![84862A3F-A187-499C-88BB-71002D276C51](https://user-images.githubusercontent.com/16564975/209882900-e512d74f-3aae-4ac5-b060-0f21480ab181.jpeg)

