# Several installation methods
# a) conda install numba
# b) conda update numba
# c) pip install numba
import array 
import random 
from numba import jit
import timeit


interval = 10000000
# bigger interval bigger the time difference between numba and the normal version

a = array.array('l', [random.randint(0,10) for x in range (0,interval)]) 

def normal_sum(x): 
    total = 0 
    for items in x: 
      total+=items 
    return total 


@jit(nopython=True, parallel=False) 
def numba_sum(x): 
    total = 0 
    for items in x: 
      total+=items 
    return total  
starttime = timeit.default_timer()
normal_sum(a) 
print("Normal - The time difference is :", timeit.default_timer() - starttime)


starttime = timeit.default_timer()
numba_sum(a)
print("NUMBA - The time difference is :", timeit.default_timer() - starttime) 

