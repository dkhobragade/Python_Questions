# Initiliazed the Node
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


# To Delete the start Node
def delete_at_beginning(head):
    return head.next


# To Delete the end Node
def delete_at_end(head):
    cur = head
    while cur.next.next != None:
        cur = cur.next
    cur.next = None
    return head


# To Delete the given position Node
def delete_at_pos(head, i):
    cur = head
    count = 0
    while i != count + 1:
        count += 1
        cur = cur.next
    cur.next = cur.next.next
    return head


# Middle of the Node using Array
def middle_linked_list_array(head):
    cur = head
    a = []
    while cur:
        a.append(cur.data)
        cur = cur.next
    index = len(a) // 2
    return a[index]


# middle_using_Floyds_cycle
def middle_using_Floyds_cycle(head):
    slow_pointer = head
    fast_pointer = head

    while fast_pointer:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return slow_pointer.data


# Reverse the linked_list
def reverse(head):
    prev = None
    cur = head
    while cur is not None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev  # return the new head


# Number of Nodes
def count(head):
    c = 0
    cur = head
    while cur:
        cur = cur.next
        c += 1
    return c


# To make the Last Node as the First Node
def last_first(head):
    second_last = None
    last = head

    while last.next:
        second_last = last
        last = last.next
    second_last.next = None
    last.next = head
    head = last
    return head


# To make the middle Node as the First Node
def middle_first(head):
    p = None
    p1 = head
    p2 = head.next.next
    while p2:
        p = p1
        p2 = p2.next.next
        p1 = p1.next
    p.next = p.next.next
    p1.next = head
    head = p1
    return head


# To add the one to the last Node
def add_1_to_lastNode(head):
    cur = head
    while cur.next:
        cur = cur.next
    cur.data = cur.data + 1
    return head


# To print the linked list
def print_linked_List(head):
    cur = head
    while cur:
        print(str(cur.data), "-->", end=" ")
        cur = cur.next
    print("None")


# Delete the alternate node
def delete_alternate_nodes(head):
    prev = head
    now = head.next
    while now and prev:
        prev.next = now.next
        now = None
        prev = prev.next
        if prev != None:
            now = prev.next
    return head


# Remove the Kth Node
def remove_kth_Node(head, k):
    cur = head
    count = 1
    while cur:
        count += 1
        if k == count:
            cur.next = cur.next.next
            count = 1
        cur = cur.next
    return head


# Remove Duplicates
def remove_Duplicate(head):
    prev = head
    now = head.next

    while now:
        if prev.data == now.data:
            prev.next = now.next
            now = now.next
        else:
            prev = prev.next
            now = now.next
    return head


# Add Number Linked Lists
# def number_linked_list(head):
#     cur = head
#     sum = 0
#     while cur:
#         sum = sum + cur.data
#         cur = cur.next
#     Total = sum * 2
#     while Total > 0:
#         mod = mod % 10
#         insert_at_beginning()
#     return sum


node4 = insert_at_beginning(40, None)
node3 = insert_at_beginning(25, node4)
node2 = insert_at_beginning(20, node3)
node1 = insert_at_beginning(10, node2)

insert_at_end(node1)
insert_at_given_pos(node1, 2)
print_linked_List(node1)

# Middle of the Node using Array
# print("Middle of the Node using Array", middle_linked_list_array(node1))
# print("Middle of the Node using Floyds cycle", middle_using_Floyds_cycle(node1))

# Numder of the Nodes
# print("The Count of the Nodes in the Linked List", count(node1))

# Deletion
# print_linked_List(delete_at_beginning(node1))
# print_linked_List(delete_at_end(node1))
# print_linked_List(delete_at_pos(node1, 2))

# Reverse
# print_linked_List(reverse(node1))

# To make the Last Node as the First Node
# print_linked_List(last_first(node1))

# To make the middle Node as the first Node
# print_linked_List(middle_first(node1))


# print_linked_List(delete_alternate_nodes(node1))

# print(number_linked_list(node1))

# print_linked_List(remove_Duplicate(node1))


print_linked_List(remove_kth_Node(node1, 2))
