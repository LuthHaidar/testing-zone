#q1a
def dec2bin(number):
    number = int(number)
    binarynum = ''
    while number > 0:
        if number % 2 == 1:
            binarynum += '1'
        else:
            binarynum += '0'
    number = number // 2
    binarynum = binarynum[::-1]
    return binarynum

#q1b
def bin2dec(number):
    