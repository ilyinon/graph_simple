Simple library which show example of finding path in directed and undirected graph.

# Define graph where
    g = {"a": [["d", 1]],
         "b": [["c", 1]],
         "c": [["b", 1], ["c", 1], ["d", 1], ["e", 0]],
         "d": [["a", 0], ["c", 0]],
         "e": [["c", 1]],
         "f": []
         }
"g" name of graph and new class
  `a, b, c, d, e`   - vertex
  
  ```[["d", 1]], [["c", 1]], [["b", 1], ["c", 1], ["d", 1], ["e", 0]] .. etc ```-   links to other vertex,
      where second element shows is link directed or not.
      
       `1 - link is direct and we can go by it`
       `0 - link is reverse and we can't go by it`

# Create new instance of graph
    `graph = Graph(g, directed=True)`
    `graph = Graph(g, directed=False)`
    
 'directed' can has two values,  
 
    `True` - directed graph
    `False` - undirected
    


##################

#Possible actions:

1. Print vertices of graph:
```
graph.vertices()
```

2. Print edges of graph:
```
graph.edges()
```

3. Add new vertex:
```
graph.add_vertex("z")
```
4. Add new edge
```
graph.add_edge({"a", "z"})
```
5. Find path 
```
graph.find_path("e", "d")
```
