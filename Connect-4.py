import sys
from time import sleep
def checkcolumn(c):
    #checkcolumn(c) checks if the top cth column has atleast one empty spot
    if board[0][c-1] == '.':
        return True
    return False    
def checkwin(ab):
    #checkwin(ab) prints which player wins if any and returns True if a player has won or returns False otherwise
    if ab==0:
        t='X'
    else:
        t='O'
    for row in range(0,6):
        for column in range(0, 7):
            if column<=3 and t==board[row][column] and t==board[row][column+1] and t==board[row][column+2] and t==board[row][column+3]:
                print "Player "+ str(ab+1) +" wins!"
                return True
            if row<=2 and t==board[row][column] and t==board[row+1][column] and t==board[row+2][column] and t==board[row+3][column]:
                print "Player "+ str(ab+1) +" wins!"
                return True
            if column>=3 and row<=2 and t==board[row][column] and t==board[row+1][column-1] and t==board[row+2][column-2] and t==board[row+3][column-3]:
                print "Player "+ str(ab+1) +" wins!"
                return True
            if column<=3 and row<=2 and t==board[row][column] and t==board[row+1][column+1] and t==board[row+2][column+2] and t==board[row+3][column+3]:
                print "Player "+ str(ab+1) +" wins!"
                return True
    return False    
win=0  
board=[['.', '.', '.' ,'.', '.', '.' ,'.'],['.', '.', '.' ,'.', '.', '.' ,'.'],['.', '.', '.' ,'.', '.', '.' ,'.'],['.', '.', '.' ,'.', '.', '.' ,'.'],['.', '.', '.' ,'.', '.', '.' ,'.'],['.', '.', '.' ,'.', '.', '.' ,'.']]
def startGame() :
    words = "Greetings Stranger(s)! "
    #Experimental Typing
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    print ""
    words = "Welcome to my Connect-4 Game! Do you know the rules to the game?(Y/N)"
    #Experimental Typing
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    c=raw_input("")
    if c=="N":
        words = "The rules of this game are simple you connect 4 of X's or the O's, vertically,horizontally or diagonally to win the game."
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
    print ""
    GameOn()
def GameOn():
    t=0 
    while(t<=42):
        for row in board:
            for x in row:
                sys.stdout.write(x+" ")
            print("")
        if t==42:
            #If the board is Full and there is no winner
            print("TIE! Game TIED!")
            break  
        k=0  
        while(k==0):
            c=raw_input("Choose your column, mate "+str(t%2 + 1)+ "!(1-7): ")
            if c not in "0123456789" or c=="":
                print "Choose an integer between 1-7!"
        
            else:
                c=int(c)
                if c<=0 or c>=8:
                    print "Choose between 1-7!"
                elif not checkcolumn(c):
                    print "Column full,try another column!"
                else:
                    board.reverse()
                    for x in board:
                        if x[c-1]=='.':
                            if t%2==0:
                                x[c-1]='X'
                                break
                            else:
                                x[c-1]='O'
                                break  
                    board.reverse()                       
                    k=1   
        if checkwin(t%2):
            for row in board:
                for x in row:
                    sys.stdout.write(x+" ")
                print ""
            break
        t=t+1;
startGame()
        
            
           
         

        
    
