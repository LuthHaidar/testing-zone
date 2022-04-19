pascalDict = {}

def pascalRow(number):
    number += 1
    row = [1]  
    for i in range(1, number):
        row.append(row[i-1] * (number - i) // i)
    pascalDict[number] = row
    return row

def printPascal(number):
    number += 1
    for i in range(number):
        try:
            print(pascalDict[i+1])
        except:
            print(pascalRow(i))
    return None