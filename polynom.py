import math
import random


class Polynom:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.z = c


pol = Polynom(1, 1, 1)
def creating(diff):
    z = random.randint(1, 10**int(diff))
    pol.z = z
    a = random.randint(1, 10 ** int(diff))
    pol.a = a
    b = random.randint(1, 10 ** int(diff))
    pol.b = b
    if(z == 1):
        s = 'x^2'
    else:
        s = str(z) + 'x^2'
    if(z*(a+b) < 0):
        s += ("+" + str(abs(z*(a+b))) + 'x')
    else:
        s += ('-' + str(z*(a+b)) + 'x')
    if(a*b*z < 0):
        s += str(a*b*z)
    else:
        s += ('+' + str(a * b * z))

    return s

def mult(task):
    return pol.a * pol.b


