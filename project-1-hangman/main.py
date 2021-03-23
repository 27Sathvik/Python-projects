import os
import random

def hangman():
  words_file = open("words.txt", "r").read()
  words = words_file.split('\n')
  word = random.choice(words)
  alphabets = ["_"]
  lives = ['❤️','❤️','❤️','❤️','❤️','❤️','❤️','❤️','❤️','❤️','❤️','❤️']
  letters = list()
  while "_" in alphabets or '❤️' not in lives:
      print(' '.join(lives))
      print(' '.join(alphabets))
      alphabets = []

      letter = input("Enter an alphabet: ")
      while len(letter) != 1 or letter.isdigit() or letter in letters:
          letter = input("Try again.Enter an alphabet: ")

      letters.append(letter)

      for alphabet in word:
          if alphabet in letters:
              alphabets.append(alphabet)
          else:
              alphabets.append("_")
              
      if letter not in alphabets:
        lives.pop()
      os.system('clear')

  print(word)
  print("You did it you won!!!")

if __name__ == "__main__":
  hangman()
