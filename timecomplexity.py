def biggestnumber(arr):
    firstvalue = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > firstvalue:
            firstvalue = arr[i]

    return firstvalue


arr = [2,3,4,5,6,7,8,9]
print(biggestnumber(arr))


