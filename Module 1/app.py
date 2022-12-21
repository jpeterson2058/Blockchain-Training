#Imports

import streamlit as st
import datetime as datetime
from dataclasses import dataclass
from typing import Any, List
import pandas as pd
import datetime as datetime
import hashlib

@dataclass
class Block:
    data: Any
    creator_id: int
    prev_hash: str = 0
    timestamp: str = datetime.datetime.utcnow().strftime("%H:%M:%S")

    def hash_block(self):
        sha = hashlib.sha256()

        data = str(self.data).encode()
        sha.update(data)

        timestamp = str(self.timestamp).encode()
        sha.update(timestamp)

        prev_hash = str(self.prev_hash).encode()
        sha.update(prev_hash)

        return sha.hexdigest()

# Creating a  class called PyChain
@dataclass
class PyChain:
    chain: list[Block]

    def add_block(self, block):
        self.chain += [block]

# Streamlit code

# Adds the cache decorator for Streamlit

@st.cache(allow_output_mutation=True)
def setup():
    print("Initializing chain")
    return PyChain([Block(data="Genesis", creator_id=0)])

pychain = setup()

st.markdown("# PyChain: A Python Blockchain Application")
st.markdown("## Store Data in the Chain")

input_data = st.text_input("Block Data")

if st.button("Add Block"):
    # @TODO:
    # Select the previous block in the chain
    prev_block = pychain.chain[-1]

    # @TODO
    # Hash the previous block in the chain
    prev_block_hash = prev_block.hash_block()

    # @TODO
    # Create a block in the new chain
    new_block = Block(data="new_block", creator_id=42, prev_hash=prev_block_hash)

    # @TODO
    # Add the new block to the chain
    pychain.add_block(new_block)

st.markdown("## Pychain Ledger")

# @TODO
# Create a Pandas DataFrame to display the PyChain ledger
pychain_df = pd.DataFrame(pychain.chain)

# @TODO
# Use the streamlit write function to display the PyChaine dataframe
st.write(pychain_df)
