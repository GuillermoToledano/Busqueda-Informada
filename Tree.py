class Node:
    def __init__(self, data, son=None):
        self.data = data
        self.son = None
        self.father = None
        self.cost = None
        self.set_son(son)

    def set_son(self, son):
        self.son = son
        if self.son is not None:
            for s in self.son:
                s.father = self

    def get_son(self):
        return self.son

    def get_father(self):
        return self.father

    def set_father(self, father):
        self.father = father

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_cost(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

    def equal(self, node):
        if self.get_data() == node.get_data():
            return True
        else:
            return False

    def on_list(self, node_list):
        listed = False
        for n in node_list:
            if self.equal(n):
                listed = True
        return listed

    def __str__(self):
        return str(self.get_data())
