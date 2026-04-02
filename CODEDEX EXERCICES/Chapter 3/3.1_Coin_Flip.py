# Write code below 💖

attempts = 0

def coin_flip():
    import random
    num = random.randint(0, 1)
    
    if num > 0.5:
        print('heads')
    else:
        print('Tails')

    global attempts
    attempts += 1

while attempts < 5:
    coin_flip()


