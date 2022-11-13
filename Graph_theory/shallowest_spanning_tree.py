
class Vertex:

    def __init__(self, v):
        self.v = v
        self.adj = []

    def add_edge(self,u,w):
        self.adj.append((u,w))


class Graph:

    def __init__(self, gfile):
        (self.n,edge_lst) = (self.__readFile__(gfile))

        print(edge_lst)
        self.graph = [None]*self.n
        self.insert_vertex(edge_lst)
        
        #print(self.graph[3].adj)
        
    def __readFile__(self,gfile):
        file = open(gfile)
        text = file.read()

        text = text.split("\n")

        n = int(text[0])

        for i in range(len(text)):
            text[i] = text[i].split(' ')

        text = text[1:]
        
        return n,text[:-1]

    def insert_vertex(self, lst):

        graph = self.graph      
        
        for i in lst:
            vertex_1 = int(i[0])
            vertex_2 = int(i[1])
            weight_edge = int(i[2])

            if graph[vertex_1] == None:
                graph[vertex_1] = Vertex(vertex_1)

            if graph[vertex_2] == None:
                graph[vertex_2] = Vertex(vertex_2)

            graph[vertex_1].add_edge(vertex_2,weight_edge)
            graph[vertex_2].add_edge(vertex_1,weight_edge)
             
        self.graph = graph

    def BFS_depth(self, start):

        spanning_tree = []
        
        visited = [False]*len(self.graph)
        queue = []
        depth_queue = []
    
        queue.append(start)
        visited[start] = True
        depth_queue.append(0)
        
        while queue:
            
            start = queue.pop(0)
            spanning_tree.append(start)
            depth = depth_queue[-1]
            
            for i in self.graph[start].adj:
                
                if visited[i[0]] == False:
                    
                    queue.append(i[0])
                    depth_queue.append(depth+1)
                    visited[i[0]] = True

        return depth_queue[-1]
        
    def shallowest_spanning_tree(self):

        shallowest_depth = (len(self.graph),None)
        
        for index in range(len(self.graph)):
            depth = self.BFS_depth(index)
            print(index,depth)

            if depth < shallowest_depth[0]:
                shallowest_depth = (depth, index)
        

        return shallowest_depth
            

#this = Graph("fancy_graph")
#print(this.shallowest_spanning_tree())
