# Principles and Fundamentals of Artificial Intelligence
## Report from Assignment 1

## Authors 
- Longho Bernard Che
- Mbah Godwin 

```shell
Running BFS with the following configuration:  check for explored nodes.  
--------------------------------
Elapsed time (s): 0.03269
Solution found at depth: 7
Number of nodes explored: 251
Cost of solution: 7
Estimated effective branching factor: 2.20196560849778
--------------------------------

Running DFS with the following configuration:  check for explored nodes.  
--------------------------------
Elapsed time (s): 0.026643
Solution found at depth: 7
Number of nodes explored: 251
Cost of solution: 7
Estimated effective branching factor: 2.20196560849778
--------------------------------

Running BFS with the following configuration:  not checking explored nodes.  
--------------------------------
Elapsed time (s): 0.029960999999999988
Solution found at depth: 7
Number of nodes explored: 341
Cost of solution: 7
Estimated effective branching factor: 2.300499028199929
--------------------------------

Running DFS with the following configuration:  not checking explored nodes.  
--------------------------------
Elapsed time (s): 0.026778999999999997
Solution found at depth: 7
Number of nodes explored: 341
Cost of solution: 7
Estimated effective branching factor: 2.300499028199929
--------------------------------


Running IDS with the following configuration:  not checking explored nodes.  
--------------------------------
Elapsed time (s): 0.027546000000000015
Solution found at depth: 7
Number of nodes explored: 341
Cost of solution: 7
Estimated effective branching factor: 2.300499028199929
--------------------------------


Running IDS with the following configuration:  check for explored nodes.  
--------------------------------
Elapsed time (s): 0.032533
Solution found at depth: 7
Number of nodes explored: 251
Cost of solution: 7
Estimated effective branching factor: 2.20196560849778
```
---
## Observations 
- When the check for visited nodes is removed from dfs, the number of nodes explored is about 90 more than when 
the check of explored nodes is enabled. This also increases the execution time of the algorithm. 

- Comparing the DFS and BFS shows that, in general, DFS is faster in terms of CPU time. Both give the same branching
factor and number of explored nodes. 

- When the search is done with IDS, we noticed that the solution was found at depth 7 just like the other algorithms.  

