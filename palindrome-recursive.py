'''
def palindromeTest(string):
    if string[0] == string[-1] and palindromeTest(string[1:-1]):
        return "Its a palindrome"
    else:
        return "Not a palindrome"
'''
#doesn't actually work
#no clue why

def palindromeTest(string):
    string = str(string)
    string = string.lower()
    if len(string) == 1:
        return "Its a palindrome."
    elif len(string) == 2:
        if string[0] == string[1]:
            return "Its a palindrome."
        else:
            return "Its not a palindrome."    
    elif string[0] == string[-1]:
        return palindromeTest(string[1:-1])
    else:
        return "Its not a palindrome."
