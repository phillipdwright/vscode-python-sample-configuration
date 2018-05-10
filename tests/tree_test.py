from unittest import TestCase

from trees.node import Node
from trees.tree import Tree, EmptyTree


class TreeTest(TestCase):
    def test__tree__given_root__is_not_empty(self):
        root = Node(0)
        tree = Tree(root)

        assert not tree.is_empty()

    def test__tree__given_no_root__is_empty(self):
        tree = Tree(root=None)

        assert tree.is_empty()

    def test__empty_tree__is_empty(self):
        empty_tree = EmptyTree()

        assert empty_tree.is_empty()
