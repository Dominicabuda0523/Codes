# Write code below 💖

import csv

bestselling_books = (
    ['Onyx Storm', 'Rebecca Yarros','English', 2026, '2.7M', 'Fantasy Fiction']
)

with open('Bestseller - Sheet1.csv', 'r', encoding='utf8') as file:
    csv_reader = csv.reader(file)
    file.readlines(1)
    for row in csv_reader:
        title = str(row[0])
        sales = float(row[4])
        print(f'{title} - {sales}M Sales')
    
    file.close()

with open('bestseller_info.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(bestselling_books)
    file.close()