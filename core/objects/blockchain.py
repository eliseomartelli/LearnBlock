from core.objects.block import Block

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

    def checkchain(self):
        prevhash = ""
        chainbroken = False
        for block in self.chain:
            chainbroken = block.getPreviousHash() != prevhash
            prevhash = block.getCurrentHash()
            if chainbroken:
                print("Chain broken at block index: " + str(block.getIndex() - 1))
                break

    def editblock(self, blocknumber):
        self.chain[blocknumber].setMessage(input("Message: "))
        self.chain[blocknumber].mine(self.difficulty)


    def remine(self):
        for block, index in zip(self.chain, range(0, len(self.chain))):
            if index > 0:
                block.setPreviousHash(self.chain[index-1].getCurrentHash())
            block.mine(self.difficulty)

    def showblockchain(self):
        print()
        for block in self.chain:
            block.visualize()
            print()

    def mineblock(self, blocknumber):
        self.chain[blocknumber].mine(self.difficulty)
