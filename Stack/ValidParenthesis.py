def validParenthesis(string):
    stack = []
    hashMap = {')': '(', ']': '[', '}': '{'}
    for i in string:
        if i in hashMap:
            if stack and (stack[-1] == hashMap[i]):
                stack.pop()
            else:
                return False
        else:
            stack.append(i)

    return True if not stack else False


string1 = "{}}"
print(validParenthesis(string1))
