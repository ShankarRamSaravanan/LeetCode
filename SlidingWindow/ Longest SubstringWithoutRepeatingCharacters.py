def longestSubstring(s):

    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1

        charSet.add(s[r])

        # print(s[r], s[l])
        res = max(res, r-l+1)

    return res


a = longestSubstring("abcabcbb")
print("longest substring length is ", a)
