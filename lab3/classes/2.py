class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length=l
        
    def area(self):
        return self.length*self.length
    
b=Square(0)
print(b.area())

a=int(input())
b=Square(a)
print(b.area())
    
            
    