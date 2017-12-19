class Utils:

    def __init__(self):
        pass

    def printlines(self, linestoprint, center):
        for line in linestoprint:
            if center:
                line = line.center(80, " ")
            print(line)
