def half(message):
    new_message = ''
    len_message = len(message)
    len_half_message = len_message // 2

    if len_message % 2 == 0:
        new_message = message[len_half_message:] + message[: len_half_message]
    else:
        new_message = message[(len_half_message + 1):] + message[: (len_half_message + 1)]

    return new_message


def decrypt(message):
    new_message = half(message)
    first_tilda = new_message.index('~')
    last_tilda = new_message.rfind('~')

    length_key = int(new_message[(last_tilda + 1):])
    key = new_message[(last_tilda - length_key):last_tilda]

    length_alphabet = int(new_message[:first_tilda])
    alphabet = new_message[first_tilda + 1: (first_tilda + 1) + length_alphabet]

    encrypted_message = new_message[(first_tilda + 1) + length_alphabet: (last_tilda - length_key)]

    encrypted_positions = to_positions(encrypted_message, alphabet)

    len_enc_positon = len(encrypted_positions)
    how_many = int((len(encrypted_message) // length_key) + 1)

    key_repeated = (key * how_many)[:len(encrypted_message)]

    key_positions = to_positions(key_repeated, alphabet)

    result = []
    for index in range(len(key_positions)):
        result.append(encrypted_positions[index] - key_positions[index])
        if result[-1] < 0:
            result[-1] += len(alphabet)

    return to_letters(result, alphabet)


def to_positions(message, alphabet):
    positions = []

    for symbol in message:
        positions.append(alphabet.index(symbol))

    return positions


def to_letters(message, alphabet):
    result = ''

    for symbol in message:
        result += alphabet[symbol]

    return result


def main():
    message = input()
    print(decrypt(message))


if __name__ == '__main__':
    main()
