def meow(meows):
  
  if meows > 15:
    print('sorry, i am not talkative today')
    return
  if meows <= 0:
    print('I am not that talkative today')
    return


  for number in range(meows):
    print('meow')
  
#name = input('what is your name? ')
#print(f'hello {name}')

meows = int(input('How many times should I meow? '))

meow(meows)
