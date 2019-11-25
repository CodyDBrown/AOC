import pandas

def readInput(filePath):
    table = pandas.read_csv(filePath, delimiter="\t", header=None)
    return table

def partOneMain():
    answer =0
    inpt = readInput("input.txt")
    for row in range(len(inpt)):
        answer += (max(inpt.loc[row]) - min(inpt.loc[row]))
        
    print("Answer for part one: ", answer)
        
    return 0

def sortRows(dataFrame):
    numbers = dataFrame.values
    numbers.sort(axis = 1) # no ascendiing argument
    
    numbers = numbers[:, ::-1]
    return pandas.DataFrame(numbers)

def checkRow(df, row):
    for refNum in range(df.loc[row].size):
        for checkNum in range(refNum + 1, df.loc[row].size):
            if(df.loc[row][refNum] % df.loc[row][checkNum] == 0):
                return df.loc[row][refNum] / df.loc[row][checkNum]

def partTwoMain():
    answer = 0
    inpt = readInput("input.txt")
    sortedInput = sortRows(inpt)
    # With it being sorted I can iterate through the numbers in order
    for row in range(len(sortedInput)):
        answer += checkRow(sortedInput, row)
    print("Answer for part two: ", answer)

if __name__ == "__main__":
    partOneMain()
    partTwoMain()
