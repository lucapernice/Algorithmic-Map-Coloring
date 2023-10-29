# Algorithmic Map Coloring and Problem Solving

This repository contains Python code for solving algorithmic map coloring problems and includes a module for generating random instances of such problems. The primary focus is on solving map coloring problems, which involve assigning colors to regions on a map in such a way that adjacent regions have different colors.

## Generating Map Coloring Problem Instances

The `generate_istance` module, included in this repository, provides the tools to create random instances of map-coloring problems. These instances are generated as follows:

1. Scatter `n` points on the unit square.
2. Connect the points by straight lines, ensuring that the lines do not intersect with each other.
3. Repeat this process until no more connections are possible.

The generated instances serve as input for the map coloring problem-solving algorithms.

## Problem Solving with the `Problem` Class

The Problem class is the heart of this repository, designed to solve map coloring problems. It offers a variety of algorithms and utility functions to facilitate the process of assigning colors to regions on a map while ensuring that adjacent regions have different colors.

## The `Problem` Class

The `Problem` class is the heart of this repository, designed to solve map coloring problems. It offers a variety of algorithms and utility functions to facilitate the process of assigning colors to regions on a map while ensuring that adjacent regions have different colors.

### Initializing the Problem

To create a `Problem` object, you need to provide the following parameters:

- `list_of_regions`: A list containing the points or regions that need to be colored.
- `seg_list`: A list of objects from the `gen.Segment` class, which represent constraints on the coloring. These segments define which regions should not have the same color.
- `k`: An integer representing the number of available colors.
- `colours`: An array that will be used to store the assigned colors for each region.

Here's how you initialize a `Problem`:

```python
problem = Problem(list_of_regions, seg_list, k)
```

### Solving Map Coloring Problems

The `Problem` class provides various methods to solve map coloring problems. The primary methods are as follows:

#### Backtracking Search

The `backtracking_search` method is used to solve the map coloring problem using different techniques:

- **Normal Backtracking**: You can call `backtracking_search` without any parameters to use normal backtracking, which tries to find a valid coloring of the map.

```python
problem.backtracking_search()
```

- **Backtracking with Forward Checking**: To use forward checking, specify `type='forward_checking'` when calling the method. Forward checking reduces the domain of possible colors for each region based on prior assignments.

```python
problem.backtracking_search(type='forward_checking')
```

- **Backtracking with Maintaining Arc-Consistency (MAC)**: To use MAC, specify `type='mac'` when calling the method. MAC enforces arc consistency while searching for a solution, improving efficiency.

```python
problem.backtracking_search(type='mac')
```

#### Utility Functions

The `Problem` class also provides utility functions to assist in solving map coloring problems:

- `search_conflicts`: This function returns a list of neighbors in conflict, which helps identify regions that need to be recolored.

- `min_conflict`: The `min_conflict` method implements the min-conflict algorithm, which resolves conflicts in a given assignment.

- `consistence`: This function checks for consistency when assigning colors to regions.

- `backtrack`: The `backtrack` method implements the backtracking algorithm based on Russell and Norvig's "Artificial Intelligence: A Modern Approach."

- `forward_domain`: It updates the domain based on forward checking, ensuring regions do not have conflicting colors.

- `backtrack_f`: The `backtrack_f` method adapts the backtracking algorithm for forward checking.

- `revise`: The `revise` function is used to revise the domain values, ensuring consistency using the AC3 algorithm.

- `ac3`: The `ac3` method uses the AC3 algorithm to enforce arc consistency.

- `backtrack_mac`: The `backtrack_mac` method adapts the backtracking algorithm with MAC to enforce arc consistency.

### Using the `Problem` Class

To use the `Problem` class to solve a map coloring problem, follow these steps:

1. Create a `Problem` object by providing a list of regions, segment constraints, and the desired number of colors.

2. Choose the type of search algorithm you want to use for solving the problem (normal backtracking, forward checking, or MAC).

3. Call the `backtracking_search` method with the specified algorithm type.

Here's an example of how to use the `Problem` class:

```python
from generate_istance import generate
from solver import Problem

# Generate a map coloring problem instance with 10 points
points, segments = generate(10)

# Create a Problem object
problem = Problem(points, segments, k = 4)

# Solve the problem using backtracking
problem.backtracking_search(type='normal')

# Print the solution
print(problem.colours)
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



