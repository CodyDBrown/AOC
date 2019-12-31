from Moon import Moon
import math

def fileToList(path):
    """
    Opens the file and reads in the numbers. Talor made to work for day 12
    Input
    ----------
    path:   String of the path to the text file that has the puzzle input.
    """
    file = open(path, 'r')
    text = file.read()
    file.close()
    text = text.split('\n')
    moonList = []
    for n in text:   
        n = n.split(',')
        moonList.append(n)
    coordinates = []
    for moon in moonList:
        corFoo = []
        for el in moon:
            for c in ['<','x','=','y','z','>', ' ']:
                el = el.replace(c,'')
            corFoo.append(int(el))
        coordinates.append(corFoo)
    return coordinates


def Gravity(Moons):
    """
    Updates the velocity of the moon objects. 
    """
    velocities = []
    # First change the velocities
    for moon in Moons:
        vx, vy, vz = 0, 0, 0
        for omoon in Moons:
            if (moon.x - omoon.x) > 0:
                vx += -1
            elif (moon.x - omoon.x) < 0:
                vx += 1
            
            if (moon.y - omoon.y) > 0:
                vy += -1
            elif (moon.y - omoon.y) < 0:
                vy += 1
            
            if (moon.z - omoon.z) > 0:
                vz += -1
            elif (moon.z - omoon.z) < 0:
                vz += 1
        velocities.append([vx,vy,vz])
    # Now that I have a list of velocities to update. Update them
    for m in range(len(Moons)):
        Moons[m].vx += velocities[m][0]
        Moons[m].vy += velocities[m][1]
        Moons[m].vz += velocities[m][2]
        
    return Moons

def Velocity(Moons):
    """
    Updates the velocity of the moons
    Input
    ----------
    Moons: List of Moon objects
    """
    for moon in Moons:
        moon.x += moon.vx
        moon.y += moon.vy
        moon.z += moon.vz
    return Moons
    
def FindTotalEnergy(Moons):
    NRG = 0
    for moon in Moons:
        moon.SetPotential()
        moon.SetKinetic()
        NRG += (moon.Potential * moon.Kinetic)
    return NRG

def SetAllKeys(Moons):
    for moon in Moons:
        moon.SetKey()
    return Moons

def partOne():
    numbers = fileToList("input.txt")
    # Make my 4 moon objects
    Moons = []
    TIME = 0
    for coor in numbers:
        Moons.append(Moon(coor[0], coor[1], coor[2]))
    while TIME < 1000:
        Moons = Gravity(Moons)
        Moons = Velocity(Moons)
        TIME += 1
        
    TotalEnergy = FindTotalEnergy(Moons)
    
    print("The total energy after {} steps is: {}".format(TIME, TotalEnergy))

def partTwo():
    
    def _lcm(a, b):

        return a * b // math.gcd(a, b)
    
    numbers = fileToList("input.txt")
    # Make my 4 moon objects
    Moons = []
    # Make a dictionary for the moon times
    # Period of all the moons
    XPeriod = 0
    YPeriod = 0
    ZPeriod = 0
    TIME = 1
    for coor in numbers:
        Moons.append(Moon(coor[0], coor[1], coor[2]))
    Moons = SetAllKeys(Moons)
    print("IO starting")
    Moons[0].PrintValues()
    StartingX = [Moons[0].x, Moons[1].x, Moons[2].x, Moons[3].x]
    StartingY = [Moons[0].y, Moons[1].y, Moons[2].y, Moons[3].y]
    StartingZ = [Moons[0].z, Moons[1].z, Moons[2].z, Moons[3].z]
    while True:
        Moons = Gravity(Moons)
        Moons = Velocity(Moons)
        TIME += 1
        if [Moons[0].x, Moons[1].x, Moons[2].x, Moons[3].x] == StartingX and XPeriod == 0:
            XPeriod = TIME
            print(XPeriod)
        if [Moons[0].y, Moons[1].y, Moons[2].y, Moons[3].y] == StartingY and YPeriod == 0:
            YPeriod = TIME    
            print(YPeriod)
        if [Moons[0].z, Moons[1].z, Moons[2].z, Moons[3].z] == StartingZ and ZPeriod == 0:
            ZPeriod = TIME
            print(ZPeriod)
            
        if XPeriod > 0 and YPeriod > 0 and ZPeriod > 0:
            answer = _lcm(_lcm(XPeriod, YPeriod), ZPeriod)
            print("Answer to part two is: ", answer)
            return 0
            
            
            
        

if __name__ == "__main__":
    partOne()
    partTwo()