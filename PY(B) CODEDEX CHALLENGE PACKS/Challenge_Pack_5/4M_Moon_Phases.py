# Write code below 💖

def moon_phase(phase):
  if phase.lower() == 'new moon':
    return '🌑'
  elif phase.lower() == 'waxing crescent':
    return '🌒'
  elif phase.lower() == 'first quarter':
    return '🌓'
  elif phase.lower() == 'waxing gibbous':
    return '🌔'
  elif phase.lower() == 'full moon':
    return '🌕'
  elif phase.lower() == 'waning gibbous':
    return '🌖'
  elif phase.lower() == 'last quarter':
    return '🌗'
  elif phase.lower() == 'waning crescent':
    return '🌘'

answer = moon_phase('last quarter')
print(answer)


