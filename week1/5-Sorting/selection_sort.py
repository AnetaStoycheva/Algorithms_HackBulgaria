def min_element_index(sequence, used_indexes):

    min_element_value = max(sequence) + 1
    min_element_index = -1

    for index in range(len(sequence)):
        if sequence[index] <= min_element_value and not used_indexes[index]:
            min_element_value = sequence[index]
            min_element_index = index

    used_indexes[min_element_index] = True

    return min_element_value


def selection_sort(sequence):

    sorted_sequence = []
    used_indexes = [False] * len(sequence)

    while len(sorted_sequence) != len(sequence):

        min_el = min_element_index(sequence, used_indexes)
        sorted_sequence.append(min_el)

    return sorted_sequence


a = [8, 10, 3, 7, 13, 2, 42, 6]

print(selection_sort(a))
