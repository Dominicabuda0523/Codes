# Write code below 💖

# Task 1
# Statistics are made up for demonstration purposes only and do not reflect actual game statistics

kansas_player_data = [
    {'name': 'Felix Anudlike-Uzomah', 'position': 'DE', 'jersey number': 97, 'receiving yards': 1, 'touchdowns': 4},
    {'name': 'Chris Jones', 'position': 'DT', 'jersey number': 95, 'receiving yards': 2, 'touchdowns': 5},
    {'name': 'Nick Bolton', 'position': 'LB', 'jersey number': 54, 'receiving yards': 8, 'touchdowns': 1},
    {'name': 'Travis Kelce', 'position': 'TE', 'jersey number': 87, 'receiving yards': 120, 'touchdowns': 1},
    {'name': 'Patrick Mahomes', 'position': 'QB', 'jersey number': 15, 'receiving yards': 300, 'touchdowns': 3}
]

# Task 2
print('Kansas City Chiefs Roster:')
for player in kansas_player_data:
    print(f'{player["name"]}, -, {player["position"]}')

# Task 3

kansas_player_data[0]['receiving yards'] += 5 # Felix Anudlike-Uzomah caught a pass for 5 yards
kansas_player_data[0]['touchdowns'] += 1 # Felix Anudlike-Uzomah scored a touchdown

# Task 4

average_receiving_yards = sum(player['receiving yards'] for player in kansas_player_data) / len(kansas_player_data)
average_touchdowns = sum(player['touchdowns'] for player in kansas_player_data) / len(kansas_player_data)
print(f'\nAverage Receiving Yards: {average_receiving_yards}')
print(f'Average Touchdowns: {average_touchdowns}')