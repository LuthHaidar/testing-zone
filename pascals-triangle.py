pascalDict = {}

def pascalRow(number):
    number += 1
    row = [1]  
    for i in range(1, number):
        row.append(row[i-1] * (number - i) // i)
    pascalDict[number] = row
    return row

def pascalFormat(number, row):
    number = len(str(pascalRow(number)))
    row = " " * ((number - len(str(row)))// 2)  + str(row)
    return row

def printPascal(number):
    try:
        for i in range(0, number+1):
            print(pascalFormat(number, pascalDict[i]))
    except KeyError:
        for i in range(0, number+1):
            print(pascalFormat(number, pascalRow(i)))