import math

print("Program to perform nCr calculation for combinations")
#Define selection pool
n = input("What is the number of possible selections?: ")
n = int(n)
#Define selection limit
r = input("How many can you choose?: ")
r = int(r)
#This method ignores repeats as it is assumed users will not repeat words
print("Calculating...")
#Print amount of possiblities
print (math.comb(n, r)) 
