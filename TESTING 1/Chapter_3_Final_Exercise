# Write code below 💖

# Stores the score of each house in a variable.

scr_gryffindor = 0
scr_ravenclaw = 0
scr_hufflepuff = 0
scr_slytherin = 0

print('\nQ1) Do you like Dawn or Dusk?')
print('1) Dawn \n2) Dusk')
question_1 = int(input('\nAnswer: '))

if question_1 == 1:
  scr_gryffindor += 1
  scr_ravenclaw += 1
elif question_1 == 2:
  scr_hufflepuff += 1
  scr_slytherin += 1
else:
  print('Wrong Input.')

print("\nWhen I’m dead, I want people to remember me as:")
print('1) The Good \n2) The Great \n3) The Wise \n4) The Bold')
question_2 = int(input('\nAnswer: '))

if question_2 == 1:
  scr_hufflepuff += 2
elif question_2 == 2:
  scr_slytherin += 2
elif question_2 == 3:
  scr_ravenclaw += 2
elif question_2 == 4:
  scr_gryffindor += 2
else:
  print('Wrong Input.')

print('\nWhich kind of instrument most pleases your ear?')
print('1) The Violin \n2) The Trumpet \n3) The Piano \n4) The Drum')
question_3 = int(input('\nAnswer: '))

if question_3 == 1:
  scr_slytherin += 4
elif question_3 == 2:
  scr_hufflepuff += 4
elif question_3 == 3:
  scr_ravenclaw += 4
elif question_3 == 4:
  scr_gryffindor += 4
else:
  print('Wrong Input.')

print('\nGryffindor: ', scr_gryffindor)
print('Ravenclaw: ', scr_ravenclaw)
print('Hufflepuff: ', scr_hufflepuff)
print('Slytherin: ', scr_slytherin)

# Finds the maximum score among the four houses.

list = [scr_gryffindor, scr_ravenclaw, scr_hufflepuff, scr_slytherin]
max_score = max(list)

# Finds which maximum score corresponds to which house.

if max_score == scr_gryffindor:
    max_score = "Gryffindor"
elif max_score == scr_ravenclaw:
    max_score = "Ravenclaw"
elif max_score == scr_hufflepuff:
    max_score = "Hufflepuff"
elif max_score == scr_slytherin:
    max_score = "Slytherin"

print(f'\nYour Hogwarts House is {max_score}!')