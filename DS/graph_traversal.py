from .queue import Queue

def bfs(g, start):
    """
    time: O(V + E)
    space: O(V)
    """
    start.setDistance(0)
    start.setPred(None)
    vertQueue  = Queue()
    vertQueue.enqueue(start)

    while vertQueue.size() > 0:
        currentVertex = vertQueue.dequeue()
        for nbr in currentVertex.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('grey')
                nbr.setDistance(currentVertex.getDistance() + 1)
                nbr.setPred(currentVertex)
                vertQueue.enqueue(nbr)
        currentVertex.setColor('black')

def dfs(g):
    """
    time: O(V+E)
    space: O(V) for stack
    """
    for aVertex in g.getVertices():
        aVertex.setColor('white')
        aVertex.setPred(-1)

    for aVertex in g.getVertices():
        if aVertex.getColor() == 'white':
            dfsVisit(aVertex)

def dfsVisit(startVertex):
    startVertex.setColor('grey')
    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)
            dfsVisit(nextVertex)
    startVertex.setColor('black')


def topologicalSort(digraph):
    """
    Time: O(M + N), where M --> No of edges, N --> No of nodes
    Space: O(N)
    
    """

    indegrees = {node: 0 for node in digraph}
    for node in digraph:
        for nbr in digraph[node]:
            indegrees[nbr] += 1

    nodesWithNoIncomingEdges = []
    for node in digraph:
        if indegrees[node] == 0:
            nodesWithNoIncomingEdges.append(node)

    topologicalOrdering = []
    while len(nodesWithNoIncomingEdges) > 0:
        node = nodesWithNoIncomingEdges.pop()
        topologicalOrdering.append(node)

        for nbr in digraph[node]:
            indegrees[nbr] -= 1
            if indegrees[nbr] == 0:
                nodesWithNoIncomingEdges.append(nbr)

    if len(topologicalOrdering) == len(digraph):
        return topologicalOrdering
    else:
        raise Exception("Cycle has detected!")

    

    