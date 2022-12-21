from graph import *

def bfs(graph, source):
    """
    Function to print a BFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """
    print("start: {} ".format(source), end="")
    temp = graph.graph[source]
    while temp:
        print("-> {} ".format(temp.vertex), end="")
        temp = temp.next
    

graph = Graph(10)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(1,4)
graph.add_edge(1,5)

bfs(graph, 1)