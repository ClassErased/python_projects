import psutils as ps

global memcheck
memcheck = []
status = True

memcheck = psutil.virtual_memory()
#If the computers memory is less than 2GB warn of low mem
if memcheck[0] > 2.1490e+9:
    print("Low memory system, could be analysis!")
