import numpy as np
from sys import *


numbers = []
int = 2
status = 1

## Keep calculating powers of two to delay analysis
def sleeper():
    while status == 1:
        global int
        int = int ** 2
        print(f"{int}\n")
        # append to array 
        if int > 10e+8000000000:
            print("maths complete")
            global status
            status == 0
            break

if __name__ == '__main__'
sleeper()
