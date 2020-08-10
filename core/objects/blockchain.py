class Blockchain:
    difficulty = 0
    chain = []
    def __init__(self, difficulty):
        self.difficulty = difficulty
    def addblock(self, block):
        if block.index > 0:
            block.setPreviousHash(self.chain[len(self.chain) -1].getCurrentHash())
        self.chain.append(block)
        self.mineblock(len(self.chain) - 1)


    def getblocknumber(self):
        return len(self.chain)

    def showblock(self, blocknumber):
        print()
        self.chain[blocknumber].visualize()
        print()

    def showblockchain(self):
        print()
        for block in self.chain:
            block.visualize()
            print()

    def mineblock(self, blocknumber):
        self.chain[blocknumber].mine(self.difficulty)
