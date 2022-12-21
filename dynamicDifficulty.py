#Imports

import streamlit as st
import datetime as datetime
from dataclasses import dataclass
from typing import Any, List
import pandas as pd
import hashlib

@dataclass
class Block:
    data: Any
    creator_id: int
    prev_hash: str = 0
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")
    prev_hash: str = 0
    nonce: int = 0

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        creator_id = str(self.creator_id).encode()

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        sha.update(data)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        nonce = str(self.nonce).encode()
        sha.update(nonce)

        return sha.hexdigest()

# Creating a  class called PyChain
@dataclass
class PyChain:
    chain: list[Block]
    difficulty: int = 4

    def proof_of_work(self,block):
        calculated_hash = block.hash_block()

        num_of_zeros = "0" * self.difficulty

        while not calculated_hash.startswith(num_of_zeros):
            block.nonce += 1
            calculated_hash = block.hash_block()

        print("Winning Hash", calculated_hash)
        return block        

    def add_block(self, candidate_block):
        block = self.proof_of_work(candidate_block)
        self.chain += [block]

# Streamlit code

# Adds the cache decorator for Streamlit

@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing chain")
    return PyChain([Block(data="Genesis", creator_id=0)])

pychain = setup()

st.markdown("# PyChain")
st.markdown("## Store Data in the Chain")

# Add a Streamlit slider named "Block Difficulty" that allows the user to update a difficulty value.  Set this equal to the variable "difficulty 1,5,4"
difficulty = st.sidebar.slider("Block Difficulty", 1, 5, 4)

# Update the difficulty data attribute of the Pychain data class (pychain.difficulty) with the new difficulty value
pychain.difficulty = difficulty

input_data = st.text_input("Block Data")

if st.button("Add Block"):
    # Select the previous block in the chain
    prev_block = pychain.chain[-1]
    prev_block_hash = prev_block.hash_block()

    new_block = Block(data="new_block", creator_id=42, prev_hash=prev_block_hash)

    pychain.add_block(new_block)

    st.write("Winning Hash", new_block.hash_block())

st.markdown("## Pychain Ledger")
pychain_df = pd.DataFrame(pychain.chain)

st.write(pychain_df)        
