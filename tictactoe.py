#this is bad tictactoe throw it
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player = "X"

def display():
    for i in board:
        print(board[board.index(i)])

def main():
    global board
    global player
    while True:
        if player == "X":
            print("Player 1's turn")
        else:
            print("Player 2's turn")
        move = input("Where would you like to move? ")
        move = move.split(",")
        move[0] = int(move[0])
        move[1] = int(move[1])
        if board[move[0]][move[1]] == " ":
            board[move[0]][move[1]] = player
            display()
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That space is already taken!")

def intro():
    print("Welcome to Tic Tac Toe by Luth and Jie Rei.\n")
    print("The rules are simple. You play against a friend, or yourself, if you have no friends.\n")
    print("You can play on the board in the following way:")
    print("When asked for your row, input your selected row number.\n")
    print("When asked for your column, input your selected column number.\n")
    wanttoplay = input("Do you want to play? (y/n): ")
    if wanttoplay == "y":
        print("Let's play!")
        main()

intro()