#Author: Raunak Bhojwani
#Created: November 10 2014
#Lab4: Dartmouth Pathfinder
#Class definition for a vertex

from cs1lib import *

VERTEX_RADIUS = 5.5
EDGE_WIDTH = 3.5


class Vertex:                                                       #Class - Vertex
    def __init__(self, name, x, y):
        
        self.name = name                                            # Initialize the name, x and y coordinate in the constructor
        self.x = x
        self.y = y
        
        self.adjacency_list = []                                    # Initialize empty list for adjacent vertices
        
    def __str__(self):
        
        i = len(self.adjacency_list)
        temp = ""                                                   # Initialize 'temp' as a string
        for vertex in self.adjacency_list:                          # Use a for loop to make sure to get all vertices in 
            temp = temp + vertex.name  
            if i > 1:                                               # This makes sure that the last variable doesn't have a comma
                temp = temp + ", "                                   
                i -= 1
            
        return self.name + "; Location: " + str(self.x) +", " + str(self.y) +"; Adjacent vertices: " + temp    # Return in the order given by Professor HF
        
    def draw_vertex(self, r=0, g=0, b=1):                           # Function to draw the vertex
        disable_stroke()                                            # Disables stroke, which is important for the graph
        set_fill_color(r, g, b)                                     # set the color and draw a circle with VERTEX_RADIUS    
        draw_circle(self.x, self.y, VERTEX_RADIUS)
        
    def draw_edges(self, r=0, g=0, b=1):                            # Function to draw the edges between self and all vertices in the adjacency list
        enable_stroke()                                             # Enables stroke so line is visible
        set_stroke_color(r, g, b)                                   # Set color, width and then, in a for loop, draw a line between self and every other adjacent vertex
        set_stroke_width(EDGE_WIDTH)
        for point in self.adjacency_list:
            draw_line(self.x, self.y, point.x, point.y)
            
    def draw_path(self, vertex, r=1, g=0, b=0):                     # Function that allows a path(edge) to be drawn between two vertices
        if vertex != None:
            self.draw_vertex(1, 0, 0)                               # Draw the vertex in red
            vertex.draw_vertex(1, 0, 0)
            
            enable_stroke()                                         # enable stroke
            set_stroke_color(r, g, b)
            set_stroke_width(EDGE_WIDTH)
            draw_line(self.x, self.y, vertex.x, vertex.y)           # draw the edge
        
    def smallest_square(self, x, y):                                # Return a boolean indicating whether the mouse is pointing to the self vertex or not
        return self.x - VERTEX_RADIUS <= x <= self.x + VERTEX_RADIUS and self.y - VERTEX_RADIUS <= y <= self.y + VERTEX_RADIUS
        