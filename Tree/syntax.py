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


def level_of_key(root, key):

    if root.data == key:
        return "yes"


def serach_node(root, key):

    if root is None:
        return False

    if root.data == key:
        return True

    if root.data > key:
        return serach_node(root.left, key)
    else:
        return serach_node(root.right, key)


if __name__ == "__main__":
    root = None

    keys = [50, 30, 20, 40, 70, 60, 80, 100]

    for key in keys:
        root = insert(root, key)

    print("In-order traversal of the tree:")
    inorder_traversal(root)
    print()
    print("Depth:")
    print(depth_of_binary_tree(root))
    print()
    print("Search")
    print(serach_node(root, 100))
