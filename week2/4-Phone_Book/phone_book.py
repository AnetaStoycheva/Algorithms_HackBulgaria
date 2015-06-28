class PhoneBook:

    # Find the names of people based on their phone numbers.
    # phone_book - [(String, int)]
    # numbers - [int]
    def lookup_names(phone_book, numbers):
        phone_book.sort(key=lambda element: element[-1])

        result = []
        for number in numbers:
            left = 0
            right = len(phone_book) - 1

            while left <= right:
                middle = left + (right - left) // 2

                if phone_book[middle][-1] == number:
                    result.append(phone_book[middle][0])
                    break
                elif phone_book[middle][-1] < number:
                    left = middle + 1
                else:
                    right = middle - 1

            if phone_book[middle][-1] != number:
                result.append(None)

        return result

a = [('a', 0), ('a', 2), ('Stani', 1), ('Rado', 5), ('Ivan', 6), ('Ivan', 8)]
b = [2, 15, 8]

print(PhoneBook.lookup_names(a, b))
