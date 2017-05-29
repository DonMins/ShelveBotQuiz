import math
import random

from shelvetry import setans

def creating(id, diff):
    z = random.randint(1, 10**int(diff))
    a = random.randint(1, 10 ** int(diff))
    b = random.randint(1, 10 ** int(diff))
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
    mult(a, b, id)
    return s

def mult(a, b, id):
    setans(id, 2, (a*b))
    #return pol.a * pol.b


