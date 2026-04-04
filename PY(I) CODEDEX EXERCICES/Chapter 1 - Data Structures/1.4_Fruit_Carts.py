# Write code below 💖

friend_fav_fruits = {'🫐','🍇','🍌','🍓','🍒'}
my_fav_fruits = {'🍍','🍌','🍓','🍒','🥭'}

similar = friend_fav_fruits.intersection(my_fav_fruits)
difference = friend_fav_fruits.difference(my_fav_fruits)

print(f'The similarities are: {similar}\n')
print(f'The difference are: {difference}')