import re

class Claim:

    def __init__(self, line):
        #  #ID @ distanceFromLeft,distanceFromTop: width x height
        # id @ x, y, width x height
        pattern = "^(.*?) @ (.*?),(.*?): (.*?)x(.*?)$"
        result = re.search(pattern, line)

        self.id = result.group(1)
        self.x = int(result.group(2))
        self.y = int(result.group(3))
        self.width = int(result.group(4))
        self.height = int(result.group(5))
        self.coordinates = self.createCoordinates(self.x, self.y, self.width, self.height)

    def createCoordinates(self, x, y, width, height):
        calculatedCoordinates = set()
        for i in range(x, x+width):
            for j in range(y, y+height):
                calculatedCoordinates.add(str(i) + "," + str(j))

        self.coordinates = calculatedCoordinates
        return calculatedCoordinates

class ThirdDay:

    def firstPart(self, inputFilePath):
        # I have a bunch of claims and I need the overlapping points
        # I calculate the coordinates for each suit and check, if they're already in the set
        # In the end, I just count those in the set
        lines = open(inputFilePath, "r").read().split("\n")

        claimedAtLeastOnce = set()
        claimedAtLeastTwice = set()

        for line in lines:
            claim = Claim(line)
            x = claim.x
            y = claim.y
            width = claim.width
            height = claim.height

            coordinates = claim.createCoordinates(x, y, width, height)

            for claimedCoordinate in coordinates:
                if claimedCoordinate in claimedAtLeastOnce:
                    claimedAtLeastTwice.add(claimedCoordinate)
                else:
                    claimedAtLeastOnce.add(claimedCoordinate)

        print("Number of inches, that were claimed more than once: %s" % len(claimedAtLeastTwice))



if __name__ == "__main__":
    thirdDay = ThirdDay()
    thirdDay.firstPart("input.txt")
