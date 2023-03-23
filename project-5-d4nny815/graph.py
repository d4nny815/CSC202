from typing import Any, List, Optional
# from stack_array import *  # Needed for Depth First Search
from queue_array import *  # Needed for Breadth First Search


class Vertex:
    """Add additional helper methods if necessary."""

    def __init__(self, key: Any) -> None:
        """Add other attributes as necessary"""
        self.id = key
        self.adjacent_to: List = []
        self.color: Any = None

    # def __repr__(self) -> str:
    #     return f'Vertex({self.id}, {self.adjacent_to})'

    def add_adj(self, vertex: Any) -> None:
        old_adj_to: List = self.adjacent_to
        old_adj_to.append(vertex)
        self.adjacent_to = sorted(old_adj_to)
    
    def get_adj(self) -> List:
        return self.adjacent_to
        
        
    def get_color(self) -> str:
        return self.color if self.color else 'None'
    
    def change_color(self, color: str) -> None:
        self.color = color


class Graph:
    """Add additional helper methods if necessary."""

    def __init__(self, filename: str):
        """reads in the specification of a graph and creates a graph using an adjacency list representation.
           You may assume the graph is not empty and is a correct specification.  E.g. each edge is
           represented by a pair of vertices.  Note that the graph is not directed so each edge specified
           in the input file should appear on the adjacency list of each vertex of the two vertices associated
           with the edge."""
        self.vertices: dict = {}
        pairs = self.get_node_pairs(filename)
        for pair in pairs:
            self.add_edge(pair[0], pair[1])

    def get_node_pairs(self, filename: str) -> List:
        list: List = []
        with open(filename, 'r') as file:
            for line in file:
                line = line.rstrip()
                list.append(line.split())

        return list

    def add_vertex(self, key: Any) -> None:
        """Add vertex to graph, only if the vertex is not already in the graph."""
        if key not in self.vertices:
            self.vertices[key] = Vertex(key)
        return

    def get_vertex(self, key: Any) -> Optional[Vertex]:
        """Return the Vertex object associated with the id. If id is not in the graph, return None"""
        if key not in self.vertices:
            return None
        else:
            return self.vertices[key].id

    def add_edge(self, v1: Any, v2: Any) -> None:
        """v1 and v2 are vertex id's. As this is an undirected graph, add an
           edge from v1 to v2 and an edge from v2 to v1.  You can assume that
           v1 and v2 are already in the graph"""
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add_adj(v2)
        self.vertices[v2].add_adj(v1)

    def get_vertices(self) -> List:
        """Returns a list of id's representing the vertices in the graph, in ascending order
           Note: Results of Python sort on the list satisfies ascending order requirement"""
        v_list = []
        for vertex in self.vertices:
            v_list.append(self.vertices[vertex].id)
        return sorted(v_list)

    def conn_components(self) -> List:
        """Returns a list of lists.  For example, if there are three connected components
           then you will return a list of three lists.  Each sub list should contain the
           vertices (in 'Python List Sort' order) in the connected component represented by that list.
           The overall list of lists should also be in order based on the first item of each sublist.
           This method MUST use Depth First Search logic!"""
        
        vertices = self.get_vertices()
        connected = []
        visited = {v: False for v in vertices}
        
        for v in vertices:
            if not visited[v]:
                temp: List = []
                connected.append((self.dfs(temp, self.vertices[v], visited)))
                
        return connected
    
    def dfs(self, temp: List, vertex: Vertex, visited: dict) -> List:
        '''Helper method for conn_components'''
        visited[vertex.id] = True
        temp.append(vertex.id)
        
        for v in vertex.get_adj():
            if not visited[v]:
                temp = self.dfs(temp, self.vertices[v], visited)
        return sorted(temp)
        

    def is_bipartite(self) -> bool:
        '''Returns True if the graph is bicolorable and False otherwise.
        This method MUST use Breadth First Search logic!'''
        vertices = self.get_vertices()
        queue = Queue(len(vertices))
        
        for v in vertices:
            vertex: Vertex = self.vertices[v]
            if vertex.color is None:
                vertex.change_color('red')
                queue.enqueue(vertex)
                
            while not queue.is_empty():
                current: Vertex = queue.dequeue()
                for adj in current.get_adj():
                    adj_vertex: Vertex = self.vertices[adj]
                    if adj_vertex.color is None:
                        if current.get_color() == 'red':
                            adj_vertex.change_color('black')
                        else:
                            adj_vertex.change_color('red')
                        queue.enqueue(adj_vertex)
                    elif adj_vertex.get_color() == current.get_color():
                        return False
        return True

        
        
        
