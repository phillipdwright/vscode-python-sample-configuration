from .node import Node


class NodeFactory:
    lower_bound=0
    upper_bound=128

    def __init__(self, rng, lower_bound=None, upper_bound=None):
        self._random = rng
        if lower_bound is not None:
            self.lower_bound = lower_bound
        if upper_bound is not None:
            self.upper_bound = upper_bound

    def create_root_node(self):
        return self._create_node(parent=None)

    def create_children_for_each(self, nodes, child_count):
        for node in nodes:
            for _ in range(child_count):
                yield self._create_node(parent=node)

    def _create_node(self, parent):
        value = self._generate_value()
        return Node(value, parent)

    def _generate_value(self):
        return self._random.randint(self.lower_bound, self.upper_bound)
