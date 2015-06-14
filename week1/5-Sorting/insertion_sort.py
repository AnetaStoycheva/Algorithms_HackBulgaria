def insertion_sort(sequence):

    for next_unsorted in range(len(sequence)):
        index = next_unsorted

        while index > 0 and sequence[index] < sequence[index - 1]:
            sequence[index - 1], sequence[index] = sequence[index], sequence[index - 1]
            index -= 1

    return sequence


a = [8, 10, 3, 7, 13, 2, 42, 6]

print(insertion_sort(a))
