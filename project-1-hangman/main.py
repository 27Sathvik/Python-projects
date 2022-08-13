import random


words_file = open("words.txt", "r").read()
words = words_file.split('\n')
word = random.choice(words)
alphabets = ["_"]
lives = ['❤️','❤️','❤️','❤️','❤️','❤️']
letters = ['a','e','i','o','u']
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

    if len(lives) == 0:
        print("you lost")
        break 

print(word)

if __name__ == "__main__":
  hangman()
