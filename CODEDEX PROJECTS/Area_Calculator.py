
# Interface or the Menu of the Area Calculator
def interface():
  print('\n===================')
  print('Area Calculator 📐')
  print('===================\n')

  print('1) Triangle')
  print('2) Rectangle')
  print('3) Square')
  print('4) Circle')
  print('5) Quit')

interface()

# Function to select the shape that the user wants to calculate the area of. 
# It also validates the input to make sure it is an integer.
def shape_select():
  while True:
    try:
      user_input = int(input('\nPlease select which shape: \n'))
      return user_input
    except ValueError:
      print('Invalid Input. Please try again.')

# Define the variable to store the user input for shape selection after validating it.
user_input = shape_select()

# Calculate for area of Triangle
if user_input == 1:
  base = float(input('Base: '))
  height = float(input('Height: '))
  area_tr = (base * height) / 2
  print('Area of Triangle: ', area_tr)

# Calculate for area of Rectangle
elif user_input == 2:
  length = float(input('Length: '))
  width = float(input('Width: '))
  area_re = length * width
  print('Area of Rectangle: ', area_re)

# Caculate for area of Square
elif user_input == 3:
  side = float(input('Side: '))
  area_sq = side ** 2
  print('Area of Square: ', area_sq)

# Calculate for area of Circle
elif user_input == 4:
  radius = float(input('Radius: '))
  area_ci = 3.14 * (radius ** 2)
  print('Area of Circle: ', area_ci)

# Quit the program if the user selects 5
elif user_input == 5:
  print('\nThank you for using!\nSee you next time!')
  quit()

# If the user input is not between 1 and 5, it will print an error message and ask the user to select again.
while True:
  retry = input('\nDo you want to calculate again? (Y/N): ')
  if retry.lower() == 'y':
    interface()
    shape_select()
  elif retry.lower() == 'n':
    print('\nThank you for using!\nSee you next time!')
    quit()
  else:
    print('Invalid Input. Please try again.')