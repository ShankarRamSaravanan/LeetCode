def toString(List):

    return ''.join(List)


def permute(a, l, r):
    list1 = []
    if l == r:
        list1.append(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)

            # backtrack
            a[l], a[i] = a[i], a[l]
    return list1


string = "pcpc"
n = len(string)
a = list(string)
permute(a, 0, n-1)
