
# Naive approach using division to find product
def productOfArrayExcept(elements):

    count = 1
    for i in elements:
        count *= i

    res = []
    for i in elements:
        res.append(int(count/i))

    return res


# print(productOfArrayExcept([4, 5, 6]))


# Approach Without Using division:


# get the prefix and the suffix of the array
def productOfArrayExceptD(elements):

    # calculate Prefix:
    print(elements)
    prefix = []

    count = 1
    for i in elements:
        count *= i
        prefix.append(count)

    postfix = []

    count = 1

    for i in elements[::-1]:
        count *= i
        postfix.append(count)
    postfix = postfix[::-1]

    mainOuput = []
    for i in range(len(elements)):

        output = prefix[i-1] * postfix[i+1]
        mainOuput.append(output)

    # return output


# print(productOfArrayExceptD([1, 2, 3, 4]))


def productOfArrayExceptRahul(Element):

    prefix = []
    prefix_element = 0
    count = 1
    for i in range(len(Element)):
        if prefix_element == 0:
            prefix_element += 1
        else:
            count *= Element[i-1]
        prefix.append(count)

    postfix = []
    postfix_element = 0
    count_new = 1
    Element_new = Element[::-1]
    for i in range(len(Element)):
        if postfix_element == 0:
            postfix_element += 1
        else:
            count_new *= Element_new[i-1]
        postfix.append(count_new)

    postfix = postfix[::-1]

    main_ouput = []
    for i in range(len(Element)):
        main_ouput.append(prefix[i] * postfix[i])
    return main_ouput


print(productOfArrayExceptRahul([1, 2, 3, 4]))
