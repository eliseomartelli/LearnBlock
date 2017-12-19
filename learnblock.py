from block import Block

def main():
    blocka = Block()
    blocka.setIndex(0)
    blocka.setMessage("HelloWorld")
    blocka.mine(5)
    blocka.visualize()

    print()

    blockb = Block()
    blockb.setIndex(1)
    blockb.setMessage("HelloWorld1")
    blockb.setPreviousHash(blocka.getCurrentHash())
    blockb.mine(5)
    blockb.visualize()

    print()

    blockc = Block()
    blockc.setIndex(2)
    blockc.setMessage("HelloWorld2")
    blockc.setPreviousHash(blockb.getCurrentHash())
    blockc.mine(5)
    blockc.visualize()


if __name__ == '__main__':
    main()
