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