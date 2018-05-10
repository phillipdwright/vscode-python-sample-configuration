from unittest import TestCase

from trees.node import Node


class NodeTest(TestCase):
    def test__node__before_children_added__has_no_children(self):
        node_before_children_added = Node(0)

        has_children = bool(node_before_children_added.children)

        assert not has_children

    def test__node__given_parent__adds_new_node_to_parent(self):
        parent = Node(0)
        
        child = Node(1, parent=parent)

        assert child in parent.children

    def test__add_child_to_parent__adds_node_to_parents_children(self):
        parent = Node(0)
        child = Node(1)

        parent.add_child(child)

        assert child in parent.children
