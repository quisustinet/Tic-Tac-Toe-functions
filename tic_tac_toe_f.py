from random import randrange
#from os import system, name    
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    line=3*"+-------"+"+"
    print(line)
    for i in range(3):
        print(3*"|       ", sep="", end="|\n")
        for j in range(3):
            print("|   ",board[i][j],"   ", sep="", end="")
        print("|")
        print(3*"|       ", sep="", end="|\n")
        print(line)
    print("\n")
    
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    # and prints it out to the console.
    global next_move_user
    try:
        move=int(input("Enter your move:"))
    except:
        print("Your move should be an integer number.")
    if move < 1:
        print("You can't do this move. Try again.")
    elif move < 4:
        if type(board[0][move-1])==int:
            board[0][move-1]="O"
            next_move_user=0
    elif move < 7:
        if type(board[1][move-3-1])==int:
            board[1][move-3-1]="O"
            next_move_user=0
    elif move < 10:
        if type(board[2][move-6-1])==int:
            board[2][move-6-1]="O"
            next_move_user=0
    else:
        print("You can't do this move. Try again.")

def comp_move(board):
    global next_move_user
    # The function draws the computer's move and updates the board.
    move=randrange(1,10)
    if move < 4:
        if type(board[0][move-1])==int:
            board[0][move-1]="X"
            next_move_user=1
                    
    elif move < 7:
        if type(board[1][move-3-1])==int:
            board[1][move-3-1]="X"
            next_move_user=1
        
    else:
        if type(board[2][move-6-1])==int:
            board[2][move-6-1]="X"
            next_move_user=1
        
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    # and prints it out to the console.
    global free_fields
    free_fields=[]
    for i in board:
        for j in i:
            s=(board.index(i),i.index(j))
            if type(j)==int and s not in free_fields:
                free_fields.append(s)
                   
def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # and prints it out to the console.
    for i in range(3):
        if board[i][0]==sign and board[i][1]==sign and board[i][2]==sign:
            return True
    for i in range(3):
        if board[0][i]==sign and board[1][i]==sign and board[2][i]==sign:
            return True
    if board[0][0]==sign and board[1][1]==sign and board[2][2]==sign:
        return True
    if board[0][2]==sign and board[1][1]==sign and board[2][0]==sign:
        return True
def create_board():
    global board
    board=[]
    n=1
    for i in range(3):
        row=[n+i for i in range(3)]
        board.append(row)
        n+=3
        
create_board()
next_move_user=randrange(2)
make_list_of_free_fields(board)
while len(free_fields) > 0:
    display_board(board)
    if next_move_user:
        enter_move(board)
    else:
        comp_move(board)
        make_list_of_free_fields(board)
    if victory_for(board, "X"):
        display_board(board)
        print("Computer won.\n")
        exit()
    elif victory_for(board, "O"):
        display_board(board)
        print("You won.\n")
        exit()
display_board(board)
print("\nDraw.\n")


