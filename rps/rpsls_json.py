import json
import sys
from random import choice, seed

# Rules of the game:
# Rock vs Paper - Paper covers rock and wins
# Rock vs scissor - Rock crushes scissor and wins
# Paper vs scissor - Scissor cuts paper and wins


def score(player, computer):
  '''
  Score the player versus computer.
  
  Return a string with the result of the game.
  '''

  if player == computer:
    return ('Tie')

  if player == 'r':
    if computer == 's':
      return ('Rock crushes scissor, rock wins')
    else:
      return ('Paper covers rock, rock loses')
  if player == 's':
    if computer == 'p':
      return ('Scissor cuts paper, scissor wins')
    else:
      return ('Rock crushes scissor, scissor loses')
  if player == 'p':
    if computer == 's':
      return ('Scissor cuts paper, scissor wins')
    else:
      return ('Paper covers rock, paper wins')


def get_player_pick_from_json():
  # We are using a json file as input to demonstrate how to debug
  # as replit offers no way to supply command line arguments nor
  # input while debugging.

  # Read the json file and return the selection.
  # It is up to the caller to verify the input.
  with open("player.json") as f_in:
    data = json.load(f_in)
    #print(json.dumps(data, indent=4))
    return data['player']


def main():

  # Make a tuple with the allowable choices
  # The computer will select from this list, and the players choice will be checked
  # against the list.
  choices = ('r', 'p', 's')

  # For debugging, read the player choice from the json file
  # and convert to lower-case.
  player = get_player_pick_from_json().lower()

  # Player decides not to play
  if player == 'q' or player == 'Q':
    print('Thanks for playing')
    sys.exit()

  # Check to make sure the player made a valid selection
  if player not in choices:
    print(f'{player} is not a valid choice')
    sys.exit()

  # Ok, we are ready to play, seed the random number generator
  seed()

  # Have the computer make a random choice
  computer = choice(choices)

  # Check the result of the game
  result = score(player, computer)

  # Print the result of the game to the concole
  print(result)

  return


if __name__ == '__main__':
  main()

