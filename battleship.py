"""
Battleship Project
Name: Khadeer
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    # data["name"] = value

    data.update({"rows":10,"cols":10,"board_size":500})                     # adding values to empty dictonary using update method - Type 1
    data["cellsize"] = (data["board_size"]*2)//(data["cols"]+data["rows"])      # adding value to existing dict one by one - Type 2
    data["n_comp_ships"] = 5
    data["n_user_ships"] = 0
    data["user_board"] = emptyGrid(data["rows"], data["cols"])
    #data["user_board"] = test.testGrid()                            # temporarily setting your user grid = test.testGrid()
    data["temp_ship"] = []                                           # intialising temp list as list (2D List)
    data["comp_board"] = emptyGrid(data["rows"], data["cols"])              # Becomes input in the next step
    data["comp_board"] = addShips(data["comp_board"],data["n_comp_ships"])       # replacing the value for the same key

    return ()


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data, compCanvas, data["comp_board"], showShips=True)
    drawGrid(data, userCanvas, data["user_board"], showShips=True)

    drawShip(data, userCanvas, ship=test.testShip())

    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    grid = [[EMPTY_UNCLICKED for col in range(cols)] for row in range(rows)]
    return grid


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    x_cord_ship_c = random.randint(1,8)
    y_cord_ship_c = random.randint(1,8)
    align_ship = random.randint(0,1)

    if (align_ship == 0): #assuming 0 represents vertical
        position_ship = [[x_cord_ship_c-1,y_cord_ship_c],[x_cord_ship_c,y_cord_ship_c],[x_cord_ship_c+1,y_cord_ship_c]]
    else:
       position_ship  = [[x_cord_ship_c,y_cord_ship_c-1],[x_cord_ship_c,y_cord_ship_c],[x_cord_ship_c,y_cord_ship_c+1]]

    return position_ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    lst_v = []
    lst_E = [EMPTY_UNCLICKED for i in range(len(ship))]     # creating a list of 3 elements
    for i in range(len(ship)):
        xcor = ship[i][0]
        ycor = ship[i][1]
        lst_v.append(grid[xcor][ycor])      # lst_v (2D) appends grid(ship(cordinates))
    
    if (lst_v == lst_E):    # comparing element by element of the list
        return True
    else:
        return False


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    while (numShips>0):
        ship = createShip()
        v_ship = checkShip(grid,ship)
        if (v_ship == True):
            for i in range(len(ship)):
                xcor = ship[i][0]
                ycor = ship[i][1]
                grid[xcor][ycor] = SHIP_UNCLICKED
            numShips -= 1 
    return (grid)


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):

    for i in range(data["cols"]):
        for j in range(data["rows"]):
            x_cor = 0 + data["cellsize"]*j
            y_cor = 0 + data["cellsize"]*i
            if (grid[i][j]==SHIP_UNCLICKED):
                canvas.create_rectangle(x_cor, y_cor, x_cor+data["cellsize"], y_cor+data["cellsize"], fill="yellow", width= 1)
            else:
                canvas.create_rectangle(x_cor, y_cor, x_cor+data["cellsize"], y_cor+data["cellsize"], fill="blue", width= 1)

    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):

    if ((ship[0][1]) == (ship[1][1]) == (ship[2][1])):
        if ((ship[0][0] + 2) == (ship[1][0] + 1) == (ship[2][0])):
            return True
        elif ((ship[0][0] ) == (ship[1][0] + 1) == (ship[2][0] + 2)):
            return True
        elif ((ship[0][0]) == (ship[1][0] + 2) == (ship[2][0] + 1)):
            return True
        else:
            return False
    else:
        return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    if ((ship[0][0]) == (ship[1][0]) == (ship[2][0])):
        if ((ship[0][1] + 2) == (ship[1][1] + 1) == (ship[2][1])):
            return True
        elif ((ship[0][1] ) == (ship[1][1] + 1) == (ship[2][1] + 2)):
            return True
        elif ((ship[0][1]) == (ship[1][1] + 2) == (ship[2][1] + 1)):
            return True
        else:
            return False
    else:
        return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    c_factor = data["cellsize"]
    grid_cor = [event.y//c_factor,event.x//c_factor]
    return grid_cor


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in range(len(ship)):
        x_cor_t_tship = ship[i][1]*data["cellsize"]
        x_cor_b_tship = ship[i][1]*data["cellsize"] + data["cellsize"]
        y_cor_t_tship = ship[i][0]*data["cellsize"]
        y_cor_b_tship = ship[i][0]*data["cellsize"] + data["cellsize"]
        
        canvas.create_rectangle(x_cor_t_tship, y_cor_t_tship, x_cor_b_tship, y_cor_b_tship, fill="white", width=1)
        
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship) == 3:
        for i in (range(len(ship))):
            if (grid[ship[i][0]][ship[i][1]]) == EMPTY_UNCLICKED:
                if (isVertical(ship) == True or isHorizontal(ship) == True):
                    pass
                else:
                    #print("Creating ship is not valid, placing Vertically or Horizontally is only possible")
                    return False
            else:
                #print("Creating ship is not possible as there another ship already there")
                return False
        return True
    else:
        #print("Creating ship is not possible as it does not match size requirments")
        return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):

    user_grid = data["user_board"]
    t_ship = data["temp_ship"]

    if (shipIsValid(user_grid, t_ship) == True):
        for i in (range(len(t_ship))):
             user_grid[t_ship[i][0]][t_ship[i][1]] = SHIP_UNCLICKED
        data["temp_ship"] = []
        data["n_user_ships"] += 1
    else:
        print("Ship is not valid")
        data["temp_ship"] = []
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):

    if (data["n_user_ships"] == 5):
        return
    else:
        for i in range(len(data["temp_ship"])):
            if (row == data["temp_ship"][i][0] and col == data["temp_ship"][i][1]):
                return
            else:
                data["temp_ship"] += [[row,col]]
                if (len(data["temp_ship"]) == 3):
                    placeShip(data)
                    if (data["n_user_ships"] == 5):
                        print("You can start the game")
                    else:
                        return
                else:
                    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":

    ## Finally, run the simulation to test it manually ##
    ## runSimulation(500, 500)
    test.testShipIsValid()