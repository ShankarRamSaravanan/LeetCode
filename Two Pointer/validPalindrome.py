# Method1


def validPalindrome(string):

    palin = ""

    for i in string:
        if i.isalnum():
            palin += i.lower()

    if palin == palin[::-1]:
        return True
    else:
        return False


string = "A man, a plan, a canal: Panama"

# Function call


# validPalindrome(string)


# Since the above program consumes more memory, we are considering the second Problem


# Method 2


def validPalindrome_2(string):

    stringLength = len(string)

    print(stringLength)

    # for i, j in zip(range(stringLength), range(stringLength-1, 0, -1)):


string = "A man, a plan, a canal: Panama"
validPalindrome_2(string)
