import math
from Shapes import Circle


class Cuboid():
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
    def getSurfaceArea(self):
        return 2(self.depth * self.width + self.width * self.height + self.length * self.height)
    def getVolume(self):
        return (self.width * self.height * self.depth)
    
    
class Cube():
    def __init__(self, width, height, depth):
        self.width = width 
        self.height = height
        self.depth = depth
    def getSurfaceArea(self):
        return ((self.width * self.height) * 6)
    def getVolume(self):
        return ((self.width * self.height * self.depth))
    

class Cylinder():
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def getSurfaceArea(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2))
    def getVolume(self):
        return (math.pi * (self.radius ** 2) * self.height)


class Prism():
    def __init__(self, sideLength, faces, height):
        self.sideLength = sideLength
        self.height = height
        self.faces = faces
    def getVolume(self):
        return (1/2 * self.sideLength) * (1/2 * self.sideLength * math.sqrt(3)) * self.faces * self.height
    def getSurfaceArea(self):
        (1/2 * self.sideLength) * (1/2 * self.sideLength * math.sqrt(3)) * self.faces * 2 + ((self.sideLength * self.height) * self.faces)