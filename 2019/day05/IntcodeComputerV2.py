def IntcodeComputer(numbers):
    INDEX = 0
    def modeCheck(m, offset):
        if m == '0':
            return numbers[numbers[INDEX+offset]]
        else:
            return numbers[INDEX + offset]
        
    while(True):
        
        comand, modes = getOperation(numbers[INDEX])
        print(comand, INDEX, modes)
        if comand == 1:
            firstNumber = modeCheck(modes[-1], 1)
            secondNumber = modeCheck(modes[-2], 2)
            if modes[-3] == '0':
                outPut = numbers[INDEX + 3]
                numbers[outPut] = firstNumber + secondNumber

            else:
                numbers[INDEX + 3] = firstNumber + secondNumber

            INDEX += 4
            
        elif comand == 2:
            firstNumber = modeCheck(modes[-1], 1)
            secondNumber = modeCheck(modes[-2], 2)
            if modes[-3] == '0':
                outPut = numbers[INDEX + 3]
                numbers[outPut] = firstNumber * secondNumber
            else:
                numbers[INDEX + 3] = firstNumber * secondNumber

            INDEX += 4
        
        elif comand == 3:
            INPUT = input("Ener your input: ")
            # We're in position mode
            location = int(numbers[INDEX+1])
            numbers[location] = int(INPUT)
            INDEX += 2
                
        elif comand == 4:
            if modes[-1] == '0':
                
                OUTPUT = numbers[numbers[INDEX + 1]]
                print("Position mode, output: ", OUTPUT)
            else:
                OUTPUT = numbers[INDEX+1]
                print("Immediate Mode Program output", OUTPUT)
            INDEX += 2
            
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
            if firstParam < secondParam:
                numbers[numbers[INDEX +3]] = 1
            else:
                numbers[numbers[INDEX + 3]] = 0
            INDEX += 4
            
        elif comand == 8:
            firstParam = modeCheck(modes[-1],1 )
            secondParam = modeCheck(modes[-2], 2)
            if firstParam == secondParam:
                numbers[numbers[INDEX +3]] = 1
            else:
                numbers[numbers[INDEX + 3]] = 0
            INDEX += 4
            
        
        elif comand == 99:
            # Program ends
            return 0
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
        
    

        


