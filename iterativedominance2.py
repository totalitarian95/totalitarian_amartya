"""
Iterative dominance strategy, a different code
Totalitarian
"""
def is_dominated(strategy, payoff_matrix):
  """
  Checks if a strategy is dominated by another strategy

  Args:
    strategy (list): List representing the strategy (e.g., [1, 0] for choosing option 1)
    payoff_matrix (list of lists): Payoff matrix for the game

  Returns:
    bool: True if dominated, False otherwise
  """
  dominated = False
  for other_strategy in payoff_matrix:
    if all(other_strategy[i] >= strategy[i] for i in range(len(strategy))):
      # Check if all payoffs under other strategy are at least as good
      if any(other_strategy[i] > strategy[i] for i in range(len(strategy))):
        # Check if at least one payoff under other strategy is strictly better
        dominated = True
        break
  return dominated

def iterative_dominance(payoff_matrix):
  """
  Implements iterative dominance algorithm

  Args:
    payoff_matrix (list of lists): Payoff matrix for the game

  Returns:
    list of lists: List of remaining iteratively dominant strategies for each player
  """
  dominant_strategies = [list(range(len(payoff_matrix[0])))] * len(payoff_matrix)
  changed = True
  while changed:
    changed = False
    for player in range(len(payoff_matrix)):
      new_dominant_strategies = []
      for strategy in dominant_strategies[player]:
        if not is_dominated(payoff_matrix[strategy], payoff_matrix):
          new_dominant_strategies.append(strategy)
      if new_dominant_strategies != dominant_strategies[player]:
        changed = True
      dominant_strategies[player] = new_dominant_strategies
  return dominant_strategies

# Example usage
payoff_matrix = [[[1, 0], [2, 1]], [[0, 2], [1, 1]]]
dominant_strategies = iterative_dominance(payoff_matrix)

print("Dominant strategies:")
for i, player_strategies in enumerate(dominant_strategies):
  print(f"Player {i+1}: {player_strategies}")