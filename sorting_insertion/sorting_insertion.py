def sorting_insertion(array):
    """
    Sorts an array in ascending order using the insertion sort algorithm.
    """
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1
        while j >= 0 and value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value
    return array