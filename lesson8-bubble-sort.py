numlist = [42, 34, 23, 55, 77, 83, 31, 98, 12]
namelist = ['bob','amy','jonathan','susan','karen','robert']

def bubble_sort(list, order = 'ascending'):
    cycles = 0
    if order.lower() == 'descending':
        if type(list[0]) == int:
            for i in range(len(list)-1):
                swap = False
                for j in range(len(list)-1-i):
                    if list[j] < list[j+1]:
                        list[j], list[j+1] = list[j+1], list[j]
                        swap = True
                if swap == False:
                    break
                cycles += 1
        
        elif type(list[0]) == str:
            for i in range(len(list)-1):
                swap = False
                for j in range(len(list)-1-i):
                    if len(list[j]) < len(list[j+1]):
                        list[j], list[j+1] = list[j+1], list[j]
                        swap = True
                if swap == False:
                    break
                cycles += 1
    
    elif order.lower() == 'ascending':
        if type(list[0]) == int:
            for i in range(len(list)-1):
                swap = False
                for j in range(len(list)-1-i):
                    if list[j] > list[j+1]:
                        list[j], list[j+1] = list[j+1], list[j]
                        swap = True
                if swap == False:
                    break
                cycles += 1
        
        elif type(list[0]) == str:
            for i in range(len(list)-1):
                swap = False
                for j in range(len(list)-1-i):
                    cycles += 1
                    if len(list[j]) > len(list[j+1]):
                        list[j], list[j+1] = list[j+1], list[j]
                        swap = True
                if swap == False:
                    break
                cycles += 1
    
    return list

print(bubble_sort(numlist, 'ascending'))
print(bubble_sort(numlist, 'descending'))
print(bubble_sort(namelist, 'ascending'))
print(bubble_sort(namelist, 'descending'))