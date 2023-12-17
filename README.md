# Social Network Analysis for Computer Scientists - Code

By R. Wensveen & R. The

The following repository contains all code as presented in our paper. This code is used for the several experiments that have been performed in order to exactly determine/approximate betweenness centrality.

## Files/Folders:

- betweennessCentrality.py: script to perform betweenness centrality calculation/approximation using all of our created methods.
- Code: contains all necessary code to perform betweenness centrality estimation
- Data: contains all datasets that are used within our paper

### betweennessCentrality.py:

Usage of the script as follows:

```
usage: betweennessCentrality.py [-h] [-d DIRECTED] input_file

This script will perform exact calculation and approximation of betweenness
centrality, and will present the statistics of this.

positional arguments:
input_file Path to the input file, of a give graph in (weighted) edge-list format

optional arguments:
-h, --help show this help message and exit
-d DIRECTED, --directed DIRECTED
Set input graph type to directed graph. True OR False,
Default=False

```

This script will perform our experiment consisting of the following steps:

1. Exact calculation of betweenness centrality using NetworkX, Brandes implementation.
2. Approximation of betweenness centrality using NetworkX, Brandes implementation, with sampling/pivoting
   - Sample size of 60/80% of number of nodes.
3. Approximation of betweenness centrality using NetworKit,

### Data:

- Directed and weighted graph: yeastinter_st.txt
  - Nodes: 688 Edges: 1,079
- Directed and weighted graph: USairport500
  - Nodes: 7,976 Edges: 30,501
- Directed and unweighted graph: email-Eu-core.txt
  - Nodes: 1,005 Edges: 25,571
- Directed and unweighted graph: p2p-Gnutella24.txt
  - Nodes: 26,518 Edges: 65,369
- Undirected and weighted graph: mol_yeast_spliceosome.txt
  - Nodes: 103 Edges: 4,119
- Undirected and weighted graph: bio-CE-CX.txt
  - Nodes: 15,229 Edges: 245,952
- Undirected and unweighted graph: mc_mullen.txt
  - Nodes: 159 Edges: 204
- Undirected and unweighted graph: bio-CE-CX.txt
  - Nodes: 11,174 Edges: 23,409

### Dependencies

- rich
- networkx
- networkit
