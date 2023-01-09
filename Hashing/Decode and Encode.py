def encode(strs):

    res = ""

    for i in strs:
        res += str(len(i)) + "#" + i
    return res


array = ["Hello", "World", "shankar", "ram"]



#Decode is the tricky part 

def decode(a=encode(array)):

    res, i = [], 0      # Taking a list and a pointer
    while i < len(a):      # i is 0 intiallly where the length of string would be combination of a number with # which is actually a encoded value
                           # This will loop through until we the len(str) become equal to zero
        j = i              # Passing the value of i to j for considering the the hash ("#")

        while a[j] != "#":    #This is would loop though for once since the j holds the value of i and we are incrementing
            j += 1

        length = int(a[i:j])       #here we are taking the interger value which is actaully the length of individual string from i:j of the encoded string 
        res.append(a[j+1:j+1+length])    # Appending the value to the res where j, it becomes j+1 +1 now from there we take till j+1+length

        i = j+1+length              #Here we are setting the value of i from j+1+length
        print(res)

    return res


print(decode())
