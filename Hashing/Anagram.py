from collections import defaultdict


def Anagram(ana):

    List = defaultdict(list)

    for s in ana:

        count = [0] * 26

        for c in s:

            count[ord(c) - ord("a")] += 1

        print(count)

        List[tuple(count)].append(s)

        # typle(count) will become the  key for the dictionary Lit
        # append(s) will become the value for the key.

        # Since key is unique it will just append values of all the unique keys

        # print(List)

    # return List.values()


array = ["bat", "ate", "tan", "eat", "tea", "nat"]


print(Anagram(array))
