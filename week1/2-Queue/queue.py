class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_at_beginning(self, value):
        if self.head == None:
            self.head = Node(value, None)
            self.tail = self.head
        else:
            self.head = Node(value, self.head)

    def add_at_the_end(self, value):
        if self.head == None:
            self.head = Node(value, None)
            self.tail = self.head
        else:
            new_node = Node(value, None)
            self.tail.next_node = new_node
            self.tail = new_node

    def remove_from_beginning(self):
        if self.head != None:
            element = self.head.value
            self.head = self.head.next_node
            if self.head == None:
                self.tail = None

            return element

        else:
            raise IndexError('Remove from empty list.')


class Queue:
    def __init__(self):
        self.values = LinkedList()
        self.size = 0

    # Adds value to the end of the Queue.
    # Complexity: O(1)
    def push(self, value):
        self.values.add_at_the_end(value)
        self.size += 1

    # Returns value from the front of the Queue and removes it.
    # Complexity: O(1)
    def pop(self):
        if self.size >= 1:
            self.size -= 1
        else:
            raise IndexError('Remove from empty list.')

        return self.values.remove_from_beginning()

    # Returns value from the front of the Queue without removing it.
    # Complexity: O(1)
    def peek(self):
        if self.size >= 1:
            return self.values.head.value
        else:
            return None

    # Returns the number of elements in the Queue.
    # Complexity: O(1)
    def size(self):
        return self.size


def main():
    a = Queue()

    print(a.size)  # 0
    print(a.peek())  # None

    try:
        print(a.pop())
    except Exception as e:
        print(e)
    a.push(3)

    print(a.size)  # 1

    for i in range(10):
        a.push(7)

    print(a.pop())
    print(a.peek())
    print(a.size)


if __name__ == '__main__':
    main()
