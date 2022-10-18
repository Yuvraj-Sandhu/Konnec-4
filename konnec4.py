dollars = '$'
euros = '€'
class CurrencyPiece :
    def __init__(self,team_name):
        if type(team_name) == str:
            if team_name.lower().replace(" ","") == "dollars": self.team_name = "Dollars"
            elif team_name.lower().replace(" ","") == "euros": self.team_name = "Euros"
            else: raise ValueError
        elif type(team_name) == int:
            if team_name == 0: self.team_name = "Dollars"
            elif team_name == 1: self.team_name = "Euros"
            else: raise ValueError
        else: raise TypeError

    def __str__(self):
        if self.team_name == "Dollars":
            return dollars
        elif self.team_name == "Euros":
            return euros 

class Board:
    def __init__(self):
        self.current = "Dollars"
        self.board = [[None,None,None,None,None,None,None],
                      [None,None,None,None,None,None,None],
                      [None,None,None,None,None,None,None],
                      [None,None,None,None,None,None,None],
                      [None,None,None,None,None,None,None],
                      [None,None,None,None,None,None,None],
                     ]
        
    def addPiece(self, column):
        c = 0
        if column > 8 or column < 1: raise ValueError 
        coin = None
        if self.current == "Dollars": coin = CurrencyPiece("dollars")
        elif self.current == "Euros": coin = CurrencyPiece("euros") 

        for row in range(6): 

            if self.board[row][column-1] != None:
                if row != 0:
                    self.board[row-1][column-1] = coin 
                    break
                else:
                    c = 1
                    break 
            elif self.board[row][column-1] == None:
                if row == 5:
                    self.board[row][column-1] = coin 
                    break 
        
        if c == 0:
            if self.current == "Dollars": self.current = "Euros"
            elif self.current == "Euros": self.current = "Dollars" 
    
    def checkWinner(self):
        def horizontalchecker(coin):
            for i in range(6):
                for j in range(4):
                    if str(self.board[i][j]) == coin and str(self.board[i][j+1]) == coin and str(self.board[i][j+2]) == coin and str(self.board[i][j+3]) == coin:
                        return True
        def verticalchecker(coin):
            for i in range(3):
                for j in range(7):
                    if str(self.board[i][j]) == coin and str(self.board[i+1][j]) == coin and str(self.board[i+2][j]) == coin and str(self.board[i+3][j]) == coin:
                        return True
        def positivechecker(coin):
            for i in range(3):
                for j in range(4):
                    if str(self.board[i][j]) == coin and str(self.board[i+1][j+1]) == coin and str(self.board[i+2][j+2]) == coin and str(self.board[i+3][j+3]) == coin:
                        return True 
        def negativechecker(coin):
            for i in range(3):
                for j in range(4,7):
                    if str(self.board[i][j]) == coin and str(self.board[i+1][j-1]) == coin and str(self.board[i+2][j-2]) == coin and str(self.board[i+3][j-3]) == coin:
                        return True

        coin = dollars
        if horizontalchecker(coin) == True or verticalchecker(coin) == True or positivechecker(coin) == True or negativechecker(coin) == True:
            return "Dollars"
        else:
            coin = euros
            if horizontalchecker(coin) == True or verticalchecker(coin) == True or positivechecker(coin) == True or negativechecker(coin) == True:
                return "Euros" 
            else: return False 

    def parseMove(self,column,row=1):
        return True
    
    def __str__(self) -> str:
        s = "╔" + ("══╦" * 6) + "═" * 3 + "╗\n"
        for row_index, row in enumerate(self.board):
            s += "║"
            for col_index, column in enumerate(row):
                s += f" {str(column if column != None else ' ')} ║"
            if row_index < 5:
                s += "\n╠" + ("═══╬" * 6) + "═══╣\n"
            else:
                s += '\n'
        return s + "╚" + "═══╩" * 6 + "═" * 3 + "╝\n"

#don't delete this code.

from IPython.display import clear_output
board = Board()
moves = []
while board.checkWinner() == False:
    clear_output()
    print("Board:")
    print(str(board))
    print("Current Player:", board.current)
    print(f'Past Moves: {moves}')
    column = input("Pick a column to place your coin! >> ")
    try:
        if column.lower() in ('q', "quit", 'e', "exit"):
            break
        column = int(column)
        moves.append(column)
        try:
            if board.parseMove((1, column)):
                board.addPiece(column)
            else:
                print("That is an invalid move!")
        except Exception as e:
            print("An error occured:", e)
    except Exception as e:
        print("Uh oh... An error occured:", e)
if board.checkWinner():
    clear_output()
    print("\nBoard:")
    print(str(board))
    print("And the winner is:", board.checkWinner())
    print(f'Moves: {moves}')