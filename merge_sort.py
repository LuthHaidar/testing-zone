import random
l = list(range(0,100))
random.shuffle(l)
def merge_sort(lis):
    if len(lis) > 1:
        mid = len(lis)//2
        left = lis[:mid]
        right = lis[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lis[k] = left[i]
                i += 1
            else:
                lis[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lis[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lis[k] = right[j]
            j += 1
            k += 1
    return lis[::-1]