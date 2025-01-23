from random import choice, seed


class Game:

  def __init__(self, prompt, moves, outcomes):
    self.prompt = prompt
    self.moves = moves
    self.outcomes = outcomes

  def get_prompt(self):
    return self.prompt

  def get_move(self):
    return choice(list(self.moves.keys()))

  def play(self, player_choice):
    if player_choice not in self.moves:
      return (f'{player_choice} is not a valid move, try again')

    computer_choice = self.get_move()

    if player_choice == computer_choice:
      return f"It's a tie!  Both choose {self.moves[player_choice]}"
    elif (player_choice, computer_choice) in self.outcomes:
      outcome = self.outcomes[(player_choice, computer_choice)]
      return f'{outcome}: {self.moves[player_choice].capitalize()} wins!'
    else:
      outcome = self.outcomes[(computer_choice, player_choice)]
      return f'{outcome}: {self.moves[player_choice].capitalize()} loses!'


class rps(Game):

  def __init__(self):
    prompt = '(r)ock, (p)aper, (s)cissors, or (q)uit: '
    moves = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    outcomes = {
        ('r', 's'): "Rock crushes scissors",
        ('s', 'p'): "Scissors cuts paper",
        ('p', 'r'): "Paper covers rock"
    }

    super().__init__(prompt, moves, outcomes)


class rpslk(Game):

  def __init__(self):
    prompt = '(r)ock, (p)aper, (s)cissors, (l)izzard, Spoc(k) or (q)uit: '
    moves = {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors',
        'l': 'lizzard',
        'k': 'Spock'
    }
    outcomes = {
        ('r', 's'): "And as always, rock crushes scissors",
        ('s', 'p'): "Scissors cuts paper",
        ('p', 'r'): "Paper covers rock",
        ('p', 'k'): "Paper disprooves Spock",
        ('s', 'l'): "Scissor decapatates lizzard",
        ('l', 'k'): "Lizzard poisons Spock",
        ('k', 's'): "Spock smashes scissors",
        ('k', 'r'): "Spock vaporizes rock",
        ('l', 'p'): "Lizzard eats paper",
        ('r', 'l'): "Rock crushes lizzard"
    }

    super().__init__(prompt, moves, outcomes)


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

