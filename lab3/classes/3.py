class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width
d = int(input())
e = int(input())
r = Rectangle(d,e)
print(r.area())
