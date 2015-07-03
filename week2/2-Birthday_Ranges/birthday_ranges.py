class BirthdayRanges:

    # Return a vector with the number of people born in the specific ranges.
    # birthdays - [int]
    # ranges - [(int, int)]

    @staticmethod
    def birthdays_count(birthdays, ranges):
        dates = [0] * 366
        prefix_sum = [0]
        result = []

        for date in birthdays:
            dates[date] += 1

        for date_count in dates:
            prefix_sum.append(prefix_sum[-1] + date_count)

        for element in ranges:
            result.append(prefix_sum[element[-1] + 1] - prefix_sum[element[0]])

        return result


def main():
    p_r = input()
    people_and_ranges = p_r.split(' ')
    N = int(people_and_ranges[0])
    M = int(people_and_ranges[-1])

    birthdays = []
    ranges = []

    d = input()
    dates = d.split(' ')
    for date in dates:
        birthdays.append(int(date))

    while M != 0:
        r = input()
        a_range = r.split(' ')
        ranges.append((int(a_range[0]), int(a_range[-1])))

        M -= 1

    result = BirthdayRanges.birthdays_count(birthdays, ranges)

    for item in result:
        print(item)


if __name__ == '__main__':
    main()
