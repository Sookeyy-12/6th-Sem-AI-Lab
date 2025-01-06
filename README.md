# 6th Semester Artificial Intelligence Lab
This repository contains the lab assignments for the Artificial Intelligence Lab course for the 6th semester of B.Tech. CSE at KIIT University.

## Lab Assignments

<details><summary>
<h3> Lab 1: Maze Solver using BFS and DFS
</summary>

**Objective**: Implement BFS and DFS to solve a maze problem

**Problem Statement**: Given a grid based maze where `0` represents walls and `1` represents walkable paths, find the shortest path from a start cell to an end cell.

**Tasks**: 
1. Use BFS to find shortest path.
2. Use DFS to explore all possible paths and report one valid path (not necessarily the shortest).
3. Compare the number of nodes explored by BFS and DFS.

</details>

<details><summary>
<h3> Lab 2: Route Finder Using Bi-Directional BFS/DFS
</summary>

**Objective**: Use Bi-directional BFS/DFS to solve a navigation problem

**Problem Statement**: Represent a City Map as a graph where intersections are nodes and roads are edges. Find the shortest path between two locations.

**Tasks**:
- Implement Bi-directional BFS to minimize the number of nodes explored.
- Compare the performance of Bi-directional BFS with standard BFS and DFS.
- Visualize the search process (e.g., using a library like networkx in Python).

</details>

<details><summary>
<h3> Lab 3: Search for treasure using Best Find Search
</summary>

**Objective**: Use Best Find Search to find a treasure in a grid

**Problem Statement**: The Treasure is hidden in a grid, and each cell has a heuristic value representing its "closeness" to the treasure. Implement Best-Find Search to locate the treasure.

**Tasks**:
1. Use Manhattan distance as heuristic.
2. Implement the algorithm to always move to the most promising cell first (minimum heuristic value).
3. Analyze how heuristic choice affects performance.

</details>