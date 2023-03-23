from stack_array import *


class vertex:
    def __init__(self, adjacencies: List):
        self.in_degree = 0
        self.adjacencies = adjacencies

    # def __repr__(self) -> str:
    #     return f"vertex({self.adjacencies}, {self.in_degree})"

    def get_adj(self) -> List:
        return self.adjacencies

    def get_in_degrees(self) -> int:
        return self.in_degree

    def add_in_degree(self) -> None:
        self.in_degree += 1

    def sub_in_degree(self) -> None:
        self.in_degree -= 1


def tsort(vertices: List) -> str:
    """
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.
    *
    * Raises a ValueError if:
    *   - vertices is emtpy with the message "input contains no edges"
    *   - vertices has an odd number of vertices (incomplete pair) with the
    *     message "input contains an odd number of tokens"
    *   - the graph contains a cycle (isn't acyclic) with the message
    *     "input contains a cycle"
    """
    if len(vertices) == 0:
        raise ValueError("input contains no edges")
    if len(vertices) % 2 == 1:
        raise ValueError("input contains an odd number of tokens")

    adj_list = adjacent_list(vertices)
    stack = Stack(50)
    t_list = ''
    for node in adj_list:
        if adj_list[node].get_in_degrees() == 0:
            stack.push(node)

    while not stack.is_empty():
        node_name = stack.pop()
        node = adj_list[node_name]
        node.sub_in_degree()
        t_list += f'{node_name}\n'

        for adj_node in node.get_adj():
            adj_list[adj_node].sub_in_degree()
            if adj_list[adj_node].get_in_degrees() == 0:
                stack.push(adj_node)

    for node in adj_list:
        if adj_list[node].get_in_degrees() > 0:
            raise ValueError("input contains a cycle")
    return t_list


def adjacent_list(vertices: List) -> dict:
    adj_list = {}
    pairs = []
    for i in range(0, len(vertices) - 1, 2):
        pairs.append([vertices[i], vertices[i + 1]])

    for outgoing, incoming in pairs:
        # print(f"from: {outgoing}, to: {incoming}")
        # if node not in adj list at it and what it points to
        if outgoing not in adj_list:
            adj_list[outgoing] = vertex([incoming])
        # if node alr in adj list updates its adj nodes
        else:
            adj = adj_list[outgoing].get_adj()
            adj.append(incoming)
            adj_list[outgoing].adjacencies = adj
        # if the incoming node not in initialize an empty adj list
        # and add an in degree from outgoing node
        if incoming not in adj_list:
            adj_list[incoming] = vertex([])
            adj_list[incoming].add_in_degree()
        # update in degree from outgoing node
        else:
            adj_list[incoming].add_in_degree()
    return adj_list
