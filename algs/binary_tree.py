

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def add_node(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            focus_node = self.root
            parent = None

            while True:
                parent = focus_node

                if data < focus_node.data:
                    focus_node = focus_node.left

                    if focus_node is None:
                        parent.left = new_node
                        return

                else:
                    focus_node = focus_node.right

                    if focus_node is None:
                        parent.right = new_node
                        return

    def pre_order_traversal(self, focus_node):
  
        if focus_node is not None:
            print(focus_node.data)
            self.pre_order_traversal(focus_node.left)
  
            self.pre_order_traversal(focus_node.right)



tree = BinaryTree()
tree.add_node(1)
tree.add_node(2)
tree.add_node(3)
tree.add_node(2)
tree.add_node(1)


# DFS alg

def forward(root_tree):
    if root_tree is not None:
        print(root_tree.data)
        forward(root_tree.left)
        forward(root_tree.right)

forward(tree.root.right)