class Vector:
    def __init__(self, capacity):
        self.vector = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def vector_size(self):
        return self.size

    def vector_capacity(self):
        return self.capacity

    def insert_at_specific_index(self, index, value):
        if self.size >= self.capacity:
            self.vector = self.vector + self.capacity * [None]
            self.capacity *= 2

        for i in range(self.size, index, -1):
            self.vector[i] = self.vector[i - 1]

        self.vector[index] = value
        self.size += 1

    def add_at_the_end(self, value):
        if self.size >= self.capacity:
            self.vector = self.vector + self.capacity * [None]
            self.capacity *= 2

        self.vector[self.size] = value
        self.size += 1

    def return_value_specific_index(self, index):
        if index < self.size and index >= 0:
            return self.vector[index]
        else:
            raise IndexError('Index {} out of bounds.'.format(index))

    def remove_from_specific_index(self, index):
        if index < self.size and index >= 0:
            for i in range(index, self.size - 1):
                self.vector[i] = self.vector[i + 1]
            self.vector[self.size - 1] = None
            self.size -= 1
        else:
            raise IndexError('Index {} out of bounds.'.format(index))

    def remove_at_last_index(self):
        if self.size > 0:
            self.vector[self.size - 1] = None
            self.size -= 1
        else:
            raise IndexError('Pop from empty vector.')


def main():
    a = Vector(4)
    print(a.vector_size())
    print(a.vector_capacity())
    for i in range(1000001):
        a.add_at_the_end('a')

    a.insert_at_specific_index(2, 10)
    # for index in range(a.size):
    #     print(a.return_value_specific_index(index))
    # print(a.vector_size())
    # print(a.vector_capacity())
    a.remove_at_last_index()
    # for index in range(a.size):
    #     print(a.return_value_specific_index(index))
    a.remove_from_specific_index(1)
    # for index in range(a.size):
    #     print(a.return_value_specific_index(index))
    print(a.vector_size())
    print(a.vector_capacity())


if __name__ == '__main__':
    main()
