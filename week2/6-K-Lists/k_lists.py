class Node:

    def __init__(self, value, next_node):
        self.__value = value
        self.__next = next_node

    def value(self):
        return self.__value

    def next(self):
        return self.__next

    def __lt__(self, other_node):
        return self.__value < other_node.__value


class Heap:
    @staticmethod
    def parent(j):
        return j // 2

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
            self.heap.pop()
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

    def size(self):
        return len(self.heap) - 1


class KLists:

    # Merge K sorted lists.
    # lists - [Node]
    def merge(lists):

        heap = Heap()
        result = []

        for l in lists:
            heap.add(l)

        while heap.size() > 0:
            current_node = heap.pop()
            result.append(current_node.value())

            if current_node.next() != None:
                heap.add(current_node.next())

        return result


o = Node(3, Node(5, Node(7, Node(9, None))))
p = Node(2, Node(4, Node(6, None)))
q = Node(0, Node(1, Node(8, Node(10, None))))

print(KLists.merge([o, p, q]))
