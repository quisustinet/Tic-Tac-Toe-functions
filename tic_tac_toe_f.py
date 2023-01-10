from random import randrange
from os import system
    
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
    

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    # and prints it out to the console.
    move=int(input("Enter your move:"))
    if move < 4 and type(board[0][move-1])==int :
        board[0][move-1]="O"
    elif move < 7 and type(board[1][move-3-1])==int :
        board[1][move-3-1]="O"
    elif move < 10 and type(board[2][move-6-1])==int :
            board[2][move-6-1]="O"
    else:
        print("You can't do this move. Try again.")
        enter_move(board)

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
            #else:
                #free_fields.remove(s)
                
    

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # and prints it out to the console.
    return 0

def draw_move(board):
    # The function draws the computer's move and updates the board.
    # and prints it out to the console.
    return 0


board=[]
n=1
for i in range(3):
    row=[n+i for i in range(3)]
    board.append(row)
    n+=3
board[1][1]='X'
print(board)
display_board(board)
make_list_of_free_fields(board)
print(free_fields)
while True:
    enter_move(board)
    os.system("cls")
    display_board(board)
    print(board)
    make_list_of_free_fields(board)
    print(free_fields)