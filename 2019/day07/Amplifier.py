from IntcodeComputerV4 import IntcodeComputer

class Amplifier:
    def __init__(self, name,  phase, code):
        self.name
        self.phase = phase
        self.code = code
        self.instructionPoint = 0
    
    def AmplfifierOutputSoftware(self, INPUT):
        ampOutput, self.code, self.instructionPoint = IntcodeComputer(self.code,
                                                                      [self.phase, INPUT],
                                                                      INDEX)
    