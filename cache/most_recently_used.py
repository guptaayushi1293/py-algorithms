# Fetch Most Recently Watched Titles in Netflix.
# Keeping most recently used items at the head and least recently at the tail. (It can be other way around as well)

node_lookup = {}


def check_data_id(data):
    return node_lookup.get(data, None)


def update_node_lookup(data, node):
    node_lookup[data] = node


def remove_node_lookup(data):
    if data in node_lookup: del node_lookup[data]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    @staticmethod
    def delete(node):
        node.next = None
        node.prev = None
        del node


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, data):
        if not self.head:
            return None
        start = self.head
        while start:
            if start.data == data:
                return start
            start = start.next
        return None

    def insert_at_head(self, data):
        is_present = check_data_id(data)
        if not is_present:
            node = Node(data)
            node.next = self.head
            if self.head:
                self.head.prev = node
            self.head = node
            if not self.tail:
                self.tail = node
            update_node_lookup(data, node)

    def delete_at_tail(self):
        if not self.tail:
            return False
        curr_node = self.tail
        prev_node = curr_node.prev
        if prev_node:
            prev_node.next = curr_node.next
        if self.head == self.tail:
            self.head = self.tail = None
        self.tail = prev_node
        remove_node_lookup(curr_node.data)
        Node.delete(curr_node)
        return True

    def delete(self, data):
        present = self.search(data)
        if not present:
            return False
        prev_node = present.prev
        next_node = present.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        if self.head == present:
            self.head = next_node
        Node.delete(present)
        return True

    def print(self):
        start = self.head
        while start:
            print(start.data)
            start = start.next


arr = [1, 2, 3, 4, 5]
linked_list = DoubleLinkedList()
for number in arr:
    linked_list.insert_at_head(number)
linked_list.print()
linked_list.delete_at_tail()
print("--------------")
linked_list.print()
