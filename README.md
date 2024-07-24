# Local Clustering Coefficient Estimation

This project implements an algorithm to estimate the local clustering coefficient of nodes in a graph using NetworkX, a Python library for creating, manipulating, and studying complex networks.

## Files

- `main.py`: Contains the implementation of the `LocalClusteringEstimation` function and a demonstration using a complete graph.

## Functions

### `maxdegree(G)`

Calculates the maximum degree of any node in the graph `G`.

- **Parameters:**
  - `G`: A NetworkX graph.

- **Returns:**
  - `k`: The maximum degree in the graph.

### `LocalClusteringEstimation(G, e, delta, p)`

Estimates the local clustering coefficient for each node in the graph `G`.

- **Parameters:**
  - `G`: A NetworkX graph.
  - `e`: An error parameter.
  - `delta`: A confidence parameter.
  - `p`: A probability parameter.

- **Returns:**
  - `l`: A list of estimated local clustering coefficients for each node in the graph.

## Explanation

1. **Initialization:**
   - Create two lists, `T` and `l`, initialized to zero, to store intermediate values and the final local clustering coefficients, respectively.
   - Calculate the number of edges `m` in the graph.
   - Set the constant `c` to 1.
   - Compute the number of iterations `r` needed based on the input parameters `e`, `delta`, and `p`.

2. **Main Loop:**
   - For each iteration, randomly select an edge `(a, b)` from the graph.
   - For each neighbor `v` of node `a`, check if `v` is also a neighbor of node `b`. If true, update `T[v]`.

3. **Compute Local Clustering Coefficients:**
   - For each node `v` in the graph, calculate its local clustering coefficient using the values in `T` and the degree of `v`.

## Usage

### Prerequisites

- Python 3.x
- NetworkX library

### Installation

Install the NetworkX library using pip:

`pip install networkx`

### Execution

Run the code using python3:

`python3 clustering-coefficient.py`
