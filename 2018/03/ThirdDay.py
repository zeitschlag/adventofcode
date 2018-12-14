import re

class Claim:

    def __init__(self, line):

        pattern = "^(.*?)@ (.*?),(.*?): (.*?)x(.*?)$"
        result = re.search(pattern, line)
        
        self.id = result.group(1)
        self.x = int(result.group(2))
        self.y = int(result.group(3))
        self.width = int(result.group(4))
        self.height = int(result.group(5))

    def createCoordinates(self, x, y, width, height):
        coordinates = set()
        for i in range(x, x+width):
            for j in range(y, y+height):
                coordinates.add(str(i) + "," + str(j))
        
        return coordinates


class ThirdDay:

    def firstPart(self, inputFilePath):
        # read input files like before.
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


#  #ID @ distanceFromLeft,distanceFromTop: width x height
# id @ x, y, width x height
#  #123 @ 3,2: 5x4

# I want a structure with ID, distanceFromLeft, distanceFromTop, width, height
# I could use a regex-based parser to read the raw-data
# I have a bunch of claims and I need the overlapping points
# build claimed territory
# check for each point, if its already claimed. If yes: make an x. if no: claim it

# I could use a set, which handles the coordinates
# alreadyClaimedCoordinates = intersection(allSets)

# I calculate the coordinates for each suit and check, if they're already in the set
# In the end, I just count those in the set

if __name__ == "__main__":
    thirdDay = ThirdDay()
    thirdDay.firstPart("input.txt")
