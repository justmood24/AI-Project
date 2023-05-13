from queue import PriorityQueue

# Define the goal state as a tuple
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, None))

# Define the heuristic function (Manhattan distance)
def h(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] is not None:
                x, y = divmod(state[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

# Define the A* algorithm function
def a_star(start_state):
    # Initialize the priority queue with the start state
    queue = PriorityQueue()
    queue.put((h(start_state), start_state, 0))

    # Initialize the visited set and the moves list
    visited = set()
    moves = []

    while not queue.empty():
        # Get the state with the lowest f score
        f, state, cost = queue.get()

        # If the state is the goal state, return the moves list
        if state == goal_state:
            return moves

        # Add the state to the visited set
        visited.add(state)

        # Generate the possible next states
        for i, j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x, y = None, None
            for m in range(3):
                if None in state[m]:
                    n = state[m].index(None)
                    x, y = m, n
                    break
            new_x, new_y = x + i, y + j
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [list(row) for row in state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                new_state = tuple(tuple(row) for row in new_state)
                if new_state not in visited:
                    queue.put((h(new_state) + cost + 1, new_state, cost + 1))
                    moves.append((new_state, cost + 1))

    # If the goal state is not found, return None
    return None

# Test the algorithm with a sample start state
start_state = ((1, 2, 3), (4, None, 6), (7, 5, 8))
moves = a_star(start_state)
if moves is not None:
    for move in moves:
        print(move[0])
else:
    print("No solution found.")
