import heapq
from typing import List, Tuple

class Node:
    def __init__(self, state: List[List[int]], parent: 'Node'=None, 
                 move: str=None, depth: int=0, cost: int=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        
    def __lt__(self, other):
        return self.cost < other.cost
        
    def __eq__(self, other):
        return self.state == other.state
    
    def get_blank_pos(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return (i, j)
    
    def get_children(self):
        children = []
        blank_pos = self.get_blank_pos()
        moves = ['up', 'down', 'left', 'right']
        row, col = blank_pos
        
        for move in moves:
            new_row, new_col = row, col
            
            if move == 'up':
                new_row -= 1
            elif move == 'down':
                new_row += 1
            elif move == 'left':
                new_col -= 1
            elif move == 'right':
                new_col += 1
            
            if new_row >= 0 and new_row < 3 and new_col >= 0 and new_col < 3:
                new_state = [row[:] for row in self.state]
                new_state[row][col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[row][col]
                children.append(Node(new_state, self, move, self.depth + 1, self.cost + 1))
        
        return children
    
    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    row, col = divmod(value - 1, 3)
                    distance += abs(i - row) + abs(j - col)
        return distance
    
    def misplaced_tiles(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != self.goal[i][j]:
                    count += 1
        return count
    
    def f(self):
        return self.depth + self.manhattan_distance()
    
    def __repr__(self):
        return f"{self.state}"
    
    
def a_star(initial_state: List[List[int]]) -> Tuple[List[List[int]], List[str]]:
    start_node = Node(initial_state)
    heap = [start_node]
    heapq.heapify(heap)
    closed_set = set()
    
    while heap:
        current_node = heapq.heappop(heap)
        if current_node.state == current_node.goal:
            moves = []
            while current_node.parent:
                moves.insert(0, current_node.move)
                current_node = current_node.parent
            return current_node.state, moves
        
        closed_set.add(current_node)
        
        for child in current_node.get_children():
            if child in closed_set:
                continue
                
            if child not in heap:
                heapq.heappush(heap, child)
            elif child in heap and child.cost < heap[heap.index(child)].cost:
                heap[heap.index(child)].cost = child.cost
