import numpy as np
from queue import PriorityQueue
import time

def create_node(position, heuristic, parent=None):
    return {
        'position': position,
        'heuristic': heuristic,
        'parent': parent
    }

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def initialize_grid(size):
    grid = np.zeros((size, size))
    treasure_pos = (np.random.randint(0, size), np.random.randint(0, size))
    start_pos = (0, 0)
    
    # Set heuristic values
    for i in range(size):
        for j in range(size):
            grid[i][j] = manhattan_distance((i,j), treasure_pos)
            
    return grid, treasure_pos, start_pos

def get_neighbors(position, size):
    neighbors = []
    moves = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up
    
    for move in moves:
        new_pos = (position[0] + move[0], position[1] + move[1])
        if 0 <= new_pos[0] < size and 0 <= new_pos[1] < size:
            neighbors.append(new_pos)
    return neighbors

def reconstruct_path(node):
    path = []
    current = node
    while current is not None:
        path.append(current['position'])
        current = current['parent']
    return path[::-1]

def best_first_search(grid, start_pos, treasure_pos):
    size = len(grid)
    start_time = time.time()
    nodes_explored = 0
    
    frontier = PriorityQueue()
    start_node = create_node(start_pos, grid[start_pos])
    # Store only heuristic value as first element of tuple for comparison
    frontier.put((start_node['heuristic'], id(start_node), start_node))
    
    visited = set()
    
    while not frontier.empty():
        current_node = frontier.get()[2]  # Get the node from the third element
        current_pos = current_node['position']
        nodes_explored += 1
        
        if current_pos == treasure_pos:
            end_time = time.time()
            path = reconstruct_path(current_node)
            return {
                'success': True,
                'path': path,
                'nodes_explored': nodes_explored,
                'time_taken': end_time - start_time
            }
        
        visited.add(current_pos)
        
        for neighbor_pos in get_neighbors(current_pos, size):
            if neighbor_pos not in visited:
                neighbor = create_node(neighbor_pos, grid[neighbor_pos], current_node)
                # Add unique id to break ties and prevent dict comparison
                frontier.put((neighbor['heuristic'], id(neighbor), neighbor))
    
    return {'success': False}

def visualize_solution(grid, path, start_pos, treasure_pos):
    size = len(grid)
    print("\nGrid with heuristic values:")
    print(grid)
    
    print("\nPath taken (T=Treasure, S=Start, *=Path):")
    display_grid = np.full((size, size), '.')
    for pos in path:
        display_grid[pos] = '*'
    display_grid[start_pos] = 'S'
    display_grid[treasure_pos] = 'T'
    
    for row in display_grid:
        print(' '.join(row))

def main():
    size = 10
    grid, treasure_pos, start_pos = initialize_grid(size)
    result = best_first_search(grid, start_pos, treasure_pos)
    
    if result['success']:
        print(f"\nTreasure found!")
        print(f"Nodes explored: {result['nodes_explored']}")
        print(f"Time taken: {result['time_taken']:.4f} seconds")
        print(f"Path length: {len(result['path'])}")
        visualize_solution(grid, result['path'], start_pos, treasure_pos)
    else:
        print("No solution found!")

if __name__ == "__main__":
    main()
