class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return f"Point({self.x}, {self.y})"

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def dist(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx**2 + dy**2)**0.5


a = int(input())
b = int(input())
a1 = int(input())
b1 = int(input())
p1 = Point(a,b)
p2 = Point(a1,b1)
print(p1.show())
m1 = int(input())
m2 = int(input())
p1.move(m1,m2)
print(p1.dist(p2))
