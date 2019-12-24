import numpy as np

class Asteroid():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inView = 0
        self.distanceFromRef = 999999
        self.AngleFromRef = -1
    
    def SetAngleFromRef(self, refAsteroid):
        """
        Find the angle from this asteroid to some reference astroid.
        """
        dx = self.x - refAsteroid.x
        dy = refAsteroid.y - self.y
        angle = self.myArcTan(dx, dy)
        # I want all of my angles to be positive. 
    
        self.AngleFromRef = angle
        return 0
    
    def SetDistanceFromRef(self, refAsteroid):
        """
        Sets the distance to the reference asteroid so we know which once is 
        the closes when shooting them
        """
        dx = self.x - refAsteroid.x
        dy = self.y - refAsteroid.y
        dist = np.sqrt(dy**2 + dx**2)
        self.distanceFromRef = dist
        return 0
    
    def myArcTan(self, dx, dy):
        """
        For part two I want angles in reference to the +y axis and going CW. 
        """
        angle = np.arctan2(dy,dx)
        if angle >= 0 and angle <= np.pi/2:
            angle = np.pi/2 - angle
        elif angle > np.pi/2 and angle <= np.pi:
            angle = 2*np.pi - (angle - np.pi/2)
        elif angle < 0 and angle >= -np.pi:
            angle = abs(angle) + np.pi/2
        else:
            print("Error with myArcTan", angle)
        return angle
        
            
            
        