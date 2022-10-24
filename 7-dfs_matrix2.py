class GraphAM:
    def __init__(self,Nodes):
        self.adj_matrix=[[0]*(Nodes+1) for x in range(Nodes+1)]
    
    def add_edge(self,x,y):
        self.adj_matrix[x][y]=1
    
    def return_graph(self):
        return self.adj_matrix

#Just taking inputs
nodes=int(input())
edges=int(input())
graph=GraphAM(nodes)
connection=[]
for _ in range(edges):
    li=list(map(int, input().split()))
    connection.append(li)
for connect in connection:
    graph.add_edge(connect[0], connect[1])
grp=graph.return_graph()
#print(grp)



#visited array to keep track of visited nodes
visited=[False]*(nodes+1)
#DFS method
def DFS(node):
    visited[node]=True #Making current node as visited
    
    print(node, "--->", end="") #Printing the traversing nodes
    
    for i in range(len(grp[node])):
        
        if grp[node][i]==1 and visited[i]==False:
            
            DFS(i)

DFS(1) #Calling DFS on node 1

'''
directed graph
Sample Input
7
8
1 2
2 7
2 4
3 4
4 6
5 4
5 3
7 5
'''