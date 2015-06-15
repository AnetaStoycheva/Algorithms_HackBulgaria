def merge_sort(sequence):

    if len(sequence) > 1:
        sorted_sequence = []

        left_half = merge_sort(sequence[:len(sequence) // 2])
        right_half = merge_sort(sequence[len(sequence) // 2:])

        left_index = 0
        right_index = 0

        while len(sequence) != len(sorted_sequence):
            if len(left_half) > left_index and len(right_half) > right_index:
                if left_half[left_index] <= right_half[right_index]:
                    sorted_sequence.append(left_half[left_index])
                    left_index += 1
                else:
                    sorted_sequence.append(right_half[right_index])
                    right_index += 1
            elif len(left_half) == left_index:
                sorted_sequence.append(right_half[right_index])
                right_index += 1
            else:
                sorted_sequence.append(left_half[left_index])
                left_index += 1

        return sorted_sequence

    else:
        return sequence

a = [8, 10, 3, 7, 13, 2, 42, 6, 0]

print(merge_sort(a))
