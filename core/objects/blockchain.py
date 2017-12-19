from core.objects.block import Block

class Blockchain:
    difficulty = 0
    chain = []
    def __init__(self, difficulty):
        self.difficulty = difficulty
    def addblock(self, block):
        self.chain.append(block)

    def getblocknumber(self):
        if self.chain:
            return len(self.chain)
        else:
            return 0
    def showblockchain(self):
        print ""
        for block in self.chain:
            block.visualize()
            print ""

    def mineblock(self, blocknumber):
        if (blocknumber > 0):
            self.chain[blocknumber].setPreviousHash(chain[blocknumber - 1].getCurrentHash())
        self.chain[blocknumber].mine(self.difficulty)
