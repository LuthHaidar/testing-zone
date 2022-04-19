def insertion_sort(array):
    for x in range(1, len(array)):
        y = x
        while y > 0 and array[y] < array[y-1]:
            array[y], array[y-1] = array[y-1], array[y]
            y -= 1
    return array    