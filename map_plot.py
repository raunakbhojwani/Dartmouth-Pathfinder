#Author: Raunak Bhojwani
#Created: November 10 2014
#Lab4: Dartmouth Pathfinder
#Drawing Code

from cs1lib import *                                                            # Import all relevant functions
from load_graph import *
from bfs import bfs
from vertex import Vertex

def draw_path(path):                                                            # Function to draw the returned list 'path'
    for i in range(len(path)-1):                                                # For each element in the list, call draw path on it and the next element
        path[i].draw_path(path[i+1])

def map_plot():                                                                 # Function to plot the map
    map_img = load_image("dartmouth_map.png")                                   # Load image only once
    vertex_dictionary = load_graph("dartmouth_graph.txt")                       # Assign the dictionary returned in load_graph to vertex_dictionary
    start_vertex = None                                                         # Initialize the start_vertex and goal_vertex to None
    goal_vertex = None
            
    while not window_closed():                                                  # Begin the animation loop
        
        draw_image(map_img, 0, 0)                                               # Draw image inside loop so that we can constantly update the graph
        
        for key in vertex_dictionary:                                           # In the first loop, draw all the vertices and edges
            vertex_dictionary[key].draw_vertex()
            vertex_dictionary[key].draw_edges()
            
        for key in vertex_dictionary:                                           # Do everything else in the second for loop
            
            mouse_vertex = None                                                 # Initialize mouse_vertex to None if it points to nothing
            
            if vertex_dictionary[key].smallest_square(mouse_x(), mouse_y()):    # If the mouse points to a certain vertex, assign that vertex reference to mouse_vertex
                mouse_vertex = vertex_dictionary[key]
            
            
            if mouse_down() and mouse_vertex != None:                           # If the mouse is clicked while it points to a certain vertex:
                start_vertex = mouse_vertex                                     # Assign that vertex reference to start_vertex

                
            if start_vertex != None:                                            # If start_vertex has a value:
                start_vertex.draw_vertex(1, 0, 0)                               # Draw it in red
                
                goal_vertex = mouse_vertex                                      # Assign mouse_vertex's value to goal_vertex (mouse is goal)
                path = bfs(start_vertex, goal_vertex)                           # Call Breadth First Search and assign the path returned to the variable 'path'
                draw_path(path)                                                 # Draw the path by calling 'draw_path'
                
        request_redraw()                                                        # Request redraw and sleep
        sleep(0.02)
            
    

start_graphics(map_plot, "Dartmouth Pathfinder", 1012, 811)                     # Call start_graphics