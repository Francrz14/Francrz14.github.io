## página https://pynative.com/python-basic-exercise-for-beginners/ 
#%% Ejercicio 1

def fun(num1, num2):
    prod = num1 * num2 
    if prod < 1000:
        return prod
    else:
        return num1 + num2 

res = fun(20, 30)
print("el resultado es", res)
res = fun(40, 30)
print("el resultado es", res)

#%% ejercicio 2
num_anterior = 0

for i in range(1,10):
    suma_10 = num_anterior +i
    print("Número corriente", i," Numero anterior", num_anterior, "Suma:", suma_10)

    num_anterior = i

#%% ejercicio 3
def obtener_string(string):
    idx = 0
    new_str = ""
    while idx < len(string):
        if idx % 2 == 0:
            char = string[idx]
            new_str += char
        idx += 1
    return new_str

my_str = "HolaQueTal."
my_str2 = "pynative"
my_str3 ="unstringmuchomaslargoparaprueba"
print(obtener_string(my_str))
print(obtener_string(my_str2))
print(obtener_string(my_str3))

#%% ejercicio 4
def quitar_cadenas(cad, n):
    i = cad[n:]
    return i

print(quitar_cadenas("pynative", 4))
print(quitar_cadenas("pynative", 2))



# %% ejercicio 5
def primer_ultimo(numeroLista):
    print("divisible por 5:",numeroLista)
    primer_num = numeroLista[0]
    second_num = numeroLista[-1]
    if primer_num == second_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("el resultado es",primer_ultimo(numbers_x))
numbers_y = [75, 65, 35, 75, 30]
print("el resultado es", primer_ultimo(numbers_y))

# %% ejercicio 6

list_div_5 = [10, 20, 33, 46, 55]
for num in list_div_5:
    if num % 5 == 0:
        print(num)

# %% ejercicio 7

str_x = "Emma is good developer. Emma is a writer"
encontrar = str_x.count("Emma")
print(encontrar)

# %% ejercicio 8
for num in range(1, 6):
    for i in range(num):
        print(num, end=" ") 

    print("\n")
# %% ejercico 9

def palindromo(numero):
    numero_orig = numero

    revertido = 0
    while numero > 0:
        recordatorio = numero % 10
        revertido = (revertido * 10) + recordatorio
        numero = numero // 10

    if numero_orig == revertido:
        print("este número es palíndromo")
    else:
        print("este número no es palíndromo")

palindromo(121)
palindromo(125)
palindromo(1221)

# %% ejercico 10

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

def list_par_impar(list1, list2):
    res_lista = []
    for num in list1:
        if num % 2 != 0:
            res_lista.append(num)

    for num in list2:
        if num % 2 == 0:
            res_lista.append(num)
    return res_lista     

print("resultados en la lista", list_par_impar(list1 , list2))   

# %% ejercico 11

numero = 7536
while numero > 0:
    digito = numero % 10
    numero = numero // 10
    print(digito, end=" ")

# %% ejercico 12

dinero = 45000

if dinero < 10000:
    taxas = 0 
elif dinero < 20000:
    d = dinero -10000
    tax = d * 10 / 100
else:
    taxas = 0
    taxas = 10000 * 10 / 100
    taxas += (dinero - 20000) * 20 / 100 
print("La taxa total a pagar es", taxas)   

# %% ejercico 13

for i in range(1, 11):
    for a in range(1, 11):
        print(i * a, end = " ")
    print("\t\t")    


# %% ejercico 14

for i in range(9, 0, -1):
    for a in range(0, i - 1):
        print("*", end = " ")
    print(" ")    

# %% ejercico 15

def exponente(base, exp):
    num = exp
    resultado = 1
    while num > 0:
        resultado = resultado * base 
        num = num -1
    print(base,"elevado a la potencia de", exp, "es:", resultado)

exponente(5, 4)