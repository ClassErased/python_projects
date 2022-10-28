from numpy import sum

# j=1∑n 9 / ​10^j​ = 1 − 10^1​
# 9 / 10**j = 1 - 1 / 10**n
def first_calc():
    j = 1
    n = float(1.33)

    # lim
    ans =  1 - 1 / 10**n
    print(f"Answer of the first sum is: {ans}\n")


# useful to test for divergent sum, the sum shown is divergent.
# values bounce between -1 and 0 as it sums each value in [ans2] for n iterations
#   1 
#   ∑  (-1)**j
# j = 1
def second_calc(n: int , answer: list = []) -> list:
    value=1
    answer.append((-1)**value)
    
    for i in range (0, n):
        value += 1
        result = (-1)**value 
        answer.append(result)
    
    print(f"Answer of the second sum is: {sum(answer)}\n",answer,"\n")

if __name__ == '__main__':
    first_calc()
    #  lim   n               lim
    #  n→∞   ∑  9 / 10^j   = n→∞ (1 - 1 / 10^n) = 1
    #       j=1 

    #  ∞    9
    #  ∑    -   = 1
    # j=1  10^j
    second_calc(9)