#Author: Raunak Bhojwani
#Created: November 12 2014
#Lab4: Dartmouth Pathfinder
#Breadth First Search

from collections import deque                                                   # Import relevant functions
from vertex import Vertex
from load_graph import load_graph
from time import sleep


def bfs(start, goal):                                                           # Breadth First Search takes two parameters    
    q = deque()                                                                 # Initialize q as the deque
    q.append(start)                                                             # Append the start vertex
    
    backpointer = {}                                                            # Initialize backpointer as an empty dictionary    
    backpointer[start] = None                                                   # Start's backpointer is None    
    
    path = []                                                                   # Initialize path as an empty list
    
    while len(q) > 0:                                                           # Loop will terminate when all the vertices in the queue have been popped
        current = q.popleft()                                                   # Assign current to start (only element in queue)
        
        if current == goal:                                                     # If current is the goal, build up the path using backpointers before appending the start vertex into the path
            while backpointer[current] != None:
                path.append(current)
                current = backpointer[current]
            path.append(current)
            
        
        for vertex in current.adjacency_list:                                   # If goal and current are different, use a for loop to go through the adjacency list of current
            if not vertex in backpointer:                                       # If vertex hasn't been visited, append it into the deque and assign current as its backpointer
                q.append(vertex)
                backpointer[vertex] = current
        
    
    return path                                                                 # Return the path    
        

# gr = load_graph("dartmouth_graph.txt")
# start = gr["LSC East"]
# end = gr["Green South"]
# path = bfs(start, end)
# for p in path:
#    print(p)
 
 
 
    