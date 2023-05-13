# Run A* algorithm to solve 8-puzzle problem
solution = a_star(initial_state, goal_state)

# Print solution path and number of steps
if solution is None:
    print("No solution found!")
else:
    print("Solution found in", len(solution) - 1, "steps:")
    for i, state in enumerate(solution):
        print("Step", i, ":")
        print(state) 
