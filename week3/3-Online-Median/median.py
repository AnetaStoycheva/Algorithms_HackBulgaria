import heapq


# a wrapper class that takes a comparable type and reverses the < comparison
class ReverseLess:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


class Median:
    # inserts the number and returns the median

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def add_to_left_heap(self, value):
        heapq.heappush(self.left_heap, ReverseLess(value))

    def remove_from_left_heap(self):
        return heapq.heappop(self.left_heap).value

    def median(self):
        return self.left_heap[0].value

    def insert(self, number):
        if len(self.left_heap) == 0:
            self.add_to_left_heap(number)
        else:
            if self.median() >= number:
                self.add_to_left_heap(number)
                if len(self.left_heap) == len(self.right_heap) + 3:
                    a = self.remove_from_left_heap()
                    heapq.heappush(self.right_heap, a)
            else:
                heapq.heappush(self.right_heap, number)
                if len(self.left_heap) == len(self.right_heap):
                    a = heapq.heappop(self.right_heap)
                    self.add_to_left_heap(a)

        return self.median()


def main():
    N = int(input())
    numbers = [int(item) for item in input().split()]

    result = Median()

    for number in numbers:
        print(result.insert(number))


if __name__ == '__main__':
    main()
