from PIL import Image

class SpaceImage():
    def __init__(self, width, height, code):
        self.width = width
        self.height = height
        self.code = code
        self.codeIndex = 0
        self.Layers = []
        
    def SetLayer(self):
        Layer = []
        for col in range(self.height):
            Row = []
            for row in range(self.width):
                Row.append(self.code[self.codeIndex])
                self.codeIndex += 1
            Layer.append(Row)
        self.Layers.append(Layer)
        assert(self.codeIndex == (self.width*self.height*len(self.Layers)) )
        return 0
    
    def SetLayers(self):
        self.codeIndex = 0
        self.Layers= []
        while self.codeIndex < len(self.code):
            self.SetLayer()
        return 0
    
    def GetSetPixles(self):
        PixleValues = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(2)
            PixleValues.append(row)
        for l in range(len(self.Layers)):
            for r in range(len(self.Layers[l])):
                for c in range(len(self.Layers[l][r])):
          
                    # Check if the pixel is transparent or not
                    if PixleValues[r][c] == 2:
                        if self.Layers[l][r][c] == 0:
                            PixleValues[r][c] = (0,0,0)
                            
                        elif self.Layers[l][r][c] == 1:
                            PixleValues[r][c] = (255,255,255)
                            
                        else:
                            PixleValues[r][c] = 2
        return PixleValues
            
    def ShowImage(self, Pixels):
        img = Image.new('RGB',(self.width, self.height), color = 'red')
        imgData = img.load()
    
        for row in range(self.height):
            for c in range(self.width):
                imgData[c,row] = Pixels[row][c]
        img = img.resize((self.width*100, self.height*100))
        img.show()
    
    
    def LayerWithFewestZeros(self):
        leastZeroLayer = -1
        leastZeroCount = self.width * self.height
        for layer in range(len(self.Layers)):
            zeroCount = 0
            for row in self.Layers[layer]:
                zeroCount += row.count(0)
            if zeroCount < leastZeroCount:
                leastZeroCount = zeroCount
                leastZeroLayer = layer
        print("The layer with the most zeros is", leastZeroLayer)
        return leastZeroLayer
    
    def CountInLayer(self, LayerNumber, NumberToCount):
        NumCount = 0
        Layer = self.Layers[LayerNumber]
        for row in Layer:
                NumCount += row.count(NumberToCount)
        return NumCount
    
        
    

                