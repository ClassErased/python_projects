import math
import time
import sys


def nCr():
    print("\nProgram to perform nCr calculation for combinations")
    #User inputs the n and r variables which must be an integer
    n = int(input("What is the number of possible selections?: "))
    r = int(input("How many can you choose?: "))
    #Performs nCr calculation and prints the result, asks user what to do next.
    print (math.comb(n, r)) 
    choice2 = input("Would you like to perform another calculation? [Y/N]: ")

print("Aarons maths swiss army knife \n")
print ("[1] nCr program \n[2] Subnet calculator \n")
choice = int(input("Select a program from the list above: "))
while choice == 1:
    {nCr}
    

while choice == 2:
    print("Subnet calulator under construction, exiting program\n")