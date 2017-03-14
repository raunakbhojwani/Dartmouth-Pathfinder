#Author: Raunak Bhojwani
#Created: November 10 2014
#Lab4: Dartmouth Pathfinder
#Graph-loading function

from vertex import Vertex                                                   # Import the vertex class

def load_graph(file_name):                                                  # File_name is a parameter passed through load_graph
    
    vertex_dictionary = {}                                                  # Initialize empty dictionary
                                               
    in_file = open(file_name, "r")                                          # Open the file passed in
                         
    for line in in_file:                                                    # For each line, split into a list separated by a semicolon
        data_list = line.strip().split(";") 
        data_list[2] = data_list[2].split(",")                              # Split the x and y coordinate into a list    
        vertex_dictionary[data_list[0]] = Vertex(data_list[0], float(data_list[2][0]), float(data_list[2][1]))    # Create a new Vertex object with name, x and y coordinate from that line and save the reference of the object in the dictionary with the name as the key
        
    in_file.close()                                                         # Make sure to close the file
    
    
    in_file = open(file_name, "r")                                          # Reopen file for second pass
    
    for line in in_file:
        data_list = line.strip().split(";")                                 # For each line, split it into a list like earlier
        data_list[1] = data_list[1].split(",")                              # This time, split the adjacent vertices into a list
        for i in range(len(data_list[1])): 
            data_list[1][i] = data_list[1][i].strip()                                 
            vertex_dictionary[data_list[0]].adjacency_list.append(vertex_dictionary[data_list[1][i]])  # Append the adjacent vertices into the empty 'self.adjacent_list' for each object
        #print vertex_dictionary[data_list[0]].adjacency_list
    in_file.close()
    
    return vertex_dictionary                                                # Close the file and return the address of the dictionary
    
#load_graph("dartmouth_graph.txt")
