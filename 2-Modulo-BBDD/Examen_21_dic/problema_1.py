#%%
def fizzbuzz(n):
    for num in range(1, n+1 ):
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
            
# ¿Qué complejidad tiene en tiempo y en espacio? → Orden n, n^2, etc. -> O(n) …

# En tiempo, tenemos que iterar los 100 números, por lo que es O(n).
# En espacio, no tenemos que guardar nada, por lo que es O(1).

# ¿Cuánto crees que podría tardar en procesar 1 millón de datos? → segundos, minutos, horas… 

import time
t1 = time.time()
fizzbuzz(100000)
t2 = time.time()
print("El programa ha tardado: ", t2 - t1, " segundos")

# Para un millón de datos el programa podría tardar unos segundos.

# El tiempo de ejecución está en el orden de magnitud de los segundos.          


               

        


# %%
def factorial(n):
    if n == 0:
        return 1 
    return n*factorial(n-1)


import time
t1 = time.time()
print(factorial(10000))
t2 = time.time()
print(t1- t2)

# %%
