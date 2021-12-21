from GraphInterface import *
from Node import *
from Edge import *

class DiGraph(GraphInterface):
    def __init__(self):
        self._nodes = {}
        self._edges = {}
        self._nodeSize = 0
        self._edgeSize = 0
        self._MCsize = 0
        self.arik =0


    def v_size(self) -> int:
        return self._nodeSize

    def e_size(self) -> int:
        return self._edgeSize

    def get_mc(self) -> int:
        return self._MCsize

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self._nodes.keys():
            return False
        if id2 not in self._nodes.keys():
            return False
        for e in self._edges[id1]:
            if (e.get_dest == id2):
                return False

        curr = Edge(id1,id2,weight)
        self._edges[id1].append(curr)
        self._edgeSize=self._edgeSize+1
        self._MCsize = self._MCsize+1


    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        curr = Node(node_id,pos)
        if node_id in self._nodes.keys():
            return False
        self._nodes[node_id] = curr
        self._edges[node_id] = []
        self._nodeSize = self._nodeSize+1
        self._MCsize = self._MCsize + 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self._nodes.keys():
            return False
        edges = len(self._edges[node_id])
        self._edges.pop(node_id)
        self._nodeSize = self._nodeSize -1
        self._edgeSize=self._edgeSize-edges
        self._MCsize = self._MCsize +edges +1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        for e in self._edges[node_id1]:
            if(e.get_dest() == node_id2):
                self._edges[node_id2].remove(e)
                self._edgeSize = self._edgeSize-1
                self._MCsize = self._MCsize + 1
                return True
        return False