from .tree import EmptyTree, Tree


class TreeBuilder:
    children_per_node=2
    levels=5

    def __init__(self, node_factory):
        self._node_factory = node_factory

    def build(self):
        if self.levels < 1:
            return EmptyTree()

        root = self._node_factory.create_root_node()
        nodes_on_level = [root]

        for levels_already_created in range(1, self.levels):
            self._reduce_upper_bound_by_factor_of_child_count()
            nodes_on_level = list(self._node_factory.create_children_for_each(
                nodes_on_level,
                self.children_per_node
            ))

        return Tree(root)

    def _reduce_upper_bound_by_factor_of_child_count(self):
        self._node_factory.upper_bound //= self.children_per_node
