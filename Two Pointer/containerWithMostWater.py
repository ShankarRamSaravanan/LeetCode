#Naive, Brute force Approach which runs in o(n)


def container(array):

    res = 0

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            # width * height => area

            # j -> right
            # i -> left
            area = (j-i) * min(array[i], array[j])

            res = max(res, area)

    return res


array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#container(array)


#Linear Time Solution


def containerConstTime(array):

    res =0

    #Take two pointer both from different ends, only then we can achieve 0(n)

    l,r =0, len(array)-1

    while l<r:
        area = (r-l) * min(array[l], array[r])
        res = max(res, area)
        if array[l] < array[r]:
            l+=1
        elif array[r] < array[l]:
            r-=1
        else:
            r-=1
    return res      

containerConstTime(array)
