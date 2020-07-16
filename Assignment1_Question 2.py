#Question 2
#Class programming
class Point:
    pointX = 0
    pointY = 0
    
    
    def __init__(self, X, Y):
        self.pointX = X
        self.pointY = Y
        
    def getX(self):
        return self.pointX
    
    def getY(self):
        return self.pointY



class Rectangle:
    def __init__(self, topLeft, topRight, bottomLeft, bottomRight):
        self.TL = topLeft
        self.TR = topRight
        self.BL = bottomLeft
        self.BR = bottomRight
    def perim(self):
        return (2 * (self.TL + self.TR)) + (2 * (self.BL + self.BR))
    
    def area(self):
        return (self.TL + self.TR) * (self.BL + self.BR)
    
    def __str__(self):
        return  (self.TL, self.TR, self.BL, self.BR)

rec = Rectangle (6, 6, 24, 24)
print ("Area of rectangle: %s" % rec.area())
print ("Perimeter of rectangle: %s" % rec.perim())




