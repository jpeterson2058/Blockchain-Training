# Imports
from dataclasses import dataclass
from datetime import datetime
from typing import Any

# Creating the Block data class
@dataclass
class Block:
    data: str
    creator_id: int
    timestamp: str = datetime.utcnow().strftime("%H:%M:%S")

# Creating a new block
new_block = Block(data="My First Block", creator_id=42)
print(new_block)  
