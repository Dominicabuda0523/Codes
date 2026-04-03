# Write code below 💖

class Pokemon:
  def __init__(self, entry, name, height, weight, category, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.height = height
    self.weight = weight
    self.category = category
    self.types = types
    self.desctiption = description
    self.is_caught = is_caught

  def speak(self):
    print(f'{self.name}, {self.name}!')

  def display_details(self):
    print(f'Entry: {self.entry}')
    print(f'Name: {self.name}')
    print(f'Height: {self.height}')
    print(f'Weight: {self.weight}')
    print(f'Category: {self.category}')
    print(f'Types: {", ".join(self.types)}')
    print(f'Description: {self.desctiption}')
    print(f'Caught: {"Yes" if self.is_caught else "No"}')
    

pikachu = Pokemon(25, 'Pikachu', "2'4\"", '66.1 lbs', 'Mouse Pokémon', ['Electric'], 'Pikachu that can generate powerful electricity have cheek sacs that are extra soft and super stretchy.', True)
charizard = Pokemon(6, 'Charizard', "5'7\"", '199.5 lbs', 'Flame Pokémon', ['Fire', 'Flying'], 'Charizard flies around the sky in search of powerful opponents.', False)
bulbasaur = Pokemon(1, 'Bulbasaur', "2'4\"", '15.2 lbs', 'Seed Pokémon', ['Grass', 'Poison'], 'Bulbasaur can be seen napping in bright sunlight.', True)

pikachu.speak()
print('\n')
pikachu.display_details()
print('\n')

charizard.speak()
print('\n')
charizard.display_details() 
print('\n')

bulbasaur.speak()
print('\n')
bulbasaur.display_details()

