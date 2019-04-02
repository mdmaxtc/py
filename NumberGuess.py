
#In this project, we'll build a program that rolls a pair of dice and asks the user to guess the sum. If the user's guess is equal to the total value of the dice roll, the user wins! Otherwise, the computer wins.

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Enter the guess: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is: %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "Ne nado preuvelichivat"
  else:
    print "Rolling..."
    sleep(2)
    print "The 1st roll is %d:" % first_roll
    sleep(1)
    print "The 2nd roll is %d:" % second_roll
    total_roll = first_roll + second_roll
    print "The total roll is %d:" % total_roll
    print "The result..."
    sleep(1)
    if guess == total_roll:
      print "You won!"
    else:
        print "You lost, try again."
        
roll_dice(6)