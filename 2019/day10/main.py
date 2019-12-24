from Asteroid import Asteroid
from LaserStation import LaserStation
import numpy as np

def AsteroidLocations(path):
    """
    Reads in a text file. Makes an a new Asteroid object evreytime it finds a #
    symble and marks its x, y location. Returns a list of all the Asteroids it 
    found
    
    Input
    ----------
    path:   Path to the file we want to read in for our Asteroid
    """
    Asteroids = []
    x = 0
    y = 0
    # Read in the text file and get locations of the "#".
    file = open(path, 'r')
    text = file.read()
    file.close()
    text = text.split('\n')
    for line in text:
        for c in line:
            if c == '#':
                NewAsteroid = Asteroid(x, y)
                Asteroids.append(NewAsteroid)
            x += 1
        y += 1
        x = 0
    return Asteroids

def PrintAsteroids(Asteroids):
    """
    Prints out the x, y location for all the asteroids.
    
    Input
    ----------
    Asteroids: List containing Asteroid objects
    """
    for A in Asteroids:
        print("Asteroid at {}, {}.".format(A.x, A.y))
    return 0

def AngleBetween(aster1, aster2):
    """
    Finds the angle between 2 asteroids
    """
    x0, y0 = aster1.x, aster1.y
    x1, y1 = aster2.x, aster2.y
    dy = y1 - y0
    dx = x1 - x0
    # If I try to find the angle between itself then return -1.
    if dy == 0 and dx == 0:
        return -1
    
    angle = np.arctan2(dy, dx)
    return angle

def InView(refAsteroid, Asteroids):
    """
    Finds the numbers of asteroids that are inview of the input asteroid
    """
    # List of angles that are inview of the reference asteroid
    viewAngles = [-1]
    for A in Asteroids:
        angle = AngleBetween(refAsteroid, A)
        # Check if there's already an asteroid at that angle
        if angle not in viewAngles:
            viewAngles.append(angle)
    refAsteroid.inView = len(viewAngles)
    return viewAngles
        
def MostInView(Asteroids):
    """
    Finds the asteroid that can see the most asteroid
    """
    BestAst = Asteroid(-1, -1)
    for refA in Asteroids:
        InView(refA, Asteroids)
    for A in Asteroids:
        if A.inView > BestAst.inView:
            BestAst = A
    print("The asteroid with the best view is at, x = {} y = {}.\nIt can see {} asteroids.".format(BestAst.x, BestAst.y, BestAst.inView))
    return BestAst  

def AllTests():
    testFiles = ["test0.txt", "test1.txt", "test2.txt", "test3.txt", "test4.txt"]
    for test in testFiles:
        Asteroids = AsteroidLocations(test)
        MostInView(Asteroids)
        
    

def partOneMain():
    Asteroids = AsteroidLocations("input.txt")
    MostInView(Asteroids)
    

def partTwoMain():
    Asteroids = AsteroidLocations("input.txt")
    Laser = MostInView(Asteroids)
    Laser = LaserStation(Laser, Asteroids)
    Laser.SetAsteroidProps()
    while len(Laser.AsteroidsToShoot) > 0:
        Laser.ShootNext()
if __name__ == "__main__":
    partOneMain()
    partTwoMain()