# Write code below 💖

def play():
  import random
  symbols = ['🍒', '🍇', '🍉', '7️⃣']
  results = random.choices(symbols, k=3)
  print(f'{results[0]} | {results[1]} | {results[2]}')

  if (results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'):
    print('Jackpot!💰')
  else:
    print('Thanks for playing!')

play()

while True:
  user_input = input('Do you want to try again? (Y/N): ')
  if user_input.lower() == 'y':
    play()
  elif user_input.lower() == 'n':
    quit()
  else:
    print('Invalid Input')

