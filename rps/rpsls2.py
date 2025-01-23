from random import choice, seed


class Game:

  def __init__(self, prompt, moves, rules):
    '''Initialize a game with a prompt, moves, and rules.'''
    self.prompt = prompt
    self.moves = moves
    self.rules = rules

  def get_prompt(self):
    ''' Return the prompt to be used to display move choices.'''
    return self.prompt

  def get_move(self):
    '''Return a move choice from the list of available moves.'''
    return choice(list(self.moves.values()))

  def play(self, move):
    '''Play the game with user-supplied move against random move by computer.'''
    if move not in self.moves:
      return (f'{move} is not a valid move, try again')

    computer = self.get_move()

    return self.rules[self.moves[move]][computer]


class rps(Game):
  '''
  Rules for Rock, Paper, Scissors.
  '''
  def __init__(self):

    prompt = '(r)ock, (p)aper, (s)cissors, or (q)uit: '
    moves = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    rules = {
        'rock': {
            'rock': 'tie',
            'paper': 'paper covers rock, rock looses',
            'scissors': 'rock crushes scissors, rock wins'
        },
        'paper': {
            'rock': 'paper covers rock, paper wins',
            'paper': 'tie',
            'scissors': 'scissors cust paper, paper looses'
        },
        'scissors': {
            'rock': 'rock crushes scissors, scissors looses',
            'paper': 'scissors cuts paper, scissors wins',
            'tie': 'tie'
        }
    }
    super().__init__(prompt, moves, rules)





class rpslk(Game):
  '''
  Rules for Rock, Paper, Scissors, Lizzard, Spock game.
  '''
  def __init__(self):
    prompt = '(r)ock, (p)aper, (s)cissors, (l)izzard, Spoc(k), or (q)uit: '
    moves = {'r': 'rock', 'p': 'paper', 's': 'scissors', 'l': 'lizzard', 'k': 'spock'}
    rules = {
        'rock': {
            'rock': 'tie',
            'paper': 'paper covers rock, rock looses',
            'scissors': 'and as always, rock crushes scissors, rock wins',
            'lizzard': 'rock crushes lizzard, rock wins',
            'spock': 'Spock vaporizes rock, rock looses'
        },
        'paper': {
            'rock': 'paper covers rock, paper wins',
            'paper': 'tie',
            'scissors': 'scissors cuts paper, paper looses',
            'lizzard': 'lizzard eats paper, paper wins',
            'spock': 'paper disproves Spock, paper looses'
        },
        'scissors': {
            'rock': 'and as always, rock crushes scissors, scissor looses',
            'paper': 'scissors cuts paper, scissor wins',
            'scissors': 'tie',
            'lizzard': 'scissors decapatates lizzard, scissor wins',
            'spock': 'Spock smashes scissors, scissors looses'
        },
        'lizzard': {
            'rock': 'rock crushes lizzard, lizzard looses',
            'paper': 'lizzard eats paper, lizzard wins',
            'scissors': 'scissors decapates lizzard, lizzard looses',
            'lizzard': 'tie',
            'spock': 'lizzard poisons Spock, lizzard wins'
        },
        'spock': {
            'rock': 'Spock vaporizes rock, Spock wins',
            'paper': 'paper disprooves Spock, Spock looses',
            'scissors': 'Spock smashes scissors, Spock wins',
            'lizzard': 'lizzard poisons Spock, Spock looses',
            'spock': 'tie'
        }
    }
    super().__init__(prompt, moves, rules)


def main():

  seed()

  game_choice = input('Do you want to play rps (1) or rpsls (2): ')
  if game_choice == '1':
    game = rps()
  elif game_choice == '2':
    game = rpslk()
  else:
    print('Invalid input, thanks for playing')
    return ()

  while True:
    
    move = input(game.get_prompt()).lower()

    if move == 'q':
      print('Thanks for playing, goodbye')
      return

    result = game.play(move)
    print(result)
    print()


if __name__ == '__main__':
  main()

