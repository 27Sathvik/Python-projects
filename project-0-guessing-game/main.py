"""
Project 0 : Guessing game with numbers.
"""

import random


def guessing_game():
    random_number = random.randrange(0, 100)
    user_guess = int(
        input("enter a number between {0} &  {1}: ".format(0, 100)))
    divisible_properties = []
    counter = 0

    def number_property():
        for num in range(2,10):
          if random_number % num == 0:
            divisible_properties.append(num)

        random_property = random.choice(divisible_properties)
        return random_property

    while user_guess != random_number:
        counter += 1
        if user_guess < random_number:
            print("Number is greater than", user_guess)
        if user_guess > random_number:
            print("Number is lesser than", user_guess)
        print("The number is divisible by",number_property())

        user_guess = int(input(" try again enter a number between {0} & {1}: ".format(0, 100)))
  
    if user_guess == random_number:
      print("\nYou did it you won in {} tries".format(counter))

                

if __name__ == "__main__":
  guessing_game()