# i cant be arsed to find my calculator lol

# j=1∑n 9 / ​10^j​ = 1 − 10^1​
# 9 / 10**j = 1 - 1 / 10**n

def first_sum():
    j = 1
    n = int(30)

# estimate limit
    ans =  1 - 1 / 10**n
    print(f"{ans}")


if __name__ == '__main__':
    first_sum()

#  lim   n               lim
#  n→∞   ∑  9 / 10^j   = n→∞ (1 - 1 / 10^n) = 1
#       j=1 

#             ∞ 
# 0.999 ... = ∑  9 / 10^j = 1
#            j=1 
