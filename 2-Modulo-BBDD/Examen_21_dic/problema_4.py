#%%
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

import time
t1 = time.time()
print(factorial(1000))
t2 = time.time()
print(t1- t2)

