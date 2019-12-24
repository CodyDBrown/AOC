from IntcodeComputerV7 import IntcodeComputer
from Pannel import Pannel

class Robot():
    def __init__(self, code):
        self.code = code
        self.INDEX = 0
        self.REL_BASE = 0
        
        # Where the robot is
        self.x = 0
        self.y = 0
        
        # What direction the robot is facing
        self.faceing = "N"
        
        
    def RunNextStep(self, INPUT):
        self.code, OUTPUT, self.INDEX, self. REL_BASE = IntcodeComputer(self.code,
                                                                        INPUT,
                                                                        self.INDEX,
                                                                        self.REL_BASE)
        return OUTPUT
    
    def Turn(self, turn):
        if self.faceing == 'N' and turn == "left":
            self.faceing = 'W'
        elif self.faceing == 'N' and turn == "right":
            self.faceing = 'E'
            
        elif self.faceing == 'E' and turn == "left":
            self.faceing = 'N'
        elif self.faceing == 'E' and turn == "right":
            self.faceing = 'S'
            
        elif self.faceing == 'S' and turn == "left":
            self.faceing = 'E'
        elif self.faceing == 'S' and turn == "right":
            self.faceing = 'W'
            
        elif self.faceing == 'W' and turn == "left":
            self.faceing = 'S'
        elif self.faceing == 'W' and turn == "right":
            self.faceing = 'N'
                       
        
    def Main(self, INPUT=0):
        # Dictionary where we'll put the pannels we create. Part 2 says that we
        # start on a white pannel
        Pannels = {(0,0): Pannel(0,0)}
        Pannels[(0,0)].color = "white"
        while True:
            outcount = 0    
            # First thing we want to do is check if the pannel we're on already
            # exists or not. If it doesn't exist then make it
            if (self.x, self.y) not in Pannels:
                Pannels[(self.x, self.y)] = Pannel(self.x, self.y)
            
            # The input for the Robot IntcodeComputer depends on the color of 
            # the tile it's on. If it's black then input 0, if white then input
            # 1. 
            if Pannels[(self.x, self.y)].color == "black":
                INPUT = 0
            elif Pannels[(self.x,self.y)].color == "white":
                INPUT = 1
            
            # Need two outputs before we move the robot. 
            # Get the first output
            while outcount < 2:
                OUTPUT = self.RunNextStep(INPUT)
                if OUTPUT is None:
                    return Pannels
                outcount += 1
                # First output says what color to paint the pannel
                if outcount == 1:
                    if OUTPUT == 0:
                        Pannels[(self.x,self.y)].color = "black"
                    elif OUTPUT == 1:
                        Pannels[(self.x,self.y)].color = "white"
                # second output tells us which way to turn
                elif outcount == 2:
                    if OUTPUT == 0:
                        turn = "left"
                    elif OUTPUT == 1:
                        turn = "right"
                    self.Turn(turn)
                    # Now that we turned we need to move forward one in that 
                    # direction
                    if self.faceing == 'N':
                        self.y += 1
                    elif self.faceing == 'E':
                        self.x += 1
                    elif self.faceing == 'S':
                        self.y -= 1
                    elif self.faceing == 'W':
                        self.x -= 1
