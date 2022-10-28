from numpy import sum

# j=1∑n 9 / ​10^j​ = 1 − 10^1​
# 9 / 10**j = 1 - 1 / 10**n
def first_calc(n: float, j = 1):
    # lim
    answer =  j - j / 10**n
    print(f"Answer of the first sum is: {answer}\n")

# useful to test for divergent sum, the sum shown is divergent.
# values bounce between -1 and 0 as it sums each value in [ans2] for n iterations
#   1 
#   ∑  (-1)**j
# j = 1
def second_calc(n: int , answer: list = [(-1),], j = 1) -> list:
    #answer.append((-1)**j)
    for i in range (0, n):
        j += 1
        result = (-1)**j 
        answer.append(result)
    
    print(f"Answer of the second sum is: {sum(answer)}\n",answer,"\n")

if __name__ == '__main__':
    first_calc(1.33)
    #  lim   n               lim
    #  n→∞   ∑  9 / 10^j   = n→∞ (1 - 1 / 10^n) = 1
    #       j=1 

    #  ∞    9
    #  ∑    -   = 1
    # j=1  10^j
    second_calc(10)