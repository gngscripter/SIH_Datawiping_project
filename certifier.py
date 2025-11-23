import hashlib
import datetime
from pymongo import MongoClient

class WipeCertifier:
    def __init__(self, db_name="wipe_chain", collection="certificates"):
        
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection]

        
        if self.collection.count_documents({}) == 0:
            self._create_genesis_block()

    def _create_genesis_block(self):
        """Creates the first block in the chain (genesis)."""
        genesis_data = {
            "index": 0,
            "timestamp": str(datetime.datetime.utcnow()),
            "event": "Genesis Block",
            "prev_hash": "0" * 64
        }
        genesis_data["hash"] = self._compute_hash(genesis_data)
        self.collection.insert_one(genesis_data)

    def _compute_hash(self, data):
        """Computes SHA256 hash of a block's content."""
        block_string = f"{data['index']}{data['timestamp']}{data['event']}{data['prev_hash']}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_certificate(self, event_msg):
        """Adds a new wipe event to the chain."""
        last_block = self.collection.find_one(sort=[("index", -1)])
        new_index = last_block["index"] + 1
        prev_hash = last_block["hash"]

        new_block = {
            "index": new_index,
            "timestamp": str(datetime.datetime.utcnow()),
            "event": event_msg,
            "prev_hash": prev_hash
        }
        new_block["hash"] = self._compute_hash(new_block)

        self.collection.insert_one(new_block)
        return new_block

    def verify_chain(self):
        """Verifies the integrity of the entire chain."""
        chain = list(self.collection.find().sort("index", 1))
        for i in range(1, len(chain)):
            prev = chain[i - 1]
            curr = chain[i]

            
            if curr["prev_hash"] != prev["hash"]:
                return False
            if curr["hash"] != self._compute_hash(curr):
                return False
        return True
