## 1. Extend the echo algorithm presented in class to an algorithm that executes on a connected network graph G and returns at the root node the number of nodes of the network graph, the number of edges of the network graph, and the number of edges of the echo-created spanning tree.

First, let us assume that the function `recv()` in the pseudocode returns a tuple of `(msg_type, node_counter, graph_edge_counter)`.

If the `message_type` is `ECHO`, the `node_counter` and `graph_edge_counter` are integers. Otherwise, they are `NULL`.

#### Root
```
# message types
# (EXP, from)
# (ECHO, from)

N := set of neighbors
graph_edge_count := N
node_count := 0
forall n in N, send(EXP, root)
while N != NULL do {
    (msg_type, node_counter, graph_edge_counter) = recv()
    N = N - {n}
    if (message_type == ECHO) {
        node_count = node_count + node_counter
        graph_edge_count = graph_edge_count +
            graph_edge_counter
    }
}

graph_edge_count = graph_edge_count / 2
spanning_tree_edges = node_count

return (node_count, graph_edge_count, spanning_tree_edges)
```

#### Non-root (node v)

```
(msg_type, node_counter, graph_edge_counter) = recv()
if (message_type == EXP) {
    node_counter := 1
    parent := n
    neighbor_counter := N
    N := N - {n}
    for all n in N, send(EXP, v)
    while N != NULL do {
        (msg_type, node_counter, graph_edge_counter) = 
            recv()

        N = N - {n}
        if (message_type == ECHO) {
            node_counter = node_counter + value
            neighbor_counter = neighbor_counter + 
                graph_edge_counter
        }
    }
    
    send(ECHO, node_counter, neighbor_counter, v) to parent
}
```

---

calculate network graph edges: https://stackoverflow.com/questions/40634526/number-of-edges-in-an-undirected-graph



---
calculate edges of the spanning tree: https://www.tutorialspoint.com/data_structures_algorithms/spanning_tree.htm
