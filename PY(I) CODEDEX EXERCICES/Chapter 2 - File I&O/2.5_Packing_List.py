# Write code below 💖

import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('packing_list.csv', 'r', encoding='utf8') as file:
        csv_reader = csv.reader(file)
        print(csv_reader)
except FileNotFoundError:
    print('Packing list not found. Creating a new one.')
    with open('packing_list.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)