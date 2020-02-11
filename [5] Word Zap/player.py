import random


class Player:
    def __init__(self, name):
        self.name = name
        self.letters = []
        for i in range(7):
            self.drawLetter()

    def getName(self):
        return self.name

    def getLetters(self):
        return self.letters

    def drawLetter(self):
        letter = random.choice('aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttu'
                               'uuuvvwwxyyz')
        self.letters.append(letter)
        return letter

    def printLetters(self):
        letter_str = ''
        for item in self.letters:
            letter_str += (item + ' ')
        return letter_str.strip()

    def checkWord(self, word):
        letters = self.getLetters()[0:]
        for char in word:
            if char in letters:
                letters.remove(char)
            else:
                return False
        self.letters = letters
        return True
