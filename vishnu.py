
MAX_CHAR = 26


def factorial(n):

    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact


def countDistinctPermutations(st, length):

    freq = [0] * MAX_CHAR

    for i in range(0, length):
        if (st[i] >= 'a'):

            freq[(ord)(st[i]) - 97] = freq[(ord)(st[i]) - 97] + 1
        print(freq)
    fact = 1
    for i in range(0, MAX_CHAR):
        fact = fact * factorial(freq[i])

    return factorial(length) // fact


st = "pcpc"

length = 4


print(countDistinctPermutations(st, length))
