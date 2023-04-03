arr = [1, 2, 3, 4, 5]

def reverseArray(arr):
    reversed_arr = [None] * len(arr)
    
    for i in range(len(arr)-1, -1, -1):
        reversed_arr[len(arr)-1-i] = arr[i]
    
    return reversed_arr

reversed_arr = reverseArray(arr)
print(reversed_arr)  