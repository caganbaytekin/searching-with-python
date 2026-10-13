def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1


array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
targ = 15

result = binarySearch(array, targ)

if result != -1:
    print(f"Value {targ} found at index {result}.")
else:
    print(f"Value {targ} not found.")
