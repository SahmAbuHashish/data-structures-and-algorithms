def insertShiftArray(arr, val):
    mid = len(arr) // 2
    new_arr = [0] * (len(arr) + 1)
    
    for i in range(mid):
        new_arr[i] = arr[i]
    
    new_arr[mid] = val
    
    for i in range(mid+1, len(arr)+1):
        new_arr[i] = arr[i-1]
    
    return new_arr

arr = [1, 2, 3, 4, 5]
val = 10
new_arr = insertShiftArray(arr, val)
print(new_arr)
