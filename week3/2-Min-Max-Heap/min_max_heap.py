class MinMaxHeap:

    # Checks if a binary tree is a min/max heap.

    def is_valid(values, index, level, min_value, max_value):
        if index >= len(values):
            return True

        if not (values[index] > min_value and values[index] < max_value):
            return False

        if level % 2 != 0:
            min_value = values[index]
        else:
            max_value = values[index]

        return (MinMaxHeap.is_valid(values, 2 * index + 1, level + 1, min_value, max_value)
                and MinMaxHeap.is_valid(values, 2 * index + 2, level + 1, min_value, max_value))


def main():
    N = int(input())
    line = input()
    l = line.split()
    values = []

    for number in l:
        values.append(int(number))

    result = MinMaxHeap.is_valid(values, 0, 1, 0, 1e10)

    if result:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
