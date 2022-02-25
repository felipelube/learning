class Node:
    def __init__(self, k: int):
        self.k = k
        self.left: Node = None
        self.right: Node = None


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)


def inorder(node: Node, lyst=[]):
    if node is None:
        return

    inorder(node.left)
    lyst.append(node.k)
    inorder(node.right)

    return lyst


assert(inorder(root) == [20, 10, 40, 30, 50])


def preorder(node: Node, lyst=[]):
    if node is None:
        return

    lyst.append(node.k)
    preorder(node.left)
    preorder(node.right)

    return lyst


assert(preorder(root) == [10, 20, 30, 40, 50])
