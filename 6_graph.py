# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:31:54 2019

@author: z.chen7
"""

"""
graph is a data structure designed to show relationships between objects (vertex/node)

DAG
Directed Acyclic (no cycle) Graph

A directed graph is weakly connected when only replacing all of the directed 
edges with undirected edges can cause it to be connected. 
Imagine that your graph has several vertices with one outbound edge, 
meaning an edge that points from it to some other vertex in the graph. 
There's no way to reach all of those vertices from any other vertex in the graph, 
but if those edges were changed to be undirected all vertices would be easily accessible.


There's one vertex, U, that has only inbound edges—meaning only edges that point to it. 
Thus, the graph can't be strongly connected. Even if every vertex has a path to U,
it doesn't have a path to any of them.

"""


# Graph Representation Practice
"""
In this exercise you'll need to add functions to a Graph class to return 
various representations of the same graph. 
Your graph will have two different components: Nodes and Edges."""

"""
Nodes are pretty much the same as they were in trees. Instead of having a set 
number of children, each node has a list of Edges."""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

"""
Here, we assume that edges have both a value and a direction. 
An edge points from one node to another — the node it starts at is the 
node_from and the node it ends at is the node_to. 
You can envision it as node_from -> node_to."""

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value =  value
        self.node_from = node_from
        self.node_to = node_to
        
"""
A Graph class contains a list of nodes and edges. 
You can sometimes get by with just a list of edges, 
since edges contain references to the nodes they connect to, or vice versa. 
However, our Graph class is built with both for the following reasons:

    * If you're storing a disconnected graph, not every node will be tied to an edge, 
      so you should store a list of nodes.
    * We could probably leave it there, but storing an edge list will make our 
      lives much easier when we're trying to print out different types of graph representations.

Unfortunately, having both makes insertion a bit complicated. 
We can assume that each value is unique, but we need to be careful about 
keeping both nodes and edges updated when either is inserted."""

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        
    def insert_nodes(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(from_found)
        to_found.edges.append(to_found)
        self.edges.append(new_edge)
        
    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]
    
    def find_max_node_value(self):
        max_node_value = -1
        if self.nodes:
            for node in self.nodes:
                if node.value > max_node_value:
                    max_node_value = node.value  
        return max_node_value
    
    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_index = self.find_max_node_value()
        adjacency_list = [None] * (max_index + 1)
        for edge_object in self.edges:
            if adjacency_list[edge_object.node_from.value]:
                adjacency_list[edge_object.node_from.value].append((edge_object.node_to.value, edge_object.value))
            else:
                adjacency_list[edge_object.node_from.value] = [(edge_object.node_to.value, edge_object.value)]
        return adjacency_list

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        matrix_len = self.find_max_node_value()
        adjacency_matix = [[0] * (matrix_len + 1) for i in range(matrix_len + 1)]
        if self.edges:
            for edge_object in self.edges:
                adjacency_matix[edge_object.node_from.value][edge_object.node_to.value] = edge_object.value
        return adjacency_matix
        


graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
graph.insert_nodes(5)

graph.get_edge_list()

graph.get_adjacency_list()

graph.get_adjacency_matrix()




# Graph traversal
"""
Two basic methods for graph traversal
    * a depth first search, where we follow one path as far as it'll go
    * a breadth first search, where we look at all the nodes adjacent to one before moving on to the next level

A graph search and a graph traversal is roughly the same thing.
In a traversal, you look at every element, and in a search, you just stop traversing
when you find the element you're looking for.

A common implementation of depth first search (DFS) users a stack, so we can
store the node we just saw on the stack. Next you pick an edge follow it and
mark that node as seen and add it to the stack.
When you do hit a node that you've seen before, just go back to the previous node
and try another edge.
If you run out of edges with new nodes, you pop the current node from the stack
and go back to the one before it, which is just the next one on the stack.
You continue this approach until you've popped everything off the stack or you 
find the node you were originally looking for. 

There's another common implementation of depth first search (DFS) that uses 
recursion and no stack.

run time: O(|E| + |V|)

For breadth first search (BFS), you're still visiting every edge and marking off every node.
However, here you search every edge of one node before continuing on through the graph.
Again, we start with the first node and mark it as seen, then visit a node adjacent
to it. Once we mark that node, we can add it to a queue. We go back to that first
node and visit everything adjacent to it, marking each as seen and adding them
to a queue. When we run out of edges, we can just dequeue a node from the queue
and use that as our next starting place

the efficiency: O(|E| + |V|) (the number of edges plus the number of vertices)
"""


# Graph Traversal practice



# Eulerian path
"""
a path that travels through evey edge in a graph at least once.

Eulerian Cycle: you must traverse every edge only once and end up 
at the same node that started with.
Graphs can only have Eulerian cycles if all vertices have an even degree
or an evern number of edges connected to them.

Eulerian paths are a little bit more lenient. So it's okay for your graph to 
have two nodes with an odd degree as long as they're the start and end of the path.

"""