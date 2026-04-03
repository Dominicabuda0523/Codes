# Write code below 💖

guess = 0
tries = 0

while guess != 6 and tries < 6:
  guess = int(input("Guess the number:  "))
  tries += 1

print("You got it!")