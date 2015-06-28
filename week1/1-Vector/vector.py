class Vector:

    def __init__(self, capacity):
        self.vector = [None] * capacity
        self.capacity = capacity
        self.size = 0

    # Returns the number of elements in the Vector.
    # Complexity: O(1)
    def size(self):
        return self.size

    # Returns the total capacity of the Vector.
    # Complexity: O(1)
    def capacity(self):
        return self.capacity

    # Adds value at a specific index in the Vector.
    # Complexity: O(n)
    def insert(self, index, value):
        if self.size >= self.capacity:
            self.vector = self.vector + self.capacity * [None]
            self.capacity *= 2

        for i in range(self.size, index, -1):
            self.vector[i] = self.vector[i - 1]

        self.vector[index] = value
        self.size += 1

    # Adds value to the end of the Vector.
    # Complexity: O(1)
    def add(self, value):
        if self.size >= self.capacity:
            self.vector = self.vector + self.capacity * [None]
            self.capacity *= 2

        self.vector[self.size] = value
        self.size += 1

    # Returns value at a specific index in the Vector
    # Complexity: O(1)
    def get(self, index):
        if index < self.size and index >= 0:
            return self.vector[index]
        else:
            raise IndexError('Index {} out of bounds.'.format(index))

    # Removes element at the specific index
    # Complexity: O(n)
    def remove(self, index):
        if index < self.size and index >= 0:
            for i in range(index, self.size - 1):
                self.vector[i] = self.vector[i + 1]
            self.vector[self.size - 1] = None
            self.size -= 1
        else:
            raise IndexError('Index {} out of bounds.'.format(index))

    # Removes element at the last index
    # Complexity: O(1)
    def pop(self):
        if self.size > 0:
            self.vector[self.size - 1] = None
            self.size -= 1
        else:
            raise IndexError('Pop from empty vector.')


def main():
    a = Vector(4)
    print(a.size())
    print(a.capacity())
    for i in range(1000001):
        a.add('a')

    a.insert(2, 10)
    # for index in range(a.size):
    #     print(a.get(index))
    # print(a.size())
    # print(a.capacity())
    a.pop()
    # for index in range(a.size):
    #     print(a.get(index))
    a.remove(1)
    # for index in range(a.size):
    #     print(a.get(index))
    print(a.size())
    print(a.capacity())


if __name__ == '__main__':
    main()
