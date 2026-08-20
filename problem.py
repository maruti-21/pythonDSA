def remove_leading_zeros(arr):
    i = 0
    while i < len(arr) and arr[i] == 0:
        i += 1
    return arr[i:]

nums = [0, 0, 0, 3, 0, 4, 5]
print(remove_leading_zeros(nums))