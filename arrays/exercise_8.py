# Create min-heap from array elements
# input = [3, 1, 6, 5, 2, 4]


class MinHeap:
    def __init__(self, n):
        self.input_list = [None] * n

    def heapify_up(self, index):
        if index <= 0:
            return
        parent = (index - 1) // 2
        if self.input_list[index] >= self.input_list[parent]:
            return
        else:
            temp = self.input_list[index]
            self.input_list[index] = self.input_list[parent]
            self.input_list[parent] = temp
            self.heapify_up(parent)

    def insert_at_bottom(self, data, index):
        if self.input_list[0] is None:
            self.input_list[0] = data
            return
        parent = (index - 1) // 2  # integer division
        left = 2 * parent + 1
        right = 2 * parent + 2
        if self.input_list[left] is None:
            self.input_list[left] = data
        else:
            self.input_list[right] = data
        self.heapify_up(index)


input_list = [3, 1, 6, 5, 2, 4]
total = len(input_list)
min_heap = MinHeap(total)
for (i, number) in enumerate(input_list):
    min_heap.insert_at_bottom(number, i)
print(min_heap.input_list)
