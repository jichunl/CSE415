# CSE 417 Winter 2019
# Assignment 2
# Jichun Li 1531264

import sys  
import os.path
import time
   
from collections import defaultdict 
   

class Graph: 
   
    def __init__(self, vertices): 
        # No. of vertices 
        self.V = vertices  
          
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
          
        # time is used to find discovery times 
        self.Time = 0 
          
        # Count is number of biconnected components 
        self.count = 0 
   
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v)  
        self.graph[v].append(u) 
  
    '''A recursive function that finds and prints strongly connected 
    components using DFS traversal 
    u --> The vertex to be visited next 
    disc[] --> Stores discovery times of visited vertices 
    low[] -- >> earliest visited vertex (the vertex with minimum 
               discovery time) that can be reached from subtree 
               rooted with current vertex 
    st -- >> To store visited edges'''
    def BCCUtil(self, u, parent, low, disc, st, art_pt): 
  
        # Count of children in current node  
        children = 0
  
        # Initialize discovery time and low value 
        disc[u] = self.Time 
        low[u] = self.Time 
        self.Time += 1
  
  
        # Recur for all the vertices adjacent to this vertex 
        for v in self.graph[u]: 
            # If v is not visited yet, then make it a child of u 
            # in DFS tree and recur for it 
            if disc[v] == -1 : 
                parent[v] = u 
                children += 1
                st.append((u, v)) # store the edge in stack 
                self.BCCUtil(v, parent, low, disc, st, art_pt) 
  
                # Check if the subtree rooted with v has a connection to 
                # one of the ancestors of u 
                # Case 1 -- per Strongly Connected Components Article 
                low[u] = min(low[u], low[v]) 
  
                # If u is an articulation point, pop  
                # all edges from stack till (u, v) 
                if parent[u] == -1 and children > 1 or parent[u] != -1 and low[v] >= disc[u]: 
                    art_pt.append(u)
                    self.count += 1 # increment count 
                    w = -1
		    print("Biconnect component " + str(self.count) + " : ")
                    while w != (u, v): 
                        w = st.pop()
                        print w, 
                    print"" 
              
            elif v != parent[u] and low[u] > disc[v]: 
                '''Update low value of 'u' only of 'v' is still in stack 
                (i.e. it's a back edge, not cross edge). 
                Case 2  
                -- per Strongly Connected Components Article'''
  
                low[u] = min(low [u], disc[v]) 
      
                st.append((u, v)) 
  
  
    # The function to do DFS traversal.  
    # It uses recursive BCCUtil() 
    def BCC(self): 
          
        # Initialize disc and low, and parent arrays 
        disc = [-1] * (self.V) 
        low = [-1] * (self.V) 
        parent = [-1] * (self.V) 
        st = [] 
	art_pt = [] 
	
	start_time = time.time()
	 
        # Call the recursive helper function to  
        # find articulation points 
        # in DFS tree rooted with vertex 'i' 
        for i in range(self.V): 
            if disc[i] == -1: 
                self.BCCUtil(i, parent, low, disc, st, art_pt) 
  
            # If stack is not empty, pop all edges from stack 
            if st: 
                self.count = self.count + 1
 		print("Biconnect component " + str(self.count) + " : ") 
                while st: 
                    w = st.pop() 
                    print w, 
                print ""   
	print ""
	print ("Ariculation Points in the graph: " + str(art_pt))
	print ""
	print ("Total run time: " + str((time.time() - start_time) * 1000000) + " ms")

# Create a graph using file from given argument
if len(sys.argv) == 2:
	if os.path.isfile(sys.argv[1]):
		with open(sys.argv[1], 'r') as test_case:
			num_nodes = int(test_case.readline())
			g = Graph(num_nodes)
			print ("Number of Nodes: " + str(num_nodes))
			num_edges = 0
			while 1: 
				str_edge = test_case.readline()
				if not str_edge: 
					break
				lst_edge = str_edge.split()
				vtx_a = int(lst_edge[0])
				vtx_b = int(lst_edge[1])
				g.addEdge(vtx_a,vtx_b)
				num_edges = num_edges + 1
			print("Number of Edges: " + str(num_edges))	
	else:
		print("File not exist.")
		sys.exit()
else:
	print("Please provide one test case.")
	sys.exit()


'''
g = Graph(16) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 12) 
g.addEdge(0, 15) 
g.addEdge(1, 2) 
g.addEdge(1, 4) 
g.addEdge(1, 5) 
g.addEdge(1, 12) 
g.addEdge(2, 4) 
g.addEdge(2, 5) 
g.addEdge(2, 10) 
g.addEdge(3, 7) 
g.addEdge(3, 8) 
g.addEdge(3, 10) 
g.addEdge(3, 11)
g.addEdge(3, 13) 
g.addEdge(3, 14) 
g.addEdge(4, 6) 
g.addEdge(4, 9) 
g.addEdge(5, 12) 
g.addEdge(6, 9) 
g.addEdge(7, 8) 
g.addEdge(7, 11) 
g.addEdge(7, 13) 
g.addEdge(7, 14) 
g.addEdge(8, 11) 
g.addEdge(8, 13) 
g.addEdge(8, 14) 
g.addEdge(11, 13) 
g.addEdge(11, 14) 
g.addEdge(12, 15)
'''
g.BCC(); 

