import math
import string
import random
#import  Choosing

#from Choosing import incscore
#from Choosing import getscore



def generate(comp):
    comp = int(comp)
    s = ''
    i = random.randint(2, 2 + int(comp))
    seq = ['+', '-', '*', '/']
    iter = 0
    while (iter < i):
        s += str(random.randint(1, 10 ** (1 + comp)));
        s += random.choice(seq)
        iter += 1

    s += str(random.randint(0, 10 ** (1 + comp)));
    print(s)
    return s
    a = eval(s);

def count(s, guess):
      a = eval(s);
      guess = int(guess)
      print(a)
      if(abs(guess - a) < 0.001):
          return True
          #incscore()
         # print('Correct! Your score now:', getscore())
      else:
          return False
          #print("Incorrect:(, Your score is still", getscore())
      #print(a)

