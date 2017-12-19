global chain
chain = False


def main():
    introprint()
    cmdloop()

def cmdloop():
    kflag = False
    while not kflag:
        cmd = input("> ")
        kflag = cmdprocessor(cmd)
    byeprint()

def byeprint():
    print()
    print("Bye.")
    print()

def helpprint():
    helplist = [
        "create <or> c  -  Creates a blockchain",
        "help <or> h <or> ? - Shows this page",
        "show <or> s - Shows the blockchain",
        "showblock <or> sb - Shows a block",
        "addblock <or> ab - Adds a new block",
        "minechain <or> mc - Mines the chain",
        "quit <or> q <or> exit - Exits this app"
    ]
    print()
    for entry in helplist:
        print("\t" + entry)
    print()

def notdefindedprint(cmd):
    print()
    print("\"" + str(cmd) + "\" not defined")
    print()
    print("type help to see a list of cmds")
    print()

def cmdprocessor(cmd):
    if (cmd == "help" or cmd == "h" or cmd == "?"):
        helpprint()

    elif (cmd == "minechain" or cmd == "mc"):
        chain.mine()

    elif (cmd == "create" or cmd == "c"):
        createchain()

    elif (cmd == "show" or cmd == "s"):
        chain.show()

    elif (cmd == "showblock" or cmd == "sb"):
        pass


    elif (cmd == "addblock" or cmd == "ab"):
        chain.addblock(Block())

    elif (cmd == "quit" or cmd == "q" or cmd == "exit"):
        return True

    else:
        notdefindedprint(cmd)

def createchain():
    global chain
    if chain:
        print("You've already a blockchain...")
    else:
        print("Let's start!")
        print()
        difficulty = input("Difficulty: ")
        chain = Blockchain(difficulty)
        print()
        print("Blockchain created.")
        print()
        chain.addblock(Block())


def firstblock(chain):
    pass
