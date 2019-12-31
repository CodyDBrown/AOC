class Moon():
    def __init__(self, x, y, z):
        # Initial positions
        self.x = x
        self.y = y
        self.z = z
        # Velocity always starts at zero
        self.vx = 0
        self.vy = 0
        self.vz = 0
        # Energy values for the moon
        self.Potential = 0
        self.Kinetic = 0
        # Want a key for part 2
        self.key = ''
    def PrintValues(self):
        print("x: {} y: {} z: {}    vx: {} vy: {} vz: {}".format(self.x, self.y, self.z,
              self.vx, self.vy, self.vz))
        return 0
    
    def SetPotential(self):
        self.Potential = abs(self.x) + abs(self.y) + abs(self.z)
        return 0
    
    def SetKinetic(self):
        self.Kinetic = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return 0
    
    def SetKey(self):
        self.key = str(self.x) + str(self.y) + str(self.z) + str(self.vx) + str(self.vy) + str(self.vz)
    
        