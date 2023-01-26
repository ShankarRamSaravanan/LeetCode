def calc(N, C, A):
    arr = A

    arr.sort()

    res = 0

    for ele in arr:

        if ele > C:
            res += 1

    return res


print(calc(3, 2, [6, 2, 9]))
