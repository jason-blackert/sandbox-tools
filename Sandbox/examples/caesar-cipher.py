import numpy as np
import time

class Caesar:
    def __init__(self):
        self.letters = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.phrase  = "Dead Again"
        self.key     = 0

        self.encodedList = []
        self.decodedList = []

    def setKey(self, key=0):
        self.key = key

    def setPhrase(self, phrase="Dead Again"):
        self.phrase = phrase.upper()

    def encodePhrase(self):
        encodedList = []
        for i in range(len(self.phrase)):
            phraseLetter=self.phrase[i]
            index        = self.letters.index(phraseLetter)

            if index == 0:
                encodedList.append(self.letters[index])
            else:
                encodedIndex = self.letters.index(phraseLetter)+self.key
                while encodedIndex > len(self.letters):
                    encodedIndex-=len(self.letters)
                encodedList.append(self.letters[encodedIndex])

        self.encodedList = ''.join([str(elem) for elem in encodedList])
        print(self.encodedList)

    def decodePhrase(self):
        decodedList = []
        for i in range(len(self.phrase)):
            phraseLetter=self.phrase[i]
            index        = self.letters.index(phraseLetter)

            if index == 0:
                decodedList.append(self.letters[index])
            else:
                decodedIndex = self.letters.index(phraseLetter)-(self.key-1) # how python indexing works
                while decodedIndex < 0:
                    decodedIndex+=len(self.letters)
                decodedList.append(self.letters[decodedIndex])

        self.decodedList = ''.join([str(elem) for elem in decodedList])
        print(self.decodedList)

if __name__ == "__main__":
    cipher = Caesar()
    cipher.setKey(1)
    cipher.setPhrase("how are you doing")
    cipher.encodePhrase()
    cipher.decodePhrase()
    input()