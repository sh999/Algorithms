// Directed graph type
typedef struct graph *Graph;

/* create a new graph with n vertices labeled 0..n-1 and no edges */

/* free all space used by graph */

/* add an edge to an existing graph */
/* doing this more than once may have unpredictable results */

/* return the number of vertices/edges in the graph */

/* return the out-degree of a vertex */

/* return 1 if edge (source, sink) exists), 0 otherwise */

/* invoke f on all edges (u,v) with source u */
/* supplying data as final parameter to f */
/* no particular order is guaranteed */
