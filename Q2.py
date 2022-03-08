def startup():
    global date
    print("This is my Date Validation Code.")
    print("You will later be asked to input a date. Format it as DDMMYYYY.")
    date = input('Enter a date in the format DDMMYYYY: ')

def valid():
    global date
    global day
    global month
    day = int(str(date)[0:2])
    month = int(str(date)[2:4])
    if month == 1 and day > 0 and day < 32:
        return print("Ok")
    elif month == 3 and day < 32:
        return print("Ok")
    elif month == 5 and day < 32:
        return print("Ok")
    elif month == 7 and day < 32:
        return print("Ok")
    elif month == 8 and day < 32:
        return print("Ok")
    elif month == 10 and day < 32:
        return print("Ok")
    elif month == 12 and day < 32:
        return print("Ok")
    elif month == 2 and int(str(date)[4:8]) % 4 == 0 and day > 1 and day < 30:
        return print("Ok")
    elif month == 2 and int(str(date)[4:8]) % 4 != 0 and day > 1 and day < 29:
        return print("Ok")
    elif month == 4 or 6 or 9 and day > 1 and day < 31:
        return print("Ok")
    else:
        return print("Invalid date")

def verify():
    global date
    try:
        int(date)
    except:
        print("Only digits")
        exit()
    if str(date) == '':
        print("Empty input")
        return exit()
    elif len(str(date)) != 8:
        print("Expected format DDMMYYYY")
        return exit()
    elif int(str(date)[2:4]) > 12:
        print("Month out of range")
        return exit()
startup()
verify()
valid()