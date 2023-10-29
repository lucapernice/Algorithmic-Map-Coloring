# Algorithmic Map Coloring and Problem Solving

This repository contains Python code for solving algorithmic map coloring problems and includes a module for generating random instances of such problems. The primary focus is on solving map coloring problems, which involve assigning colors to regions on a map in such a way that adjacent regions have different colors.

## Generating Map Coloring Problem Instances

The `generate_istance` module, included in this repository, provides the tools to create random instances of map-coloring problems. These instances are generated as follows:

1. Scatter `n` points on the unit square.
2. Connect the points by straight lines, ensuring that the lines do not intersect with each other.
3. Repeat this process until no more connections are possible.

The generated instances serve as input for the map coloring problem-solving algorithms.

## Problem Solving with the `Problem` Class

The `Problem` class offers a set of algorithms and tools to solve map coloring problems based on the generated instances. It includes the following key features:

### Algorithmic Map Coloring

- **Backtracking**: The `backtracking_search` method implements a basic backtracking algorithm to solve the map coloring problem. It assigns colors to regions such that adjacent regions have different colors.

- **Forward Checking**: The `backtracking_search` method also supports a forward checking option, which utilizes domain reduction to improve efficiency.

- **Maintaining Arc-Consistency (MAC)**: The `backtracking_search` method can operate with MAC to enforce arc consistency during the search, improving the algorithm's performance.

### Utility Functions

- `search_conflicts`: Identify neighbors in conflict to help resolve map coloring issues.
- `min_conflict`: Implement the min-conflict algorithm for resolving conflicts in a given assignment.
- `consistence`: Check for consistency when assigning colors to regions.
- `backtrack`: Implement the backtracking algorithm based on Russell and Norvig's "Artificial Intelligence: A Modern Approach."
- `forward_domain`: Update the domain based on forward checking.
- `backtrack_f`: Adapt the backtracking algorithm for forward checking.
- `revise`: Revise the domain values to ensure consistency using the AC3 algorithm.
- `ac3`: Use the AC3 algorithm to enforce arc consistency.
- `backtrack_mac`: Adapt the backtracking algorithm for MAC to enforce arc consistency.

## Getting Started

To use this code for solving map coloring problems or generating instances, follow these steps:

1. Import the `generate_istance` module for generating instances.

2. Create a `Problem` object with a list of regions, segment constraints, and the desired number of colors (`k`).

3. Use the `backtracking_search` method to solve the problem, specifying the type of search algorithm (normal, forward checking, or MAC).

Example:

```python
from generate_istance import generate
from your_module import Problem

# Generate a map coloring problem instance with 10 points
points, segments = generate(10)

# Create a Problem object
problem = Problem(points, segments, k)

# Solve the problem using backtracking
problem.backtracking_search(type='normal')
```

## Dependencies

This code relies on the following libraries:

- NumPy
- random (Python's built-in module)
- Shapely
- SciPy

Please ensure you have these dependencies installed to run the code successfully.

## License

This code is available under the MIT License. Feel free to use it and modify it for your research or project needs.

## Credits

This code was developed by Luca Pernice for AI introduction course. If you find this code useful or have any questions, please feel free to reach out.

Enjoy solving algorithmic map coloring problems and analyzing their performance with this code!



