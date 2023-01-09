#%%
def main(n):
    for num in range(1,n +1):
        mult_3 = num % 3 == 0
        mult_5 = num % 5 == 0
        if mult_3 and mult_5:
            print("fizzbuzz")
        elif mult_5:
            print("buzz")
        elif mult_3:
            print("fizz")
        else:
            print(num)

import time
t1 = time.time()
main(1000)
t2 = time.time()
print(t1 - t2)
# %%
