from queues import Queue

class Graph:
    """A simple graph class."""
    def __init__(self):
        self.adj = {}

    def addNode(self, node):
        """Add a node to the graph."""
        if node not in self.adj:
            self.adj[node] = set()

    def addEdge(self, src, dest):
        """Add an edge to the graph."""
        self.addNode(src)
        self.addNode(dest)
        self.adj[src].add(dest)

    def edge(self, src, dest):
        """Check if there is an edge between two nodes."""
        return dest in self.adj[src]
    
    def nodes(self):
        """Return the nodes of the graph."""
        return self.adj.keys()
    
    def neighbors(self, node):
        """Return the neighbors of a node."""
        return self.adj[node]
    
    def nbNodes(self):
        """Return the number of nodes."""
        return len(self.nodes())
    
    def degree(self, node):
        """Return the degree of a node."""
        return len(self.adj[node])
    
    def deleteEdge(self, src, dest):
        """Delete an edge."""
        self.adj[src].remove(dest)
    
    def nbTotalEdges(self):
        """Return the total number of edges."""
        nb = 0
        for src in self.adj:
            nb += len(self.adj[src])
        return nb

    def show(self):
        """Display the graph."""
        for src in self.adj:
            for dest in self.adj[src]:
                print(src, "->", dest)

    def breadthFirst(self, start):
        """Returns the list of nodes in breadth-first order"""
        if start not in self.nodes():
            raise ValueError("Start not in graph")
        result = []
        queue = Queue(self.nbNodes())
        queue.add(start)
        while not queue.emptyQueue():
            current = queue.remove()
            if current not in result:
                result.append(current)
            for node in self.neighbors(current):
                if node not in result:
                    queue.add(node)
        return result
    
    def distance(self, src, dest, visited=[]):
        """Minimum distance between two nodes."""
        v = visited.copy()
        if src not in self.nodes():
            raise ValueError("Start not in graph")
        if dest not in self.nodes():
            raise ValueError("End not in graph")
        if src == dest:
            return 0
        else:
            distances = []
            for element in self.adj[src]:
                if element == dest:
                    return 1
                if element not in v:
                    v.append(element)
                    distances.append(1 + self.distance(element, dest, v))
            return min(distances) if len(distances) > 0 else float("inf")

    def diameter(self):
        """Diameter of the graph."""
        pass


if __name__ == "__main__":
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 5)
    g.addEdge(3, 6)
    g.addEdge(4, 6)
    g.addEdge(4, 7)
    g.addEdge(5, 6)
    g.addEdge(6, 4)
    g.addEdge(6, 7)

    print("Nodes:", g.nodes())
    print("Edges:", g.nbTotalEdges())
    print("Degree of 3:", g.degree(3))
    print("Neighbors of 3:", g.neighbors(3))
    print("Edge between 3 and 5:", g.edge(3, 5))
    print("Distance between 1 and 6:", g.distance(1, 6))
    print("Distance between 1 and 7:", g.distance(1, 7))