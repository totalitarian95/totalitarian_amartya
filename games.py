"""
iterative dominance
And finding nash equillibrium
Totalitarian
"""
from matplotlib import pyplot as plt
import numpy as np

def is_strictly_dominated(strategy, payoff_matrix, player):
    """
    Check if a strategy is strictly dominated by another strategy.
    """
    num_strategies = payoff_matrix.shape[player]
    for s in range(num_strategies):
        if s != strategy:
            if player == 0:
                if all(payoff_matrix[strategy, :] > payoff_matrix[s, :]):
                    return True
            elif player == 1:
                if all(payoff_matrix[:, strategy] > payoff_matrix[:, s]):
                    return True
    return False

def eliminate_strictly_dominated_strategies(payoff_matrix):
    """
    Eliminate strictly dominated strategies iteratively.
    """
    num_strategies_player1 = payoff_matrix.shape[0]
    num_strategies_player2 = payoff_matrix.shape[1]

    # Initially, no strategy is eliminated
    is_strategy_eliminated = [False] * num_strategies_player1, [False] * num_strategies_player2

    # Iterate until no more strategies can be eliminated
    while True:
        # Flag to check if any strategy has been eliminated in this iteration
        eliminated_in_iteration = False

        # Check if any strategy of player 1 is strictly dominated
        for s in range(num_strategies_player1):
            if not is_strategy_eliminated[0][s] and is_strictly_dominated(s, payoff_matrix, 0):
                is_strategy_eliminated[0][s] = True
                eliminated_in_iteration = True

        # Check if any strategy of player 2 is strictly dominated
        for s in range(num_strategies_player2):
            if not is_strategy_eliminated[1][s] and is_strictly_dominated(s, payoff_matrix, 1):
                is_strategy_eliminated[1][s] = True
                eliminated_in_iteration = True

        # If no strategy has been eliminated in this iteration, break the loop
        if not eliminated_in_iteration:
            break

    # Construct the reduced payoff matrix after eliminating dominated strategies
    reduced_payoff_matrix = np.copy(payoff_matrix)
    reduced_payoff_matrix = np.delete(reduced_payoff_matrix, np.where(is_strategy_eliminated[0]), axis=0)
    reduced_payoff_matrix = np.delete(reduced_payoff_matrix, np.where(is_strategy_eliminated[1]), axis=1)

    return reduced_payoff_matrix

def find_nash_equilibria(payoff_matrix):
    """
    Find Nash equilibria using iterative elimination of strictly dominated strategies.
    """
    # Eliminate strictly dominated strategies
    reduced_payoff_matrix = eliminate_strictly_dominated_strategies(payoff_matrix)

    # Find Nash equilibria using the reduced payoff matrix
    nash_equilibria = []

    # Loop through the reduced payoff matrix to find Nash equilibria
    for strategy_player1 in range(reduced_payoff_matrix.shape[0]):
        for strategy_player2 in range(reduced_payoff_matrix.shape[1]):
            #
# Check if the current strategy pair is a Nash equilibrium
            is_nash_equilibrium = True
            for s1 in range(reduced_payoff_matrix.shape[0]):
                if reduced_payoff_matrix[s1, strategy_player2] > reduced_payoff_matrix[strategy_player1, strategy_player2]:
                    is_nash_equilibrium = False
                    break
            for s2 in range(reduced_payoff_matrix.shape[1]):
                if reduced_payoff_matrix[strategy_player1, s2] > reduced_payoff_matrix[strategy_player1, strategy_player2]:
                    is_nash_equilibrium = False
                    break

            # If the current strategy pair is a Nash equilibrium, append it to the list
            if is_nash_equilibrium:
                nash_equilibria.append((strategy_player1, strategy_player2))

    return nash_equilibria

# Example usage:
if __name__ == "__main__":
    # Define the payoff matrix for the game
    payoff_matrix = np.array([[3, 2, 4],
                               [1, 4, 2],
                               [2, 3, 3]])

    # Find Nash equilibria using iterative elimination of strictly dominated strategies
    nash_equilibria = find_nash_equilibria(payoff_matrix)

    # Print the Nash equilibria
    if len(nash_equilibria) > 0:
        print("Nash Equilibria:")
        for equilibrium in nash_equilibria:
            print("Player 1 plays strategy {}, Player 2 plays strategy {}".format(equilibrium[0], equilibrium[1]))
    else:
        print("No Nash Equilibrium found.")
        # Visualize the payoff matrix
    plt.imshow(payoff_matrix, cmap='viridis', interpolation='nearest')
    plt.title('Payoff Matrix')
    plt.colorbar(label='Payoff')
    plt.xlabel('Player 2 Strategy')
    plt.ylabel('Player 1 Strategy')

    # Highlight Nash equilibria
    for equilibrium in nash_equilibria:
        plt.plot(equilibrium[1], equilibrium[0], 'ro')  # Player 2, Player 1

    plt.show()

