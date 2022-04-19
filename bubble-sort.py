def bubble_sort(array):
    for x in range(len(array)):
        for y in range(len(array)-1-x):
            if array[y] > array[y+1]:
                array[y], array[y+1] = array[y+1], array[y]
    return array