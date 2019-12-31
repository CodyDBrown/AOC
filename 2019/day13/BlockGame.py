from IntcodeComputerV8 import IntcodeComputer
from PIL import Image

class Block():
    def __init__(self, x, y, Type):
        self.x = x
        self.y = y
        self.Type = Type

class Game():
    def __init__(self, code):
        self.code = code
        self.REL_BASE = 0
        self.INDEX = 0
        self.Blocks = []
        # For part 2 I want the paddle to move to get the ball so I need to know
        # Where the paddle and ball are. 
        self.BallX = 0
        self.PaddleX = 0
        
    def GetBrick(self):
        INPUT = self.BallX - self.PaddleX
        self.code, blockX, self.INDEX, self.REL_BASE  = IntcodeComputer(self.code, 
                                                                        INPUT = INPUT,
                                                                        REL_BASE=self.REL_BASE,
                                                                        INDEX=self.INDEX)
        # Check if we hit the hault command
        if blockX is None:
            print("Hault command")
            return False
        self.code, blockY, self.INDEX, self.REL_BASE  = IntcodeComputer(self.code,
                                                                        INPUT = INPUT,
                                                                        REL_BASE=self.REL_BASE,
                                                                        INDEX=self.INDEX)
        
        self.code, blockType, self.INDEX, self.REL_BASE  = IntcodeComputer(self.code,
                                                                           INPUT = INPUT,
                                                                           REL_BASE=self.REL_BASE,
                                                                           INDEX=self.INDEX)
        
        
        if blockX > 0:
            self.Blocks.append(Block(blockX, blockY, blockType))
            # While were at it lets get the paddle and ball location and put the
            # paddle under the ball?
            if blockType == 3:
                self.PaddleX = blockX
            elif blockType == 4:
                self.BallX = blockX
            
        elif blockX == -1 and blockY == 0:
            print("Score is now: ", blockType)
        return True
        
    def PrintBlocks(self):
        for block in self.Blocks:
            print(block.x, block.y, block.Type)
        print("There are ", len(self.Blocks), "tiles.")
            
    def main(self):
        FLAG = True
        while FLAG:
            FLAG = self.GetBrick()
            self.MakeImage()
        return 0
    
        
            
    def MakeImage(self):
        img = Image.new('RGB',(41, 25), color = 'white')
        imgData = img.load()
        for b in range(len(self.Blocks)):
            # Empty
            if self.Blocks[b].Type == 0:
                imgData[self.Blocks[b].x, self.Blocks[b].y] = (255, 255, 255)
            # Wall
            elif self.Blocks[b].Type == 1:
                imgData[self.Blocks[b].x, self.Blocks[b].y] = (0, 0, 0)
            # Block
            elif self.Blocks[b].Type == 2:
                imgData[self.Blocks[b].x, self.Blocks[b].y] = (0, 0, 255)
            # Ball
            elif self.Blocks[b].Type == 3:
                imgData[self.Blocks[b].x, self.Blocks[b].y] = (255, 0, 0)
            # Paddel
            elif self.Blocks[b].Type == 4:
                imgData[self.Blocks[b].x, self.Blocks[b].y] = (0, 255, 0)
        img = img.resize((400, 210))
        img.show()
        # img.save("day13.png")
            
        
        