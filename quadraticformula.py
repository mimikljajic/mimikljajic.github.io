import math

def solve_quadratic(a , b , c):
    d = b * b - 4 * a * c
    if d > 0:
        x1 = ((-b + math.sqrt(d))) / (2 * a)
        x2 = ((-b - math.sqrt(d))) / (2 * a)
        return ("(" + str(x1) + "," + str(x2) + ")") 
    elif d == 0:
        x = (-b / (2 * a))
        return x
    else :
        return("")
