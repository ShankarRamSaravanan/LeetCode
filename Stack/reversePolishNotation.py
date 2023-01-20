def reversePolishNotation(string):

    stack = []

    for i in string:

        if i == "+":

            stack.append(stack.pop() + stack.pop())

        elif i == '-':

            a, b = stack.pop(), stack.pop()

            stack.append(b-a)

        elif i == "*":
            stack.append(stack.pop() * stack.pop())

        elif i == "/":
            a, b = stack.pop(), stack.pop()

            stack.append(int(b/a))

        else:
            stack.append(int(i))

    return stack[0]


list = ["4", "13", "5", "/", "+"]
reversePolishNotation(list)
