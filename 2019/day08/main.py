from SpaceImage import SpaceImage

def ReadInNumbers(filePath):
    inputFile = open(filePath, 'r')
    numbers = inputFile.read()
    inputFile.close()
  
    # numbers is currently a string so we need 
    # to turn it into a list of numbers
    numbersInt = [int(n) for n in numbers]
    return numbersInt

def partOneMain():
    imageCode = ReadInNumbers("input.txt")
    image = SpaceImage(width=25, height=6, code = imageCode)
    image.SetLayers()
    ZeroistLayer = image.LayerWithFewestZeros()
    ones = image.CountInLayer(ZeroistLayer, 1)
    twos = image.CountInLayer(ZeroistLayer, 2)

    print("The zeroist layer is layers {}, it has {} one's and {} twos' in it.".format(ZeroistLayer, ones, twos))
    print("The answer to part one is:", ones*twos)
    
    
    
def partTwoMain():
    imageCode = ReadInNumbers("input.txt")
    image = SpaceImage(width=25, height=6, code = imageCode)
    image.SetLayers()
    pix = image.GetSetPixles()
    image.ShowImage(pix)
if __name__ == "__main__":
    partOneMain()
    partTwoMain()
    