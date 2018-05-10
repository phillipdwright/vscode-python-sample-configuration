from collections import namedtuple

RowSum = namedtuple('RowSum', 'row_number sum')


class TreeTraverser:
    def find_maximum_row_sum(self, tree):
        row_sums = self.calculate_row_sums(tree)
        return max(row_sums, key=lambda rs: rs.sum)

    def calculate_row_sums(self, tree):
        if tree.is_empty():
            return ()

        level = 1
        nodes_in_level = [tree.root]

        while nodes_in_level:
            level_sum = sum(node.value for node in nodes_in_level)
            yield RowSum(level, level_sum)

            level += 1
            nodes_in_level = [child for node in nodes_in_level for child in node.children]
