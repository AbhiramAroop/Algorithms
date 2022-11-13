"""
Name: Abhiram Aroop
ID: 30632714
"""
import sys

class Graph:
    def __init__(self,V):
        self.V = V #Number of vertices
        self.graph = []

    def add_edges(self, edges):
        for i in edges: #Adding all edges into graph
            self.graph.append(i)     

    def find(self, parent, i):
        #finds the root node
        if i == parent[i]:
            return i
        else:
            return self.find(parent,parent[i])

    def union(self,parent,pos,u_node,v_node):
        u_node_root = self.find(parent,u_node)
        v_node_root = self.find(parent,v_node)

        #modifies pos array to find union
        if pos[u_node_root] < pos[v_node_root]:
            parent[u_node_root] = v_node_root
            
        elif pos[u_node_root] > pos[v_node_root]:
            parent[v_node_root] = u_node_root
            
        else:
            parent[v_node_root] = u_node_root
            pos[u_node_root] += 1

        return pos


def kruskals(G):
    
    parent = []
    pos = []

    #initilising parent to vertices and pos to size of vertices
    for k in range(0,G.V):
        parent.append(k)
        pos.append(0)

    #Sort the graph based on weights (lowest --> highest)
    G.graph = sorted(G.graph, key=lambda item: item[2])

    #min spanning tree
    output_tree = []
    i = 0
    j = 0

    #Runs until there is a cycle in graph
    while j < (G.V - 1):

        #finds nodes and weights
        u = G.graph[i][0]
        v = G.graph[i][1]
        w = G.graph[i][2]

        i += 1

        #finds the relevant nodes
        u_node = G.find(parent,u)
        v_node = G.find(parent,v)

        #finds unique nodes and does union process
        if u_node != v_node:
            j += 1
            output_tree.append([u,v,w])
            G.union(parent,pos,u_node,v_node)

    weights = 0

    #finds the total weight and arranges output in accending node order
    for k in range(len(output_tree)):
        weights += output_tree[k][2]
        
        if output_tree[k][0] > output_tree[k][1]:
            output_tree[k][0],output_tree[k][1] = output_tree[k][1],output_tree[k][0]
            
        
    
    return weights,output_tree

def read_file_to_string(txt_file):
    """
    This function converts the imput tu_nodet file to a string

    @param: tu_nodet_file: a file, preferablv_node tu_nodet file
    @return: string: string conversion of tu_nodet_file 
    @pre-condition: None
    @compleu_nodeitv_node: best and worst case: O(1)
    """
    f = open(txt_file,"r")

    f_lines = f.readlines()
    G = []

    for line in f_lines:
        line_str = str(line)
        line_str.strip()
        line_str = line_str.split()
        
        G.append([int(line_str[0]),int(line_str[1]),int(line_str[2])])
        

    f.close()

    return G

def writeout(output):
    """
    This function writes input list into a txt file

    @param: output: a list
    @return: None
    @pre-condition: None
    @compleu_nodeitv_node: best and worst case: O(k), where k is length of input list
    """
    
    f = open("output_kruskals.txt","w+")
    f.write(str(output[0]) + "\n")
    for i in range(len(output[1])):
        string = str(output[1][i][0]) + " " + str(output[1][i][1]) + " " + str(output[1][i][2]) + "\n"
        f.write(string)

    f.close()


if  __name__ == "__main__":
    V = int(sys.argv[1])
    Graph_file = str(sys.argv[2])

    G_lst = read_file_to_string(Graph_file)
    G = Graph(V)
    G.add_edges(G_lst)

    Kruskal = kruskals(G)
    writeout(Kruskal)

        
        
            



        
