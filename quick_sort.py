import random
testList = list(range(0,100))
random.shuffle(testList)

def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        less = [i for i in l[1:] if i <= pivot]
        greater = [i for i in l[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)