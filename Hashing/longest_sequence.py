def longest_sequence(array):

    Numset = set(array)

    longest = 0

    for i in array:

        if (i-1) not in Numset:
            length = 0

            while i+length in Numset:
                length += 1

            longest = max(length, longest)

    return longest


array = [1, 8, 100, 101, 102, 103, 104, 8, 1]
longest_sequence(array)
