def my_threeSum(nums):
    list = []
    for i in nums:
        for j in range(1, len(nums)):
            for k in range(2, len(nums)):

                if i != nums[j] and i != nums[k] and nums[j] != nums[k]:
                    if i+nums[j]+nums[k] == 0:
                        list.append([i, nums[j], nums[k]])

    # return list


# my_threeSum([-1, 0, 1, 2, -1, -4])


def threeSum(array):
    list = []  # Since we need to return thr triplet in the form an array we are initiating the empty list

    # Step1: Sort the array:
    sortedArray = array
    sortedArray.sort()

# Step 2: Loop through the array by considering both its value and index and keep first value as kind of constant.

    for i, j in enumerate(sortedArray):
        # check if the index is greater than 0 and the sortedarray value of the cuurent index is equal to the value of the next index.

        # This checks whether any of the values in consective values are equal in the array.
        if i > 0 and j == sortedArray[i-1]:
            continue  # this would skip the similiar value

        # Initialise Left anf Right Pointer

        l = i+1
        r = len(array) - 1

        while l < r:  # In all the cases left should be lesser than r in wise of index

            # j is the first value of the index
            threesum = j + sortedArray[l] + sortedArray[r]

        # if sum >0 obviously we need to reduce the right pointer
            if threesum > 0:
                r -= 1

        # if sum <0 increment left pointer
            elif threesum < 0:
                l += 1

        # if the sum is 0 append the combination to the list
            else:
                list.append([j, sortedArray[l], sortedArray[r]])

                # now increment the left pointer again
                l += 1
                while sortedArray[l] == sortedArray[l - 1] and l < r:
                    l += 1

    return list


threeSum([-1, 0, 1, 2, -1, -4])
