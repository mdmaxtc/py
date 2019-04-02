"""
Program will choose winner of plyers in RPS game
"""

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "tie": "Yawn it's a tie!",
  "won": "yay you won!",
  "lost": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  print "You choose %s" % (user_choice)
  print "Computer choose %s" % (computer_choice)
  
  if computer_choice == user_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == options[2]:
      print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
      print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
      print message["won"]
  else:
    print ["lost"]
    
def play_RPS():
  print "Rock, Paper, or Scissors?"
  user_choice = raw_input("Select Rock, Paper, or Scissors: ").upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)
  
play_RPS()