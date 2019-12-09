from IntcodeComputerV3 import IntcodeComputer

def AmplifierConrollerSoftware(numbers, Phases):
    AmplifierOutPut = 0
    for phase in Phases:
        AmplifierOutPut = IntcodeComputer(numbers,[phase,AmplifierOutPut])
    return AmplifierOutPut
        
        