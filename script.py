class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        new_children = []
        for child in self.children:
            if child.value != child_node.value:
                new_children.append(child)
        self.children = new_children