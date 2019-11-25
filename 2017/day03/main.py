import pandas
import numpy as np

xPos = 0
yPos = 0 
count = 1

steps = 1

MOVEUP = False
MOVEDOWN = False
MOVERIGHT = True
MOVELEFT = False

def resetGlobals():
    global xPos
    global yPos
    
    global count
    global steps
    global MOVEUP
    global MOVEDOWN
    global MOVERIGHT
    global MOVELEFT
    
    xPos = 0
    yPos = 0 
    count = 1
    
    steps = 1
    
    MOVEUP = False
    MOVEDOWN = False
    MOVERIGHT = True
    MOVELEFT = False
    

def moveNext():
    global xPos
    global yPos
    
    global count
    global steps
    global MOVEUP
    global MOVEDOWN
    global MOVERIGHT
    global MOVELEFT
    
    if MOVERIGHT:
        xPos += 1
    if MOVELEFT:
        xPos -= 1
    if MOVEUP:
        yPos += 1
    if MOVEDOWN:
        yPos -= 1
        
    count += 1
    
    if( xPos == steps and yPos == -steps):
        steps += 1
    # Check if I should change direction
    if( xPos == steps and MOVERIGHT):
        MOVERIGHT = False 
        MOVEUP = True
    elif( yPos == steps and MOVEUP):
        MOVEUP = False
        MOVELEFT = True
    elif( abs(xPos) == steps and MOVELEFT):
        MOVELEFT = False
        MOVEDOWN = True
    elif( yPos == -steps and MOVEDOWN):
        MOVEDOWN = False
        MOVERIGHT = True
        
def addLocation(dataFrame):
    global xPos
    moveNext()

    dataFrame.loc[count]['x'] = xPos
    dataFrame.loc[count]['y'] = yPos
    return dataFrame

def partOneMain():
    global xPos
    global yPos
    global count
    xPos = 0
    yPos = 0
    cell = 361527
    

    for i in range(cell -1):
        moveNext()
    print("Answer to part one: ", abs(xPos) + abs(yPos))

def partTwoMain():
    global xPos
    global yPos
    global count
    resetGlobals()
    count = 0
    Grid = pandas.DataFrame(0, index = range(10), columns=['x', 'y', 'ANS'])
    for i in range(len(Grid)-1):
        Grid = addLocation(Grid)
    Grid.loc[0]['ANS'] = 1;
   
    print(Grid)

if __name__ == "__main__":
    partOneMain()
    partTwoMain()