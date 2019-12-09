from IntcodeComputerV4 import IntcodeComputer

def AmplifierConrollerSoftwareV2(numbers, Phases):
    AmplifierOutPut = 0
    KEEPGOING = True
    while KEEPGOING:
        for phase in Phases:
            # print("Using phase", phase)
            AmplifierOutPut, KEEPGOING = IntcodeComputer(numbers,[phase,AmplifierOutPut])
            print("Amplifier with phase {}, has output {}.".format(phase, AmplifierOutPut))
            if AmplifierOutPut > 139629729:
                KEEPGOING = False
    return AmplifierOutPut
        
        