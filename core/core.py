from core.objects.blockchain import Blockchain
from core.objects.block import Block
from core.utils import Utils


class Core:

    version = ""
    blockchain = None

    def __init__(self, version):
        self.version = version

    def start(self):
        self.introprint(self.version)
        self.apploop()

    def introprint(self, version):
        toprint = [
            "",
            "*****************",
            "*               *",
            "*  LEARN BLOCK  *",
            "*               *",
            "*****************",
            "Version: " + version,
            "",
            "Let's make a blockchain!",
            "",
            "(Type help to see a list of cmds)",
            "",
        ]
        Utils().printlines(toprint, True)

    def helpprint(self):
        helplist = [
            "",
            "create <or> c  -  Creates a blockchain",
            "help <or> h <or> ? - Shows this page",
            "show <or> s - Shows the blockchain",
            "showblock <or> sb - Shows a block",
            "addblock <or> ab - Adds a new block",
            "minechain <or> mc - Mines the chain",
            "mine <or> m - Mines a block",
            "quit <or> q <or> exit - Exits this app",
            "",
        ]
        Utils().printlines(helplist, False)

    def byeprint(self):
        byelist = ["", "Bye!", ""]
        Utils().printlines(byelist, False)

    def apploop(self):
        killflag = False
        while not killflag:
            cmd = input("> ")
            killflag = self.commandprocessor(cmd)
        self.byeprint()

    def createblockchain(self):
        if self.blockchain:
            linestoprint = [
                "",
                "Blockchain already created",
                "",
            ]
            Utils().printlines(linestoprint, False)
        else:
            difficulty = input("Difficulty: ")
            self.blockchain = Blockchain(difficulty)
            self.addblock(self.blockchain.getblocknumber())

    def addblock(self, blocknumber):
        block = Block()
        block.setMessage(input("Block #" + str(blocknumber) + " Message: "))
        block.setIndex(blocknumber)
        self.blockchain.addblock(block)
        print("Mining...")

    def commandprocessor(self, cmd):
        # Quit CMD
        if (cmd == "q") or (cmd == "quit") or (cmd == "exit"):
            return True

        # Help CMD
        elif (cmd == "h") or (cmd == "help"):
            self.helpprint()

        # Create CMD
        elif (cmd == "c") or (cmd == "create"):
            self.createblockchain()

        # Show cmd
        elif (cmd == "s") or (cmd == "show"):
            self.blockchain.showblockchain()

        # Add block cmd
        elif (cmd == "ab") or (cmd == "addblock"):
            self.addblock(self.blockchain.getblocknumber())

        # Show block cmd
        elif (cmd == "sb") or (cmd == "showblock"):
            self.blockchain.showblock(int(input("Block number: ")))
        # Invalid CMD
        else:
            linestoprint = [
                "",
                '"' + cmd + '" not found.',
                "",
                'type "help" for a list of commands.',
                "",
            ]
            Utils().printlines(linestoprint, False)
