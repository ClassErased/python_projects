import numpy as np
from sys import *


numbers = []
int = 2
status = True

## Keep calculating powers of two to delay analysis
def sleeper():
    while status == True:
        
        int = int ** 2
        print(int)
        
        if int > 10e+20:
            print("maths complete")
            status = False

    
#
#def unused():
#    
#    for i in range (1,10):
#        
#        print("your mum gay")
#
#
#def __main__():
#    sleeper()

if __name__ == __main__:
    sleeper()
