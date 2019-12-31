def ReadInNumbers(filePath):
    inputFile = open(filePath, 'r')
    numbers = inputFile.read()
    inputFile.close()
    # numbers is currently a string so we need 
    # to turn it into a list of numbers
    numbers = numbers.split()
    numbersInt = [int(n) for n in numbers]
    return numbersInt

def CalculateFuel(mass):
    # using // to retrun an int
    return mass//3 - 2

def FuelForFuel(fuel):
    fuelForFuel = fuel
    TotalExtraFuel = 0
    while(fuelForFuel > 0):
        fuelForFuel = CalculateFuel(fuelForFuel)
        if(fuelForFuel > 0):
            TotalExtraFuel += fuelForFuel
    return TotalExtraFuel
            

def partOneMain():
    answer = 0
    # Read in the numbers from the input file
    numbers = ReadInNumbers("input.txt")
    for number in numbers:
        answer += CalculateFuel(number)
    print("Answer to part one is:", answer)
    return 0
    
def partTwoMain():
    answer = 0
    numbers = ReadInNumbers("input.txt")
    for number in numbers:
        FuelForMod = CalculateFuel(number)
        extraFuel = FuelForFuel(FuelForMod)
        answer += FuelForMod + extraFuel        
    print("Answer to part two is:", answer)
    return 0
        

if __name__ == "__main__":
    partOneMain()
    partTwoMain()
