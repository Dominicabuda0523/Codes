# Write code below 💖

dna_sequence = [
  'GCT', 'AGC', 'AGG', 
  'TAA', 'ACT', 'CAT', 
  'TAT', 'CCC', 'ACG', 
  'GAA', 'ACC', 'GGA'
  ]

item_to_find = 'GGA'

for item in dna_sequence:
  if item_to_find == item:
    item_found = True
    break
  else:
    item_found = False
  
if item_found == True:
  print('Item Found!')
else:
  print('Item not found.')
