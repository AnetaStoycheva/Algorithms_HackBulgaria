NUMBERS = '0123456789'


def only_brackets(expression):
    result = ''

    for symbol in expression:
        if symbol not in NUMBERS:
            result = result + symbol

    return result


def is_valid(expression):
    if expression[0] in '{[(' and expression[-1] in ')]}':
        new_expression = only_brackets(expression)
    else:
        return False

    result = []
    after = {'{': '}[', '[': '](', '(': ') '}

    if new_expression[0] in '{[(':
        result += new_expression[0]
    else:
        return False

    for index in range(1, len(new_expression)):
        if len(result) == 0:
            return False

        if new_expression[index] == after[result[-1]][0]:
            result.pop()
        elif new_expression[index] == after[result[-1]][1]:
            result.append(new_expression[index])
        else:
            return False

    if len(result) == 0:
        return True
    else:
        return False


def round_br(round_br_expr):
    result = 0

    for index in range(1, len(round_br_expr) - 1):
        result = result * 10 + int(round_br_expr[index])

    return result


def square_br(square_br_expr):
    result = 0
    index = 1
    current_number = 0

    while index < len(square_br_expr) - 1:
        if square_br_expr[index] in NUMBERS:
            current_number = current_number * 10 + int(square_br_expr[index])

        if square_br_expr[index] == '(':
            current_expr = ''
            result += current_number
            current_number = 0

            for new_index in range(index, len(square_br_expr) - 1):
                current_expr += square_br_expr[new_index]

                if square_br_expr[new_index] == ')':
                    break

            index = new_index
            result += round_br(current_expr) * 2

        index += 1

    result += current_number

    return result


def curly_br(curly_br_expr):
    result = 0
    index = 1
    current_number = 0

    while index < len(curly_br_expr) - 1:
        if curly_br_expr[index] in NUMBERS:
            current_number = current_number * 10 + int(curly_br_expr[index])

        if curly_br_expr[index] == '[':
            current_expr = ''
            result += current_number
            current_number = 0

            for new_index in range(index, len(curly_br_expr) - 1):
                current_expr += curly_br_expr[new_index]

                if curly_br_expr[new_index] == ']':
                    break

            index = new_index
            result += square_br(current_expr) * 2

        index += 1

    result += current_number

    return result


def main():
    expression = input()

    if not is_valid(expression):
        print('NO')
        return

    if expression[0] == '{':
        print(curly_br(expression))
    elif expression[0] == '[':
        print(square_br(expression))
    else:
        print(round_br(expression))


if __name__ == '__main__':
    main()
