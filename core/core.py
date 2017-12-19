from core.objects.blockchain import Blockchain
from core.objects.block import Block
from core.utils import Utils

class Core:

    version = ""
    utils = None

    def __init__(self, version):
        self.version = version
        self.utils = Utils()

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
            ""
        ]
        self.utils.printlines(toprint, True)

    def helpprint(self):
        helplist = [
            "",
            "create <or> c  -  Creates a blockchain",
            "help <or> h <or> ? - Shows this page",
            "show <or> s - Shows the blockchain",
            "showblock <or> sb - Shows a block",
            "addblock <or> ab - Adds a new block",
            "minechain <or> mc - Mines the chain",
            "quit <or> q <or> exit - Exits this app",
            ""
        ]
        self.utils.printlines(helplist, False)

    def byeprint(self):
        byelist = [
            "",
            "Bye!",
            ""
        ]
        self.utils.printlines(byelist, False)

    def apploop(self):
        killflag = False
        while not killflag:
            cmd = input("> ")
            killflag = self.commandprocessor(cmd)
        self.byeprint()

    def commandprocessor(self, cmd):
        # Quit CMD
        if (cmd == "q") or (cmd == "quit") or (cmd == "exit"):
            return True
        # Help CMD
        elif (cmd == "h") or (cmd == "help"):
            self.helpprint()
        # Invalid CMD
        else:
            linestoprint = [
                "",
                "\"" + cmd + "\" not found.",
                "",
                "type \"help\" for a list of commands.",
                ""
            ]
            self.utils.printlines(linestoprint, False)
