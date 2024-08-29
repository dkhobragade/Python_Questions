class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def inorder_traversal(root):
    if root:

        inorder_traversal(root.left)

        print(root.data, end=" ")

        inorder_traversal(root.right)


def depth_of_binary_tree(root):

    if root == None:
        return 0
    return 1 + max(depth_of_binary_tree(root.left), depth_of_binary_tree(root.right))


if __name__ == "__main__":
    root = None

    keys = [50, 30, 20, 40, 70, 60, 80, 100]

    for key in keys:
        root = insert(root, key)

    print("In-order traversal of the tree:")
    inorder_traversal(root)
    print("Depth:")
    print(depth_of_binary_tree(root))
