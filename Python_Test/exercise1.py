import math

class Circle :
    def __inti__(self,radius) :
        self.radius = radius
    
    def area(self) :
        return math.pi*self.radius**2
    
    def perimeter(self) :
        return 2*math.pi*self.radius
    