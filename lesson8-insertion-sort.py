testlist1 = ['at', 'least','it','is','not','recursion']
testlist2 = [101, 110, 106, 111, 121, 32, 105, 116, 32, 119, 104, 105, 108, 101, 32, 105, 116, 32, 108, 97, 115, 116, 115]

def insertion_sort(list, order = 'ascending'):
    if order == 'ascending':
        if type(list[0]) == int:
            for i in range(1, len(list)):
                j = i
                while j > 0 and list[j] < list[j-1]:
                    list[j], list[j-1] = list[j-1], list[j]
                    j -= 1

        elif type(list[0]) == str:
            for i in range(1, len(list)):
                j = i
                while j > 0 and (list[j][0] < list[j-1][0] or (list[j][0] == list[j-1][0] and list[j][1] < list[j-1][1])):
                    list[j], list[j-1] = list[j-1], list[j]
                    j -= 1

    elif order == 'descending':
        if type(list[0]) == int:
            for i in range(1, len(list)):
                j = i
                while j > 0 and list[j] > list[j-1]:
                    list[j], list[j-1] = list[j-1], list[j]
                    j -= 1
        
        elif type(list[0]) == str:
            for i in range(1, len(list)):
                j = i
                while j > 0 and (list[j][0] > list[j-1][0] or (list[j][0] == list[j-1][0] and list[j][1] > list[j-1][1])):
                    list[j], list[j-1] = list[j-1], list[j]
                    j -= 1
    
    return list

print(insertion_sort(testlist1, "descending"))