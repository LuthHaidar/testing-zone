def main(): #the main function where displaying, editing board, and defining the winner takes place
    win = 0 # variable declarations
    turn = 0
    row = 0
    col = 0
    line1 = "   0 1 2\n"
    line2 = ['0: ' ,'  ', '  ', '  ']
    line3 = ['1: ' ,'  ', '  ', '  ']
    line4 = ['2: ' ,'  ', '  ', '  ']
    while win == 0:
        if turn % 2 == 0: #determining turn
            piece = 'X '
            print("Ready Player One")
        else:
            piece = 'O '
            print("Ready Other Guy")
        print(line1 + line2[0] + line2[1] + line2[2] + line2[3] + "\n" + line3[0] + line3[1] + line3[2] + line3[3]+ "\n" + line4[0] + line4[1] + line4[2] + line4[3])
        row = input('Row? ')
        row = int(row)
        col = input('Column? ')
        col = int(col)
        if row <= 2 and row >= 0 and col <= 2 and col >=0:
            if row == 0:
                if line2[col + 1] == '  ':
                    line2[col + 1] = piece
                    turn= turn + 1
                else:
                    print("This slot has been taken!!! Please choose another.")
            elif row == 1:
                if line3[col + 1] == '  ':
                    line3[col + 1] = piece
                    turn = turn + 1
                else:
                    print("This slot has been taken!!! Please choose another.")
            elif row == 2:
                if line4[col + 1] == '  ':
                    line4[col + 1] = piece
                    turn = turn + 1
                else:
                    print("This slot has been taken!!! Please choose another.")
        else:
            print('Please choose a better slot to place your piece into.')
        if line2 == ['0: ' ,'X ', 'X ', 'X '] or line2 == ['0: ' ,'O ', 'O ', 'O '] or line3 == ['0: ' ,'X ', 'X ', 'X '] or line3 == ['0: ' ,'O ', 'O ', 'O '] or line4 == ['0: ' ,'X ', 'X ', 'X '] or line4 == ['0: ' ,'O ', 'O ', 'O ']:
            win = 1
        elif line2[2] == 'O' and line3[2] == 'O' and line4[2] == 'O':
            win = 1
        elif line2[3] == 'O' and line3[3] == 'O' and line4[3] == 'O':
            win = 1
        elif line2[1] == 'O' and line3[1] == 'O' and line4[1] == 'O':
        win = 1
    elif line2[3] == 'O' and line3[2] == 'O' and line4[1] == 'O':
        win = 1
    elif line2[1] == 'O' and line3[2] == 'O' and line4[3] == 'O':
        win = 1
        
    elif line2[2] == 'X' and line3[2] == 'X' and line4[2] == 'X':
        win = 1
    elif line2[3] == 'X' and line3[3] == 'X' and line4[3] == 'X':
        win = 1
    elif line2[1] == 'X' and line3[1] == 'X' and line4[1] == 'X':
        win = 1
    elif line2[1] == 'X' and line3[2] == 'X' and line4[3] == 'X':
        win = 1
    elif line2[3] == 'X' and line3[2] == 'X' and line4[1] == 'X':
        win = 1
    if turn%2 == 0:
        print("Omai god Other Guy won WOOOW :shock:")
    else:
        print("haha Other Guy noob, Player One won")

def intro(): #basic intro with instructions
    print("Welcome to Tic Tac Toe by Luth and Jie Rei.\n")
    print("The rules are simple. You play against a friend, or yourself, if you have no friends.\n")
    print("You can play on the board in the following way:")
    print("When asked for your row, input your selected row number.\n")
    print("When asked for your column, input your selected column number.\n")
    wanttoplay = input("Do you want to play? (y/n): ") #determines if player wants to play
    if wanttoplay == "y": 
        print("Let's play!")
        main()

intro() #starts the program