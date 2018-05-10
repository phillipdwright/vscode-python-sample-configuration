class Tree:
    def __init__(self, root):
        self.root = root

    def is_empty(self):
        return self.root is None


class EmptyTree(Tree):
    def __init__(self):
        super().__init__(None)
