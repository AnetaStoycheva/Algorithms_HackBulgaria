def palindrome(string):
    string = str(string)

    return string == string[::-1]


def rotation(string):
    string = str(string)
    result = []

    for index in range(len(string)):
        new_string = string[index:] + string[:index]
        if palindrome(new_string):
            result.append(new_string)

    return result


def main():
    string = input()
    result = rotation(string)
    if len(result) != 0:
        for element in result:
            print(element)
    else:
        print("NONE")


if __name__ == '__main__':
    main()
