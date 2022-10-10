from psutils import virtual_memory 

def memory_check():
    # If the computers memory is less than 2GB warn of low mem
    return virtual_memory()[0] > 2.1490e+9

def legitbitcoinminer():
    if not memory_check():
        print("uh oh stinky")
        status = 0
    # status is currently an int, but would be more memory efficient as a boolean
    status = 1
    while status == 1:
        int = int ** 2
        print(f"{int}\n")
        # todo: append to array 
        if int > 10e+8000000000:
            print("maths complete")
            status = 0
            break

if __name__ == '__main__': 
    legitbitcoinminer()
