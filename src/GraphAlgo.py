from GraphAlgoInterface import *
from DiGraph import *
from queue import PriorityQueue
from Node import *
from Edge import *

class GraphAlgo(GraphAlgoInterface):
    def _init_(self):
        self._graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self._graph

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def _dijkstra(id1):
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if (id1 == id2):
            return (0, [id1])
        else:
            self._dijkstra(id1)
            ans = []
            nodeList = self._graph.get_all_v()
            n = nodeList[id2]
            totalWeight = 0
            while(n != None):
                totalWeight=totalWeight+n.get_weight()
                ans.append(0,n)
                n = n.get_father()
            return (totalWeight,ans)

    def plot_graph(self) -> None:
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        return

    def centerPoint(self) -> (int, float):
        return