import random
import math

class rad:
    def __init__(self, rad):
        self.rad = rad
        self.figure = 1
    def getrad(self):
        return self.rad
    def setrad(self, rad):
        self.rad = rad


radius = rad(1)
def deciding(diff):
    task = random.randint(0, 2)
    if( task == 0):
        radius.figure = 0
        var = random.randint(1, 10)
        radius.setrad(var)
        s = 'Whats the volume of the sphere witch such radius = ' + str(var)
        return s
    if (task == 1):
        radius.figure = 1
        var = random.randint(1, 20)
        radius.setrad(var)
        s = 'Whats the square of the sphere witch such radius = ' + str(var)
        return s
    if (task == 2):
        radius.figure = 2
        var = random.randint(1, 20)
        radius.setrad(var)
        s = 'Whats the square of the circle witch such radius = ' + str(var)
        return s

def voluming(s):
    if(radius.figure == 0):
        return "{0:.2f}".format(4/3 * math.pi * radius.getrad()**3)

    if (radius.figure == 1):
        return "{0:.2f}".format(4  * math.pi * radius.getrad() ** 2)

    if (radius.figure == 2):
        return  "{0:.2f}".format(math.pi * radius.getrad() ** 2)