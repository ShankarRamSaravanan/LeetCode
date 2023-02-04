def indexOfElement(num, target):

    left = 0
    right = len(num) - 1

    while left <= right:

        midpoint = left + right//2

        if num[midpoint] > target:
            right = midpoint - 1

        elif num[midpoint] < target:
            left = midpoint + 1

        else:
            return midpoint

    else:
        return -1


target = 78
num = [-1, 0, 3, 5, 9, 12]
print(indexOfElement(num, target))
