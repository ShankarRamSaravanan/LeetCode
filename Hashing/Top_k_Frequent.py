

# Using Sorted Bucket Concept


def Top_K_frequent(Elements, K):

    count = {}

    # [[],[],[],[],[]] if the array is 5 the array would be this.
    freq = [[] for i in range(len(Elements)+1)]

    for n in Elements:

        # We are couting the occurence of all the value in the given array in the form of dictionary
        count[n] = 1 + count.get(n, 0)

        # print(count)

        # output for above print statement
        # {1: 1}
        # {1: 2}
        # {1: 3}
        # {1: 3, 2: 1}
        # {1: 3, 2: 2}
        # {1: 3, 2: 3}
        # {1: 3, 2: 3, 3: 1}
        # {1: 3, 2: 3, 3: 1, 4: 1}
        # {1: 3, 2: 3, 3: 1, 4: 1, 5: 1}
        # {1: 3, 2: 3, 3: 2, 4: 1, 5: 1}
        # {1: 3, 2: 3, 3: 2, 4: 2, 5: 1}
        # {1: 3, 2: 3, 3: 3, 4: 2, 5: 1}
        # {1: 3, 2: 3, 3: 3, 4: 3, 5: 1}
        # {1: 3, 2: 3, 3: 4, 4: 3, 5: 1}
        # {1: 3, 2: 3, 3: 4, 4: 4, 5: 1}

    # print(count)    #output: {1: 3, 2: 3, 3: 4, 4: 4, 5: 1}

    # Here we are append all the values in the list,  that has occurence.
    for n, c in count.items():
        freq[c]. append(n)

    # print(freq)   #Output : [[], [5], [], [1, 2], [3, 4], [], [], [], [], [], [], [], [], [], [], []]

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == K:
                return res


K = 3
print(Top_K_frequent([1, 1, 1, 2, 2, 2, 3, 4, 5, 3, 4, 3, 4, 3, 4], K))
