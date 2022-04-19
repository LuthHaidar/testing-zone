def palindromeTest(string): #test if string is a palindrome
def palindromeTest(string):
    if string[0] == string[-1] and palindromeTest(string[1:-1]):
        return "Its a palindrome"
    else:
        return "Not a palindrome"
