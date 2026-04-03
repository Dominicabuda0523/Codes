# Write code below 💖

class City:
  def __init__(self, name, country, population, landmarks, current_mayor, nickname):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.current_mayor = current_mayor
    self.nickname = nickname

dasmarinas = City('Dasmarinas', 'Philippines', 700000, ['Immaculate Conception Parish Church','Kadiwa Park','Enchanted Kingdom'], 'Jennifer Barzaga', 'Home of the Paru-paro Festival')
tokyo = City('Tokyo', 'Japan', 14000000, ['Tokyo Tower', 'Shibuya Crossing', 'Senso-ji Temple'], 'Yuriko Koike', 'The City of the Future')

print(vars(dasmarinas))
print(vars(tokyo))