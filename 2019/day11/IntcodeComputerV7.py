"""
V7 will have automated inputs and take will use the ourput before halting. So it
will be more in line with the V3/4 IntcodeComputer. 
"""

def IntcodeComputer(numbers, INPUT, INDEX = 0, REL_BASE = 0):  
    def modeCheck(m, offset):
        # Position Mode
        if m == '0':
            return numbers[numbers[INDEX+offset]]
        # Immediate Mode
        elif m == '1':
            return numbers[INDEX + offset]
        # Relative mode
        elif m == '2':
            return numbers[numbers[INDEX + offset] + REL_BASE] 
        
    while(True):
        comand, modes = getOperation(numbers[INDEX])
        if comand == 1:
            firstNumber = modeCheck(modes[-1], 1)
            secondNumber = modeCheck(modes[-2], 2)
            if modes[-3] == '0':
                outPut = numbers[INDEX + 3]
                numbers[outPut] = firstNumber + secondNumber
            elif modes[-3] == '1':
                numbers[INDEX + 3] = firstNumber + secondNumber
            elif modes[-3] == '2':
                outPut = numbers[INDEX + 3] + REL_BASE
                numbers[outPut] = firstNumber + secondNumber
                
            INDEX += 4
            
        elif comand == 2:
            firstNumber = modeCheck(modes[-1], 1)
            secondNumber = modeCheck(modes[-2], 2)
            if modes[-3] == '0':
                outPut = numbers[INDEX + 3]
                numbers[outPut] = firstNumber * secondNumber
            elif modes[-3] == '1':
                numbers[INDEX + 3] = firstNumber * secondNumber
            elif modes[-3] == '2':
                outPut = numbers[INDEX + 3] + REL_BASE
                numbers[outPut] = firstNumber * secondNumber
            INDEX += 4
            
        # Input command
        elif comand == 3:
            if modes[-1] == '0':
                location = numbers[INDEX+1]
            elif modes[-1] == '1':
                location = INDEX + 1
            elif modes[-1] == '2':
                location = numbers[INDEX + 1] + REL_BASE
            numbers[location] = int(INPUT)
            INDEX += 2

        # Output command                
        elif comand == 4:
            if modes[-1] == '0':     
                OUTPUT = numbers[numbers[INDEX + 1]]
                #print(OUTPUT)
            elif modes[-1] == '1':
                OUTPUT = numbers[INDEX+1]
                #print(OUTPUT)
            elif modes[-1] == '2':
                OUTPUT = numbers[numbers[INDEX + 1]+ REL_BASE]
                #print(OUTPUT)
            INDEX += 2
            return numbers, OUTPUT, INDEX, REL_BASE
            
        elif comand == 5:
            firstParam = modeCheck(modes[-1], 1)
            secondParam = modeCheck(modes[-2], 2)
            if firstParam != 0:
                INDEX = secondParam
            else:
                INDEX += 3
        
        elif comand == 6:
            firstParam = modeCheck(modes[-1], 1)
            secondParam = modeCheck(modes[-2], 2)
            if firstParam == 0:
                INDEX = secondParam
            else:
                INDEX += 3
                
        elif comand == 7:
            firstParam = modeCheck(modes[-1],1 )
            secondParam = modeCheck(modes[-2], 2)
            outputMode = modes[-3]
            if outputMode == '0':
                outputLoc = numbers[INDEX + 3]
            elif outputMode == '1':
                outputLoc = INDEX + 3
            elif outputMode == '2':
                outputLoc = numbers[INDEX + 3] + REL_BASE
            else:
                print("Output mode error for operation 7")
                return 0
            if firstParam < secondParam:
                numbers[outputLoc] = 1
            else:
                numbers[outputLoc] = 0
            INDEX += 4
            
        elif comand == 8:
            firstParam = modeCheck(modes[-1],1 )
            secondParam = modeCheck(modes[-2], 2)
            outputMode = modes[-3]
            if outputMode == '0':
                outputLoc = numbers[INDEX + 3]
            elif outputMode == '1':
                outputLoc = INDEX + 3
            elif outputMode == '2':
                outputLoc = numbers[INDEX + 3] + REL_BASE
            else:
                print("Output mode error for operation 8")
                return 0
            if firstParam == secondParam:
                numbers[outputLoc] = 1
            else:
                numbers[outputLoc] = 0
            INDEX += 4
        
        # Change REL_BASE
        elif comand == 9:
            firstParam = modeCheck(modes[-1], 1)
            REL_BASE += firstParam
            INDEX += 2
            
        elif comand == 99:
            # Program ends
            return numbers, None, INDEX, REL_BASE
        else:
            print("ERROR", numbers[INDEX])
            return None
    
    
        
def getOperation(operation):
    operation = str(operation)
    if len(operation) < 5:
        operation = '0'*(5 - len(operation)) + operation
    comand = operation[-2:]
    modes = operation[:-2]
    return int(comand), modes
        
    

        


