import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
        self.mining_time = 0  # To store mining duration

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        start_time = time.time()

        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

        end_time = time.time()
        self.mining_time = end_time - start_time

    def __str__(self):
        return (
            f"Block #{self.index} mined ✅\n"
            f"Data            : {self.data}\n"
            f"Hash            : {self.hash}\n"
            f"Nonce Attempts  : {self.nonce}\n"
            f"Time Taken      : {self.mining_time:.4f} seconds\n"
            "----------------------------------------"
        )

def create_genesis_block(difficulty):
    block = Block(0, time.ctime(), "Genesis Block", "0")
    block.mine_block(difficulty)
    return block

def create_next_block(previous_block, data, difficulty):
    block = Block(previous_block.index + 1, time.ctime(), data, previous_block.hash)
    block.mine_block(difficulty)
    return block

# Run the simulation
difficulty = 4
blockchain = [create_genesis_block(difficulty)]
blockchain.append(create_next_block(blockchain[-1], "Second block data", difficulty))
blockchain.append(create_next_block(blockchain[-1], "Third block data", difficulty))

# Output results
for block in blockchain:
    print(block)
