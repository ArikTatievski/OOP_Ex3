class Node:
    def __init__(self, id: int, pos: tuple):
        self._id = id
        self._pos = pos
        self._father = None
        self._tag = 0
        self._weight = 0

    def get_id(self):
        return self._id

    def get_pos(self):
        return self._pos

    def get_tag(self):
        return self._tag

    def get_weight(self):
        return self._weight

    def get_father(self):
        return self._father

    def set_tag(self, tag: int):
        self._tag = tag

    def set_weight(self, weight: float):
        self._weight = weight

    def set_father(self, father):
        self._father = father

    def __lt__(self, other):
        return self._weight < other.get_weight()

    def __repr__(self):
        return f"Node {self.get_id()} located at {self.get_pos()}"
