import time
import hashlib
from core.utils import Utils

class Block:
    index = 0
    message = ""
    timestamp = 0
    previoushash = ""
    currenthash = ""
    nonce = 0

    def __init__(self):
        self.timestamp = int(round(time.time() * 1000))

    def getIndex(self):
        return self.index

    def getMessage(self):
        return self.message

    def getPreviousHash(self):
        return self.previoushash

    def getCurrentHash(self):
        return self.currenthash

    def getNonce(self):
        return self.nonce

    def getTimeStamp(self):
        return self.timestamp

    def setIndex(self, index):
        self.index = index

    def setMessage(self, message):
        self.message = message

    def setPreviousHash(self, previoushash):
        self.previoushash = previoushash

    def mine(self, difficulty):
        mined = ""
        diffstring = ""
        self.nonce = 0
        for i in range(int(difficulty)):
            diffstring = diffstring + "0"

        while not (mined.startswith(diffstring)):
            mined = hashlib.sha256(self.compose()).hexdigest()
            self.nonce = self.nonce + 1

        self.currenthash = mined

    def compose(self):
        return ("%s,%s,%s,%s,%s" % (str(self.index), self.message, str(self.timestamp), self.previoushash, str(self.nonce))).encode('utf-8')

    def visualize(self):
        toprint = [
            "Index:          " + str(self.index),
            "Message:        " + str(self.message),
            "Timestamp:      " + str(self.timestamp),
            "Previous Hash:  " + str(self.previoushash),
            "Hash:           " + str(self.currenthash),
            "Nonce:          " + str(self.nonce)
        ]
        Utils().printlines(toprint, False)
