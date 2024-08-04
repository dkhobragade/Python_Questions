# Initiliazed he Node
class Node:
    def __init__(self, head, next):
        self.data = head
        self.next = next


# To Insert the new Node at the beginning of the node
def insert_at_beginning(head, next):
    return Node(head, next)


# To Insert the new Node at the end of the node
def insert_at_end(head):
    cur = head
    while cur.next != None:
        cur = cur.next
    cur.next = Node(50, None)


# To Insert the new Node at the given postion
def insert_at_given_pos(head, i):
    cur = head
    count = 0
    while i != count + 1:
        count = count + 1
        cur = cur.next
    cur.next = Node(25, cur.next)


# To print the linked list
def print_linked_List(head):
    cur = head
    while cur:
        print(str(cur.data), "-->", end=" ")
        cur = cur.next
    print("None")


node4 = insert_at_beginning(40, None)
node3 = insert_at_beginning(30, node4)
node2 = insert_at_beginning(20, node3)
node1 = insert_at_beginning(10, node2)

insert_at_end(node1)
insert_at_given_pos(node1, 2)
print_linked_List(node1)
