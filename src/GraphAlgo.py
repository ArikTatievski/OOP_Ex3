import sys

from GraphAlgoInterface import *
from DiGraph import *
from queue import PriorityQueue
from Node import *
from Edge import *


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph = None):
        if g is not None:
            self._graph = g
        else:
            self._graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def _relax(self, e: Edge) -> None:
        src = e.get_src()
        dest = e.get_dest()
        nodedict = self._graph.get_all_v()
        vs = nodedict[src]
        vd = nodedict[dest]
        if (vd.get_weigth() > vs.get_weigth() + e.get_weight()):
            new_weight = vs.get_weigth() + e.get_weight()
            vd.set_weight(new_weight)
            vd.set_father(vs)

    def _dijkstra(self, id: int) -> None:
        nodedict = self._graph.get_all_v()
        for i in nodedict:
            v = nodedict[i]
            if (i == id):
                v.set_father(None)
                v.set_weight(0)
                continue

            v.set_father(None)
            v.set_weight(sys.maxsize)

        pq = PriorityQueue()
        for node in nodedict:
            v = nodedict[node]
            pq.put(v)

        while not pq.empty():
            temp = pq.get()
            neighbors = self._graph.all_out_edges_of_node()
            for x in neighbors:
                edge = Edge(temp.get_id(), x, neighbors[x])
                self._relax(edge)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if (id1 == id2):
            return (0, [id1])
        else:
            self._dijkstra(id1)
            ans = []
            nodeList = self._graph.get_all_v()
            n = nodeList[id2]
            if (n.get_weight() == sys.maxsize):
                return (sys.maxsize, [])
            totalWeight = 0
            while (n != None):
                totalWeight = totalWeight + n.get_weight()
                ans.append(0, n)
                n = n.get_father()
            return (totalWeight, ans)

    def _isConnected(self) -> bool:
        allNodes = self._graph.get_all_v()
        n: Node = None
        for i in allNodes:
            n = allNodes[i]
            break
        self.BFS(n)
        for i in allNodes:
            if (allNodes[i].get_tag() != 1):
                return False
        self._revBFS(n)
        for i in allNodes:
            if (allNodes[i].get_tag() != 1):
                return False
        return True

    def BFS(self, n: Node) -> None:
        allNodes = self._graph.get_all_v()
        for i in allNodes:
            allNodes[i].set_tag(0)
        queue = []
        n.set_tag(1)
        queue.append(n)
        while (queue):
            s = queue.pop()
            sEdges = self._graph.all_out_edges_of_node(s.get_id())
            for e in sEdges:
                curr: Node = allNodes[e]
                if (curr.get_tag() == 1):
                    continue
                curr.set_tag(1)
                queue.append(curr)
        return

    def _revBFS(self, n: Node) -> None:
        allNodes = self._graph.get_all_v()
        for i in allNodes:
            allNodes[i].set_tag(0)
        queue = []
        n.set_tag(1)
        queue.append(n)
        while (queue):
            s = queue.pop()
            sEdges = self._graph.all_out_rev_edges_of_node(s.get_id())
            for e in sEdges:
                curr: Node = allNodes[e]
                if (curr.get_tag() == 1):
                    continue
                curr.set_tag(1)
                queue.append(curr)
        return

    def plot_graph(self) -> None:
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        self._dijkstra(node_lst[0])
        allNodes = self._graph.get_all_v()
        for i in node_lst:
            if (allNodes[i].get_weight() == sys.maxsize):
                return ([], 0)
        totalWeight = 0
        TSPlist = []
        lstlen = len(node_lst)
        i = 0
        while (i < lstlen - 1):
            curr = self.shortest_path(node_lst[i], node_lst[i + 1])
            totalWeight = totalWeight + curr[0]
            TSPlist.append(curr[1])
        for j in TSPlist:
            TSPlist[j] = TSPlist[j].get_id()
        return (TSPlist, totalWeight)

    def centerPoint(self) -> (int, float):
        if (self._isConnected() == False):
            return (-1, 0)
        ans: Node = None
        ansWeight: float = sys.maxsize
        allNodes = self._graph.get_all_v()
        for i in allNodes:
            n: Node = allNodes[i]
            self._dijkstra(i)
            n_id = 0
            w = 0
            for j in allNodes:
                if [allNodes[j].get_weight() > w]:
                    n_id = j
                    w = allNodes[j].get_weight()
            if (w < ansWeight):
                ansWeight = w
                ans = allNodes[n_id]
        return (ans.get_id(), ansWeight)
