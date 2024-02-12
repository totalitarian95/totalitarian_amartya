"""
Location game
Totalitarian
"""
import numpy as np
import matplotlib.pyplot as plt

def location_game(num_players=3, num_locations=8):
    # Simulate the location game as before
    market_locations = np.random.randint(1, 100, num_locations)
    market_locations.sort()
    player_locations = np.random.choice(market_locations, num_players, replace=False)

    player_payoffs = []
    for i in range(num_players):
        total_distance = sum(abs(player_locations[i] - loc) for loc in player_locations if loc != player_locations[i])
        player_payoffs.append(1 / (total_distance + 1))

    return player_locations, player_payoffs

# Simulate the location game
player_locations, player_payoffs = location_game()

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(player_locations, player_payoffs, color='red', label='Player Locations', s=100)
for i, txt in enumerate(player_payoffs):
    plt.annotate(f'Payoff: {player_payoffs[i]:.2f}', (player_locations[i], player_payoffs[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.xlabel('Market Locations')
plt.ylabel('Payoff')
plt.title('Location Game Results')
plt.xticks(player_locations)
plt.grid(True)
plt.legend()
plt.show()
