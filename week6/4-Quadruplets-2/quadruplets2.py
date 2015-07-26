class Quadruplets2:

    # Returns the number of quadruplets that sum to zero.
    # a - [int]
    # b - [int]
    # c - [int]
    # d - [int]

    @staticmethod
    def zero_quadruplets_count(a, b, c, d):
        left_sums = {}
        right_sums = {}
        result = 0

        for element1 in a:
            for element2 in b:
                if element1 + element2 not in left_sums:
                    left_sums[element1 + element2] = 1
                else:
                    left_sums[element1 + element2] += 1

        for element1 in c:
            for element2 in d:
                if element1 + element2 not in right_sums:
                    right_sums[element1 + element2] = 1
                else:
                    right_sums[element1 + element2] += 1

        for key in left_sums:
            if -key in right_sums:
                result = result + (left_sums[key] * right_sums[-key])

        return result


def main():
    N = int(input())

    res = [[], [], [], []]

    for a in range(len(res)):
        line = input()
        elements = line.split(' ')

        for element in elements:
            res[a].append(int(element))

    print(Quadruplets2.zero_quadruplets_count(res[0], res[1], res[2], res[3]))
    # print(Quadruplets2.zero_quadruplets_count([5, 3, 4], [-2, -1, 6], [-1, -2, 4], [-1, -2, 7]))


if __name__ == '__main__':
    main()
