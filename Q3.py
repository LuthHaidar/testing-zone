original = input ("Input a word: ")
def rule():
    global original
    global new
    if original[0] == 'a' or 'e' or 'i' or 'o' or 'u':
        new = original + '-way'
    for i in original:
        count = 0
        if original[i] != 'a' or 'e' or 'i' or 'o' or 'u':
            count += 1
        if len(original) == count:
            new = original + '-way'
    if new[0] != 'a' or 'e' or 'i' or 'o' or 'u':
        for i in new:
            if new[i] != 'a' or 'e' or 'i' or 'o' or 'u':
                new = new[i-1:]
    