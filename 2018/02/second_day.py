class SecondDay:

    def __init__(self):

        twosCounter= 0
        threesCounter = 0

    def firstPart(self, inputFilePath):
    # read input files like before.
    # counter for two letter appearences
    # gets increased, if an ID contains the same letter twice
    # counter for three letter appearences
    # gets increased, if an ID contains the same letter three times.
    # if an id contains two/three letters twice, the counter gets increased by one only once
    # multiply these counters to get the checksum
        pass
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
        return twosCounter * threesCounter

if __name__ == '__main__':
    first_part("input.txt")
