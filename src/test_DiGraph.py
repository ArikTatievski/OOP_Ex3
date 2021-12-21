from unittest import TestCase
from DiGraph import *
from Node import *
from Edge import *


class TestDiGraph(TestCase):

    def test_v_size(self):
        g = DiGraph()
        g.add_node(0, (1, -1))
        g.add_node(1, (2, 3))
        g.add_node(2, (4, 6))
        g.add_node(3, (3, 13))
        g.add_node(4, (1, -5))
        g.add_node(5, (7, 7))
        g.add_node(6, (8, 2))
        self.assertEqual(7,g.v_size())
        g.remove_node(6)
        self.assertEqual(6,g.v_size())

    def test_e_size(self):
        g = DiGraph()
        g.add_node(0, (1, -1))
        g.add_node(1, (2, 3))
        g.add_node(2, (4, 6))
        g.add_node(3, (3, 13))
        g.add_node(4, (1, -5))
        g.add_node(5, (7, 7))
        g.add_node(6, (8, 2))
        g.add_edge(0,1,1)
        g.add_edge(0, 2, 1)
        g.add_edge(1, 4, 1)
        g.add_edge(5, 4, 1)
        g.add_edge(2, 4, 1)
        g.add_edge(5, 2, 1)
        g.add_edge(6, 5, 1)
        g.add_edge(2, 6, 1)
        g.add_edge(2, 3, 1)
        g.add_edge(3, 6, 1)
        self.assertEqual(10,g.e_size())
        g.remove_edge(2,3)
        g.remove_edge(3,6)
        self.assertEqual(8,g.e_size())

    def test_get_mc(self):
        self.fail()

    def test_add_edge(self):
        self.fail()

    def test_add_node(self):
        self.fail()

    def test_remove_node(self):
        self.fail()

    def test_remove_edge(self):
        self.fail()
