import hashlib
import json
from time import time
from hash import generateHash

class Block:
    # Create initializer method that taskes index, timestamp, transaction and previousHash
    
        # Save the received arguments in the object variables
    
        # Call calculateHash method and save result in currentHash object variable
    
       
    def calculateHash(self, timestamp=None):
        if(timestamp == None):
            timestamp = self.timestamp

        blockString = str(self.index) + str(timestamp) + str(self.previousHash) + json.dumps(self.transaction)
        return generateHash(blockString)

       
