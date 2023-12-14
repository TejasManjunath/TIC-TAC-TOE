import random

def outline(board):
    for row in board:
        print(" | ".join(row))
        print(" "*9)

def check_winner(board,player):
    for i in range(3):
        if all (board[i][j]== player for j in range(3)) or all (board[j][i]== player for j in range(3)):
            return True
    if all(board[i][i]== player for i in range(3)) or all(board[i][2-i]== player for i in range(3)):
        return True
    return False

def playerturn(board,player):
    while True:
        try:
            outline(board)
            move= int(input(f"Player {player}, Enter the move(1-9):"))
            if 0 ==move:
                End()
    
            if 1<=move <=9:
                row=(move-1)//3
                col=(move-1)%3
                if board[row][col]==" ":
                    return row,col
                else:
                    print("POSITION ALREADY TAKEN, MAKE THE MOVE AGAIN.")
            else:
                print("Enter a number between 1 and 9.")
        except ValueError:
            print("Are you dumb bro ,can't you read the message that says (Enter a number between 1 and 9.) ")

def playagain():
    while True:
        choice1 = input("Had fun with your last game? (yes/no): ")
        if choice1 == 'yes':
            choice2 = input("Do you want to play again? (yes/no):").lower()
            if choice2 in ['yes','no']:
                return choice2=='yes'
            else:
                print("bruhhh ,enter 'yes' or 'no'.")
        else:
                print("bruhhh ,enter 'yes' or 'no'.")
                
def tie(board):
    for row in board:
        if " " in row:
            return False
    return True
                
def main():
    print("Hello there lets start the game.")
    while True:
        board=[[" " for _ in range(3)] for _ in range(3)]
        players=["X","O"]
        random.shuffle(players)
        currentplayer =players[0]
        game_over=False
        
        while not game_over:
            row,col=playerturn(board,currentplayer)
            board[row][col]= currentplayer
            
            if check_winner(board,currentplayer):
                outline(board)
                print(f"{currentplayer} wins!")
                game_over=True
            elif tie(board):
                outline(board)
                print("It's a draw!")
                game_over=True
            else:
                currentplayer = players[1] if currentplayer == players[0] else players[0]
                
                
        if not playagain():
            print("Thanks for trying the game.")
            break

def End():
    print("Thanks for trying the game.")
    exit()

if __name__=="__main__":
    main()