import numpy as np
from multiprocessing import Process
import datetime as dt

class Segment():
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.xdelta = self.x1 - self.x0
        self.ydelta = self.y1 - self.y0

        

class Wire():
    def __init__(self):
        self.StartingPoint = [0,0]
        self.Segments = []
        
    def AddSegment(self, step):
        # Find the direction to move
        segment = Segment(self.StartingPoint[0], self.StartingPoint[1], step[0], step[1])
        self.Segments.append(segment)
        self.StartingPoint = step
    
    def FindStep(self, moveInstruction):
        # Get either right left up or down
        direction = moveInstruction[0]
        distance = int(moveInstruction[1:])
        if direction == 'R':
            xFinal = self.StartingPoint[0] + distance
            yFinal = self.StartingPoint[1]
            return [xFinal, yFinal]
        elif direction == 'L':
            xFinal = self.StartingPoint[0] - distance
            yFinal = self.StartingPoint[1]
            return [xFinal, yFinal]
        elif direction == 'U':
            xFinal = self.StartingPoint[0]
            yFinal = self.StartingPoint[1] + distance
            return [xFinal, yFinal]
        elif direction == 'D':
            xFinal = self.StartingPoint[0]
            yFinal = self.StartingPoint[1] - distance
            return [xFinal, yFinal]
        else:
            print("Improper direction")
            return None
        
def fileToList(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    text = text.split('\n')
    for t in range(len(text)):
        text[t] = text[t].split(',')
    text = np.array(text)
    return text

def CrossPoints(WireOne, WireTwo):
    
    wireOneHorizontalSegments = []
    wireOneVerticalSegments = []
    
    wireTwoHorizontalSegments = []
    wireTwoVerticalSegments = []
    
    # Make lists of the horizontal and vertical segments for both parts.
    for segment in WireOne.Segments:
        if abs(segment.xdelta) > 0:
            wireOneHorizontalSegments.append(segment)
        else:
            wireOneVerticalSegments.append(segment)
            
    for segment in WireTwo.Segments:
        if abs(segment.xdelta) > 0:
            wireTwoHorizontalSegments.append(segment)
        else:
            wireTwoVerticalSegments.append(segment)
    
    CrossList = []
    
    # Only need to check W1 horizontal with W2 vertical and vice versa
    for horizontalSegment in wireOneHorizontalSegments:
        for verticalSegment in wireTwoVerticalSegments:
            xLocation = sorted([horizontalSegment.x0, horizontalSegment.x1])
            yLocation = sorted([verticalSegment.y0, verticalSegment.y1])
            if verticalSegment.x0 in range(xLocation[0], xLocation[1]):
                if horizontalSegment.y0 in range(yLocation[0], yLocation[1]):
                    CrossList.append([verticalSegment.x0, horizontalSegment.y0])
                
    for horizontalSegment in wireTwoHorizontalSegments:
        for verticalSegment in wireOneVerticalSegments:
            xLocation = sorted([horizontalSegment.x0, horizontalSegment.x1])
            yLocation = sorted([verticalSegment.y0, verticalSegment.y1])
            if verticalSegment.x0 in range(xLocation[0], xLocation[1]):
                if horizontalSegment.y0 in range(yLocation[0], yLocation[1]):
                    CrossList.append([verticalSegment.x0, horizontalSegment.y0])
        
    return CrossList


    
def ManhattanDistance(point):
    return (abs(point[0]) + abs(point[1]))        

def partOneMain():
    tstart = dt.datetime.now()
    movementList = fileToList("input.txt")
    WireOne = Wire()
    WireTwo = Wire()
    for move in movementList[0]:
        step = WireOne.FindStep(move)
        WireOne.AddSegment(step)
    for move in movementList[1]:
        step = WireTwo.FindStep(move)
        WireTwo.AddSegment(step)
    CrossList = CrossPoints(WireOne, WireTwo)
    print(CrossList)
    
    minDist = 10**5
    for point in CrossList:
        dist = ManhattanDistance(point)
        if dist < minDist and dist > 0:
            minDist = dist
    print("Answer to part one is: ", minDist)
    print("My Solution took:", dt.datetime.now() - tstart)
    
    
    
        
    
def partTwoMain():
    # This part I cheated and saw someone elses answer. It's really good and has
    # a cool trick I hadn't seen before. 
    tstart = dt.datetime.now()
    A,B, = open('input.txt').read().split('\n')
    A,B = [x.split(',') for x in [A,B]]

    DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
    DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
    def get_points(A):
        x = 0
        y = 0
        length = 0
        ans = {}
        for cmd in A:
            d = cmd[0]
            n = int(cmd[1:])
            assert d in ['L', 'R', 'U', 'D']
            for _ in range(n):
                x += DX[d]
                y += DY[d]
                length += 1
                if (x,y) not in ans:
                    # I did not know that dictionary keys could be a pair of values
                    # This shoulnd't be surprising because I could have string keys
                    # and just turn this key into a string if i really wanted to
                    # but this works really well and I'm going to learn from it!
                    ans[(x,y)] = length
        return ans

    PA = get_points(A)
    PB = get_points(B)
    both = set(PA.keys())&set(PB.keys())
    part1 = min([abs(x)+abs(y) for (x,y) in both])
    print("His Solution took:", dt.datetime.now() - tstart)
    part2 = min([PA[p]+PB[p] for p in both])
    print(part1,part2)
    
    # My solution for part 1 is faster so I've got that going for me???

if __name__ == "__main__":
    partOneMain()
    partTwoMain()