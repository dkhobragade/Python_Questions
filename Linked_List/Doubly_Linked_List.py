# Initiliazed the Node
class Node:
    def __init__(self, head, prev, next):
        self.data = head
        self.prev = prev
        self.next = next


# To Insert the new Node at the beginning of the node
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    new_node.prev = new_node

    return new_node


def print_linked_list(head):
    cur = head
    while cur:
        print(str(cur.data))


node4 = Node(40)
node3 = insert_at_beginning(node4, 30)
node2 = insert_at_beginning(node3, 20)
node1 = insert_at_beginning(node2, 30)
