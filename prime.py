import math
import random

from shelvetry import setans

def inventing(id, comp):
    comp = int(comp)
    que = random.randint(3, 10 ** (comp + 1))
    if (que % 2 == 0):
        que += 1;
    isprime(que, id)
    return que



def isprime(que, id):
    limit = int(math.sqrt((que)))
    i = 3
    while (i <=  limit):
        if (que % i == 0):
            setans(id, 1, 'False')
            return
        i += 1
    setans(id, 1, 'True')
    return

