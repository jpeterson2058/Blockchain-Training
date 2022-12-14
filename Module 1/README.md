# My Blockchain Journey - By Joshua Peterson

## Module 1

### Now I know how to use Streamlit...awesome!

![Image 12-20-22 at 4 13 PM](https://user-images.githubusercontent.com/16564975/208784248-5bdb875d-4d65-4be3-865f-d829725a9f4e.jpg)

### Creating a Blockchain Block with a Python Data Class

A class offers a way to define a custom data structure in Python. We can use a class to store multiple variables, known as attributes when they exist in a class. Python has a special type of class, called a data class, that we can use to define and store data.

The following is the output from our dataClass.py file:

Block(data='My First Block', creator_id=42, timestamp='23:48:30')

### Encode the Data with a Hashing Function

The output or hash, from the encoded data is

3be30ac34e6ec3bfed48e8cfe38b052783a2202d818bfe996e8838674fa098a5

### Adding Hashing to the Block Data Class

The output from the code is:

Block(data='test', creator_id=42, timestamp='00:36:00')
7878e2834f85bd24a5e6ac7ae83556d32e77999e3cbd51f150de744e1586f23d

### Chaining Blocks

The output from the code is:

PyChain(chain=[Block(data='Genesis', creator_id=0, prev_hash='0', timestamp='01:09:48'), Block(data='new_block', creator_id=42, prev_hash='a794451d3dc3d49c2debba2ed2f3214fffe5c09e89c760a42761f6d1f7cb03f3', timestamp='01:09:48')])

### Blockchain Application

Output from the Streamlit blockchain application

![92A43F57-2863-4497-A1DF-18CAF7CD1C2A](https://user-images.githubusercontent.com/16564975/208973094-38d9682d-4694-409c-b549-92ab6397984d.jpeg)

### Dynamic Difficulty

Output from the Streamlit blockchain application

![58FCDED1-E15F-4398-A3C6-721930CB6F67](https://user-images.githubusercontent.com/16564975/208994581-c1f71b0e-0d7e-4702-a11a-689b174d9bdc.jpeg)

### Validating the Blockchain

Output from the Streamlit blockchain application

![4FBC1278-9B56-4F80-9604-336F4147E0EF](https://user-images.githubusercontent.com/16564975/209204490-8fbd2196-a28d-436b-a5d8-c51fc7edbb72.jpeg)

