# https://geeksforgeeks.org/subtract-1-from-a-number-represented-as-linked-list/
# list = 1 -> 2 -> 3 -> 4
# output = 1 -> 2 -> 3 -> 3

class Node(object):
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        return self.head

    def print(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.next
        pass


def subtract_one_from_list_util(head):
    if head is None:
        return -1
    subtractor = subtract_one_from_list_util(head.next)
    print("Data - %f\t\tsubtractor - %f" % (head.data, subtractor))
    updated_subtractor = -1 if head.data == 0 else 0
    head.data = 9 if head.data == 0 else head.data + subtractor
    return updated_subtractor


def remove_starting_zeroes(head):
    while head is not None and head.data == 0:
        node = head
        head = head.next
        del node
    return head


def create_linked_list():
    input_elements = [0, 1]
    linked_list = LinkedList()
    for number in input_elements:
        linked_list.insert(number)
    subtract_one_from_list_util(linked_list.head)
    linked_list.head = remove_starting_zeroes(linked_list.head)
    linked_list.print()


create_linked_list()