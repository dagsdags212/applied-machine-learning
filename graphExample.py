from graphTheory import *
from DFS import DFS, shortestPath

adjacency_list = {
    'Boston': ['Providence', 'New York'],
    'Providence': ['Boston', 'Chicago'],
    'New York': ['Chicago'],
    'Chicago': ['Denver', 'Phoenix'],
    'Denver': ['Phoenix', 'New York'],
    'Los Angeles': ['Boston'],
    'Phoenix': []
}

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))

    return g

def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint = True)

    if sp != None:
        print('Shortest path from ', source, 'to', destination, 'is', sp)
    else:
        print('There is no path from', source, 'to', destination)

testSP('Boston', 'Chicago')