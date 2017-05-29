import math
import string
import random
#import  Choosing

#from Choosing import incscore
#from Choosing import getscore

from shelvetry import setans

def generate(id, comp):
    comp = int(comp)
    s = ''
    i = random.randint(2, 2 + int(comp))
    seq = ['+', '-', '*', '/']
    iter = 0
    while (iter < i):
        s += str(random.randint(1, 10 ** (1 + comp)));
        s += random.choice(seq)
        iter += 1

    s += str(random.randint(1, 10 ** (1 + comp)));
    count(id, s)
    return s

def count(id, s):
      a = eval(s);
      setans(id, 0, "{0:.2f}".format(a))
      return
      #guess = int(guess)
      #if(abs(guess - a) < 0.01):
          #return True
          #incscore()
         # print('Correct! Your score now:', getscore())
      #else:
          #return False
          #print("Incorrect:(, Your score is still", getscore())
      #print(a)

