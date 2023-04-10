def BinarySearch(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

Binary_Search = BinarySearch([4, 8, 15, 16, 23, 42],15)
print(Binary_Search)

