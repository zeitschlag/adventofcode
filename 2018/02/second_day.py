class SecondDay:

    def __init__(self):
        self.twosCounter= 0
        self.threesCounter = 0

    def firstPart(self, inputFilePath):
    # read input files like before.
        lines = open(inputFilePath, "r").read().split("\n")

        for line in lines:
            containsTwos = self.containsRandomCharacterExactlyTwice(testString=line)
            containsThrees = self.containsRandomCharacterExactlyThreeTimes(testString=line)

            if containsTwos is True:
                self.increaseTwosCounter()

            if containsThrees is True:
                self.increaseThreesCounter()

        checksum = self.calculateChecksum(twosCounter=self.twosCounter, threesCounter=self.threesCounter)
        print("Calculated checksum is ", checksum)

    def increaseTwosCounter(self):
        self.twosCounter = self.twosCounter + 1

    def increaseThreesCounter(self):
        self.threesCounter = self.threesCounter + 1

    # checks, if a string contains a character exactly twice
    def containsRandomCharacterExactlyTwice(self, testString):
        return self.containsRandomCharacterInString(testString=testString, numberOfOccurences=2)

    # checks if the given string contains a character excactly three times
    def containsRandomCharacterExactlyThreeTimes(self, testString):
        return self.containsRandomCharacterInString(testString=testString, numberOfOccurences=3)
    
    def containsRandomCharacterInString(self, testString, numberOfOccurences):
        characters = list(testString)
        characterCount = dict()
        for character in characters:
            if characterCount.get(character) is None:
                characterCount[character] = 1
            else:
                characterCount[character] = characterCount[character] + 1

        for key, val in characterCount.items():
            if val is numberOfOccurences:
                return True

        return False

    def calculateChecksum(self, twosCounter, threesCounter):
        import pdb; pdb.set_trace()
        return twosCounter * threesCounter

if __name__ == '__main__':
    secondDay = SecondDay()
    secondDay.firstPart("input.txt")
