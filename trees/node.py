class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.children = set()
        if parent:
            parent.add_child(self)

    def add_child(self, child):
        self.children.add(child)

    def __repr__(self):
        return '<Node: {value}>'.format(value=self.value)
