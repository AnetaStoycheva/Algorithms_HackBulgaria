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

        while index != 1 and self.heap[index] > self.heap[Heap.parent(index)]:
            temp = self.heap[index]
            self.heap[index] = self.heap[Heap.parent(index)]
            self.heap[Heap.parent(index)] = temp
            index = Heap.parent(index)

    def pop(self):
        max_element = self.heap[1]
        if len(self.heap) == 2:
            self.heap.pop()
            return max_element
        self.heap[1] = self.heap.pop()

        index = 1

        while (Heap.right(index) < len(self.heap) and
                (self.heap[Heap.left(index)] > self.heap[index] or
                    self.heap[Heap.right(index)] > self.heap[index])):

            if self.heap[Heap.left(index)] > self.heap[Heap.right(index)]:
                next_index = Heap.left(index)
            else:
                next_index = Heap.right(index)

            temp = self.heap[index]
            self.heap[index] = self.heap[next_index]
            self.heap[next_index] = temp

            index = next_index

        if (Heap.left(index) < len(self.heap) and
                self.heap[index] < self.heap[Heap.left(index)]):

            temp = self.heap[index]
            self.heap[index] = self.heap[Heap.left(index)]
            self.heap[Heap.left(index)] = temp

        return max_element

    def size(self):
        return len(self.heap) - 1


class KMin:

    # Finds the k-th minimum element in an unsorted collection.
    # numbers - [int]
    # k - int
    def kthMinimum(numbers, k):
        heap = Heap()

        for i in range(k):
            heap.add(numbers[i])

        for i in range(k, len(numbers)):
            heap.add(numbers[i])
            heap.pop()

        return heap.pop()


# da se opravi vhoda s pop()
def main():
    first = input()
    f = first.split()
    N = int(f[0])
    k = int(f[-1])
    vector = input()
    v = vector.split()

    numbers = []

    for number in v:
        numbers.append(int(number))

    print(KMin.kthMinimum(numbers, k))


if __name__ == '__main__':
    main()
