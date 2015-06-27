class CountSort:

    MAX_VALUE = 1000

    @staticmethod
    def count_sort(sequence):
        result = []
        a = CountSort.MAX_VALUE * [0]

        for number in sequence:
            a[number] += 1

        for index in range(len(a)):
            result += ([index] * a[index])

        return result

a = [4, 0, 0, 1, 1, 1, 1, 1, 13, 13, 52, 7, 18, 3, 1, 6, 90, 800, 999, 900]

print(CountSort.count_sort(a))
