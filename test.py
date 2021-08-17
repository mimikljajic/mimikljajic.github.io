import math

class Triangle():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def perimeter(self):
        return self.a+self.b+self.c

    def area(self):
        s=(self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
    def scale(self, scale_factor):
        return Triangle(scale_factor * self.a, scale_factor * self.b, scale_factor*self.c)

    def is_right(self):
        if (self.a**2 + self.b**2) == self.c**2 or (self.a**2 + self.c**2) == self.b**2 or (self.c**2 + self.b**2) == self.a**2:
            return True
        else:
            return False

    def is_valid(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return False

t = Triangle(3,4,5)

print ("Perimeter = %d" % t.perimeter())
print ("Area = %d" % t.area())
if t.is_right():
    print ("Triangle is right.")
else:
    print ("Triangle is not right.")

if t.is_valid():
    print ("Triangle is valid.")
else:
    print ("Triangle is not valid.")


q = t.scale(2)
print(q.a, q.b, q.c)

