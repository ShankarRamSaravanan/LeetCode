def two_sum(a, target):

    hash_map = {}
    for i, n in enumerate(a):

        value = target - a[i]

        if value in hash_map:
            return (hash_map[value], i)

        hash_map[n] = i

        print(hash_map)


print(two_sum([2, 8, 11, 7], 9))
