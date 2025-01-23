from random import choice
import sys

moves = ('r', 'p', 's')
player_wins = 0

while(True):
  
  player = input('what is your move? (r)ock, (p)aper, (s)cissor, (q)uit ? ').lower()

  if player == 'q':
    print('Thanks for playing')
    print(f'You have won {player_wins} times')
    sys.exit()
  
  if player not in moves:
    print('invalid move')
    #sys.exit()
  
  computer = choice(moves)
  
  if player == 'r':
    if computer == player:
      print('tie')
    elif computer == 'p':
      print('Paper covers rock, rock looses')
    else:
      print('Rock crushes scissors, rock wins')
      player_wins = player_wins + 1
  
  elif player == 'p':
    if computer == player:
      print('tie')
    elif computer == 'r':
      print('Paper covers rock, paper wins')
      player_wins = player_wins + 1
    else:
      print('Scissors cuts paper, paper looses')
  
  else: #scissors
    if computer == player:
      print('tie')
    elif computer == 'r':
      print('Rock crushes scissors, scissors looses')
    else:
      print('Scissors cuts paper, scissors wins')
      player_wins = player_wins + 1
