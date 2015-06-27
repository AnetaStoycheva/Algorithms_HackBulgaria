class QuickSort:

    @staticmethod
    def quick_sort(sequence):
        if len(sequence) == 0:
            return sequence

        smaller = []
        bigger = []
        result = []

        for index in range(1, len(sequence)):
            if sequence[index] <= sequence[0]:
                smaller.append(sequence[index])
            else:
                bigger.append(sequence[index])

        smaller = QuickSort.quick_sort(smaller)
        bigger = QuickSort.quick_sort(bigger)

        result = smaller + [sequence[0]] + bigger
        return result

a = [4, 0, -9, 13, 13, 52, 7, 18, 3, 1, 6]

print(QuickSort.quick_sort(a))
