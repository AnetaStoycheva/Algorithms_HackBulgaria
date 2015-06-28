def binary_search(sequence, number):
    left = 0
    right = len(sequence) - 1

    while left <= right:
        middle = left + (right-left)//2

        if sequence[middle] == number:
            return middle
        elif sequence[middle] < number:
            left = middle + 1
        else:
            right = middle - 1

    return -1


sequence1 = [-1, 0, 3, 3, 4, 6, 7, 89, 90, 560, 7890]
number1 = 5

print(binary_search(sequence1, number1))
