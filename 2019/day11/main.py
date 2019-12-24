from RobotComputer import Robot
from PIL import Image

def fileToList(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    text = text.split(',')
    numberList = []
    for n in text:
        numberList.append(int(n))
    return numberList

def addMemory(numbers):
    for _ in range(len(numbers)*100):
        numbers.append(0)
    return numbers

def PrintPannels(Pannels):
    img = Image.new('RGB',(50, 50), color = 'red')
    imgData = img.load()
    for P in Pannels:
        if Pannels[P].color == "white":
            print(Pannels[P].x, Pannels[P].y)
            imgData[Pannels[P].x + 20, Pannels[P].y + 20] = (255,255,255)
        elif Pannels[P].color == "black":
            imgData[Pannels[P].x + 20, Pannels[P].y + 20] = (0,0,0)
    img.show()
    img.save("day11.png")

def partOne():
    numbers = fileToList("input.txt")
    numbers = addMemory(numbers)
    Bob = Robot(numbers)
    Pannels = Bob.Main()
    print(len(Pannels))
def partTwo():
    numbers = fileToList("input.txt")
    numbers = addMemory(numbers)
    Bob = Robot(numbers)
    Pannels = Bob.Main(INPUT = 1)
    PrintPannels(Pannels)

if __name__ == "__main__":
    #partOne()
    partTwo()