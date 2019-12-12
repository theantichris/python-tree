class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return str(self.value)

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child is not child_node]

    def traverse(self):
        print(self)
        for child in self.children:
            print(child)


root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")

root.add_child(first_child)
root.add_child(second_child)

root.traverse()
