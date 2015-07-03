class PhoneBook:

    # Find the names of people based on their phone numbers.
    # phone_book - [(String, int)]
    # numbers - [int]

    @staticmethod
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


def main():
    n_m = input()
    n_and_m = n_m.split(' ')
    N = int(n_and_m[0])
    M = int(n_and_m[-1])

    phone_book = []
    numbers = []

    while N != 0:
        contacts = input()
        ph = contacts.split(' ')
        phone_number = int(ph[0])
        name = ph[1]
        phone_book.append((name, phone_number))

        N -= 1

    while M != 0:
        a = int(input())
        numbers.append(a)

        M -= 1

    result = PhoneBook.lookup_names(phone_book, numbers)

    for item in result:
        print(item)


if __name__ == '__main__':
    main()
