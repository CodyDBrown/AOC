from Asteroid import Asteroid
import numpy as np

class LaserStation(Asteroid):
    def __init__(self, refAsteroid, Asteroids):
        self.NumberShot = 0
        self.refAsteroid = refAsteroid
        self.LastAngleShot = -1
        self.AsteroidsToShoot = Asteroids
        
    def SetAsteroidProps(self):
        """
        Find the distance and angle from the reference asteroid to all the others
        """
        for A in self.AsteroidsToShoot:
            A.SetAngleFromRef(self.refAsteroid)   
            A.SetDistanceFromRef(self.refAsteroid)
            # Check if the laster station asteroid is in the list of asteroids 
            # and if it is remove it now
            if A.SetDistanceFromRef == 0:
                self.AsteroidsToShoot.remove(A)

    def FindCW(self):
        AsteroidsCW = []
        for A in self.AsteroidsToShoot:
            if A.AngleFromRef > self.LastAngleShot:
                AsteroidsCW.append(A)
        return AsteroidsCW
    
    def ShootNext(self):
        """
        Finds the next asteroid to shoot, and removes it from the list. The 
        shooting angle will start at -1 to make sure we start at angle 0. 
        """
        # Make a list of all the Asteroids CCW to the Laser
        AsteroidsCW = self.FindCW()
        # Check if we have any. We might have wrapped around
        if len(AsteroidsCW) == 0:
            self.LastAngleShot = -1
            AsteroidsCW = self.FindCW()
        # Find the next closest in angle.
        nextAngle = 2*np.pi
        for A in AsteroidsCW:
            if A.AngleFromRef < nextAngle:
                nextAngle = A.AngleFromRef
        # Reduce the AsteroidsCW list to only those at that angle.
        AsteroidsCW = [A for A in AsteroidsCW if A.AngleFromRef == nextAngle]
        # Out of those I need to find the closest in distance
        closestAsteroid = Asteroid(0,0)
        for A in AsteroidsCW:
            if A.distanceFromRef < closestAsteroid.distanceFromRef:
                closestAsteroid = A
        
        self.AsteroidsToShoot.remove(A)
        self.LastAngleShot = nextAngle
        self.NumberShot += 1
        if self.NumberShot == 200:
            self.partTwoAnswer(A)
            return 0
        
    def partTwoAnswer(self, asteroid):
        if self.NumberShot == 200:
            print("The 200th asteroid shot is at x = {}, y = {}.".format(asteroid.x, asteroid.y))
            print("The answer to part two is: ",asteroid.x*100 + asteroid.y)
            
    def PrintAngles(self):
        for A in self.AsteroidsToShoot:
            print(A.AngleFromRef)
        
        