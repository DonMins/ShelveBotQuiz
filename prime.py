import math
import random



def inventing(comp):
    comp = int(comp)
    que = random.randint(3, 10 ** (comp + 1))
    if (que % 2 == 0):
        que += 1;
    return que
def isprime(que):
    limit = int(math.sqrt((que)))
    i = 3
    while (i <=  limit):
        if (que % i == 0):
            return 'False'
        i += 1
    return 'True'

def guessing(que):
         #from Choosing import incscore
         #from Choosing import getscore

         check = isprime(que)
         print('Is {} prime? True/False'.format(que))
         guess = input()
         if( check == str(guess) ):
             return True
             #incscore()
             #print('Correct! Your score now:', getscore())
         else:
             return False
             #print("Incorrect:(, Your score is still", getscore())
