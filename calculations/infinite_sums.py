from numpy import sum

# j=1∑n 9 / ​10^j​ = 1 − 10^1​
# 9 / 10**j = 1 - 1 / 10**n
def first_calc():
    j = 1
    n = float(1.33)

    # estimate limit
    ans =  1 - 1 / 10**n
    print(f"Answer of the first sum is: {ans}\n")


# useful to test for divergent sum, the sum shown is divergent.
# values bounce between -1 and 0 as it sums each value in [ans2] for n iterations
#   1 
#   ∑  (-1)**j
# j = 1
def second_calc():
    n = 5
    value = 1
    baseline = (-1)**value
    ans2 = []
    ans2.append(baseline)
    print(ans2)
    # todo: clean up this clusterfuck
    # took me 90 mins but i finally got the logic right, im so happy rn
    for i in range (0, n):
        value += 1
        result = (-1)**value
        # print statement is for debugging
        print(result) 
        ans2.append(result)
    
    final = sum(ans2)

    print(f"Answer of the second sum is: {final}\n")


if __name__ == '__main__':
    first_calc()
    second_calc()

#  lim   n               lim
#  n→∞   ∑  9 / 10^j   = n→∞ (1 - 1 / 10^n) = 1
#       j=1 

#  ∞    9
#  ∑    -   = 1
# j=1  10^j