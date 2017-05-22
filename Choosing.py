import random
#import quiz
#import  prime





def choose():
    score = 0
    from quiz import count
    from prime import guessing
    exitflag = ''
    print('Welcome to the victorina. Choose the difficulty from 1 to 3')
    diff = input()
    bool = False
    while (exitflag != 'N'):
         if((diff.isdigit()) & (int(diff) > 0) & (int(diff) < 4)):
             mode  = random.randint(0, 10)
             if(mode % 2 == 0):
                 bool = guessing(int(diff))
             else:
                 bool = count(int(diff))
         else:
             print('Wrong input :(')

         if(bool == True):
                score += 1
                print('Correct! Your score now:', score)
         else:
            print("Incorrect:(, Your score has burnt to 0")
            score = 0

         print("Wanna try again? Y / N")
         exitflag = input()


choose()