# Write code below 💖

liked_songs = {
    'Matasaburo': 'Yorushika',
    'Albireo': 'Rokudenashi',
    'Asu no Yozora Shokaihan': 'Yuaru',
    'Tower of Flower': 'Sayuri',
    'Koisuru Fortune Cookie': 'AKB48',
    'Fallin\'n': 'December Avenue',
    'Shelter': 'Porter Robinson',
    'Raining in Manila': 'Lola Amour',
    'Fallen': 'Lola Amour',
    'Alas Dose': 'Agsunta'
}

def write_liked_songs_to_file(songs_dict, filename):
    songs = open(filename, 'w')
    songs.write('My Favorite Songs:\n')
    for title, artist in liked_songs.items():
        songs.write(f'{title} by {artist}\n')
    songs.close()

write_liked_songs_to_file(liked_songs, 'Favorite_Songs.txt')