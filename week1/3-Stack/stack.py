import sys
sys.path.insert(0, '../2-Queue')


from queue import Queue


class Stack:
    def __init__(self):
        self.values = Queue()

    # Adds value to the end of the Stack.
    # Complexity: O(1)
    def push(self, value):
        self.values.push(value)

    # Returns value from the end of the Stack and removes it.
    # Complexity: O(1)
    def pop(self):
        q = Queue()
        while self.values.size > 1:
            q.push(self.values.pop())
        last_element = self.values.pop()

        while q.size > 0:
            self.values.push(q.pop())

        return last_element

    # Returns value from the end of the Stack without removing it.
    # Complexity: O(1)
    def peek(self):
        if self.values.size >= 1:
            last_element = self.pop()
            self.push(last_element)
            return last_element

        else:
            return None

    # Returns the number of elements in the Stack.
    # Complexity: O(1)
    def size(self):
        return self.values.size


def main():
    a = Stack()

    print(a.size())  # 0
    print(a.peek())  # None

    try:
        print(a.pop())
    except Exception as e:
        print(e)
    a.push(3)

    print(a.size())  # 1

    for i in range(10):
        a.push(i)

    print(a.pop())  # 9
    print(a.peek())  # 8
    print(a.size())  # 10


if __name__ == '__main__':
    main()
