class Quadruplets:

    # Returns the number of quadruplets that sum to zero.
    # a - [int]
    # b - [int]
    # c - [int]
    # d - [int]

    # sort lists with merge or quick sort

    def zero_quadruplets_count(a, b, c, d):
        left_sums = []
        right_sums = []
        result = 0

        for element1 in a:
            for element2 in b:
                left_sums.append(element1 + element2)

        for element1 in c:
            for element2 in d:
                right_sums.append(element1 + element2)

        left_sums.sort()
        right_sums.sort()

        last_found = len(right_sums) - 1
        previous_element = left_sums[0] - 1
        previous_result = 0

        for element in left_sums:
            if element == previous_element:
                result += previous_result
            else:
                previous_result = 0

            while last_found >= 0 and element + right_sums[last_found] >= 0:

                if element + right_sums[last_found] == 0:
                    result += 1
                    previous_result += 1

                last_found -= 1

            previous_element = element

        return result

a = [5, 3, 4]
b = [-2, -1, 6]
c = [-1, -2, 4]
d = [-1, -2, 7]

print(Quadruplets.zero_quadruplets_count(a, b, c, d))
