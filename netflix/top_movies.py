# Fetch top movies from N countries and convert them into single list in ascending order.
# Merge K sorted lists


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        head = self.head
        if head is None:
            self.head = node
            return
        while head.next is not None:
            head = head.next
        head.next = node

    def print(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.next


def merge_sorted_lists(head1, head2):
    prev = head1
    temp_head1 = head1
    while temp_head1 is not None and head2 is not None:
        if temp_head1.data < head2.data:
            prev = temp_head1
            temp_head1 = temp_head1.next
        else:
            node = head2
            head2 = node.next
            node.next = temp_head1
            prev.next = node
            prev = node
    if temp_head1 is None:
        while head2 is not None:
            node = head2
            head2 = node.next
            node.next = temp_head1
            prev.next = node
            prev = node
    return head1


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
input_list_1 = [11, 23, 32, 38]
input_list_2 = [24, 57, 99]

for number in input_list_1:
    linked_list_1.insert_at_end(number)

for number in input_list_2:
    linked_list_2.insert_at_end(number)

linked_list_1.head = merge_sorted_lists(linked_list_1.head, linked_list_2.head)
linked_list_1.print()
