class Heap:
    @staticmethod
    def parent(j):
        return j // 2  # round down

    @staticmethod
    def left(j):
        return 2 * j

    @staticmethod
    def right(j):
        return 2 * j + 1

    def __init__(self):
        self.heap = [0]

    def add(self, value):
        self.heap.append(value)

        index = len(self.heap) - 1

        while index != 1 and self.heap[index] < self.heap[Heap.parent(index)]:
            temp = self.heap[index]
            self.heap[index] = self.heap[Heap.parent(index)]
            self.heap[Heap.parent(index)] = temp
            index = Heap.parent(index)

    def pop(self):
        min_element = self.heap[1]
        if len(self.heap) == 2:
            return min_element
        self.heap[1] = self.heap.pop()

        index = 1

        while (Heap.right(index) < len(self.heap) and
                (self.heap[Heap.left(index)] < self.heap[index] or
                    self.heap[Heap.right(index)] < self.heap[index])):

            if self.heap[Heap.left(index)] <= self.heap[Heap.right(index)]:
                next_index = Heap.left(index)
            else:
                next_index = Heap.right(index)

            temp = self.heap[index]
            self.heap[index] = self.heap[next_index]
            self.heap[next_index] = temp

            index = next_index

        if (Heap.left(index) < len(self.heap) and
                self.heap[index] > self.heap[Heap.left(index)]):

            temp = self.heap[index]
            self.heap[index] = self.heap[Heap.left(index)]
            self.heap[Heap.left(index)] = temp

        return min_element


class HeapSort:

    # Sorts a sequence of integers.

    def sort(sequence):
        new_heap = Heap()
        result = []

        for element in sequence:
            new_heap.add(element)

        for element in sequence:
            result.append(new_heap.pop())

        return result

a = [4, 13, 52, 7, 18, 2, 3, 1, 6, -9, 0, 3, 3]

print(HeapSort.sort(a))
