# Array to Linked List
class Node:
    def __init__(self, head):
        self.data = head
        self.next = None


# a = [10, 15, 12, 13, 20, 14]
# a = [2, 2, 2, 2, 2]
# a = [1, 2, 3, 4, 5]
a = [1, 3, 4]
# a = [2, 4, 7, 8, 9]
# a = [9, 1, 9, 3, 9, 5, 7, 9, 2, 9]
# a = [23, 28, 28, 35, 49, 49, 53, 53]
# a = [1, 2, 1, 1, 2, 1]
# a = [590, 620, 80]
# a = [19, 28, 37, 46, 55]
# a = [1, 2, 4]
# a = [728, 279, 868, 363, 966, 212, 111, 329, 859]
# a = [25, 36, 47, 58, 69, 80]


def returnNodes():
    head = Node(a[0])
    cur = head
    for i in range(1, len(a)):
        cur.next = Node(a[i])
        cur = cur.next
    return head


head = returnNodes()


def printLinkedList(node):
    cur = node
    while cur:
        print(str(cur.data) + " -->", end=" ")
        cur = cur.next
    print("None")


printLinkedList(head)


# Remove every kth Node
def remove_kth_Node(head, k):
    cur = head
    count = 1
    while cur.next != None:
        count += 1
        if k == count:
            cur.next = cur.next.next
            count = 0
        else:
            cur = cur.next
    return head


# Remove Kth Node
# printLinkedList(remove_kth_Node(head, 3))


# pair_wise Swap
def pair_swap(head):
    prev = head
    while prev and prev.next:
        prev.data, prev.next.data = prev.next.data, prev.data
        prev = prev.next.next
    return head


# pair_wise Swap
# printLinkedList(pair_swap(head))


# Find the sum of last n nodes
def sum_last_N_Nodes(head, n):
    cur = head
    a = []
    while cur:
        a.append(cur.data)
        cur = cur.next
    sum = 0
    for i in range(n):
        sum = sum + a.pop()
    return sum


# Find the sum of last n nodes
# print(sum_last_N_Nodes(head, 3))


# Node at a given index in linked list
def node_at_given_index(head, k):
    cur = head
    count = 1
    data = -1
    while cur:
        if count == k:
            data = cur.data
            break
        else:
            cur = cur.next
        count += 1
    return data


# Node at a given index in linked list
# print(node_at_given_index(head, 3))


# Insert in Middle of Linked List
def insert_at_middle(head, x):
    low = head
    high = head

    while high and high.next and high.next.next:
        high = high.next.next
        low = low.next
    new_node = Node(x)
    temp = low.next
    low.next = new_node
    new_node.next = temp
    return head


# printLinkedList(insert_at_middle(head, 88))


# Modular Node
def modular_node(head, k):
    cur = head
    index = 1
    item = -1
    if cur == None:
        return -1
    while cur:
        if index % k == 0:
            item = cur.data
        index += 1
        cur = cur.next
    return item


# Modular Node
# print(modular_node(head, 13))


# Palindrome Linked List
def palindrome_linked_list(head):
    cur = head
    cur2 = head
    stack = []
    while cur:
        stack.append(cur.data)
        cur = cur.next
    while cur2:
        if a.pop() != cur2.data:
            return False
        cur2 = cur2.next
    return True


# palindrome_linked_list
# print(palindrome_linked_list(head))


# Swap nodes in a linked list without swapping data
def swap_node(head, x, y):
    i = head
    j = head.next
    prev = None
    while j and i:
        prev = i
        if i.data == x:
            j = j.next
            continue
        elif j.data == y:
            i = i.next
            continue
    temp = i
    i.next = j.next


# Remove Duplicates from a Sorted Linked List
def remove_duplicates_from_sorted_linkedList(head):
    cur = head
    while cur and cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head


# printLinkedList(remove_duplicates_from_sorted_linkedList(head))


# Rotate a Linked List
def rotate_linked_list(head, k):
    cur = head
    count = 1
    while cur:
        if count == k:
            head2 = cur.next
            cur.next = None
        else:
            count += 1
        cur = cur.next
    new_cur = head2
    while new_cur.next:
        new_cur = new_cur.next
    new_cur.next = head
    head = new_cur
    return head2


# printLinkedList(rotate_linked_list(head, 3))


# Remove duplicates from an unsorted linked list
def remove_duplicate_from_unsorted_linkedList(head):
    cur = head
    a = set()
    a.add(cur.data)
    while cur.next:
        if cur.next.data in a:
            cur.next = cur.next.next
        else:
            a.add(cur.next.data)
            cur = cur.next
    return head


# Remove duplicates from an unsorted linked list
# printLinkedList(remove_duplicate_from_unsorted_linkedList(head))


# Remove all occurences of duplicates in a linked list
def removeAll_duplicate_from_sorted_linkedList(head):
    cur = head
    a = set()
    a.add(cur.data)
    while cur.next:
        if cur.next.data in a:
            cur.next = cur.next.next
        else:
            a.add(cur.next.data)
            cur = cur.next
    return head


# Remove all occurences of duplicates in a linked list
# printLinkedList(removeAll_duplicate_from_sorted_linkedList(head))


# Insert in a Sorted List
def insert_in_sorted_list(head, k):
    cur = head
    new = Node(k)
    if k < head.data:
        new.next = head
        return new
    else:
        while cur.next and cur.next.data < k:
            cur = cur.next
        new.next = cur.next
        cur.next = new
        return head


# printLinkedList(insert_in_sorted_list(head, 70))


# Delete Middle of Linked List


def delete_middle_elem(head):
    # if head.next == None:
    #     return None

    # slow = head
    # fast = head.next.next.next
    # while fast.next:
    #     slow = slow.next
    #     fast = fast.next
    # slow.next = slow.next.next
    # return head
    prev = None
    slow = head
    fast = head
    while fast != None and fast.next != None:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head


# printLinkedList(delete_middle_elem(head))
# print(delete_middle_elem(head))


# Delete a Node in Single Linked List
def delete_Node(head, x):
    cur = head
    c = 1
    if c == x:
        return cur.next
    else:
        while cur:
            if c == x - 1:
                break
            c += 1
            cur = cur.next
        cur.next = cur.next.next
        return head


printLinkedList(delete_Node(head, 3))
