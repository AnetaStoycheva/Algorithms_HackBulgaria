class Roots:

    # Finds the square root of a number using binary search.
    # number - int
    def square_root(number):
        left = 0
        right = number

        for a in range(100):
            middle = left + ((right - left) / 2)
            if middle ** 2 > number:
                right = middle
            else:
                left = middle

        return middle


result1 = Roots.square_root(15)
result2 = Roots.square_root(2)
result3 = Roots.square_root(4)
result4 = Roots.square_root(5)

print('%.5f' % result1)
print('%.5f' % result2)
print('%.5f' % result3)
print('%.5f' % result4)
print(result4)
