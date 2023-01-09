#%% # Funcion de suma

def suma(a, b):
  return a + b

resultado = suma(455, 332)
print("El resultado de la suma es:", resultado) 

# %% Funcion de resta

def resta(a,b):
    return a - b
resultado = resta(458, 199)
print("El resultado de la resta es:", resultado) 

# %% funcion multiplicacion

def multiplicacion(a, b):
    return a * b
resultado = multiplicacion(238, 129)
print("El resultado de la multiplicacion es:", resultado)

# %% Funcion de division

def division(a,b):
    return a / b
resultado = division(40, 8)
print("El resultado de la división es:", resultado) 

# %% Función de potencias

def power(base, exponent):
  return base ** exponent
result = power(2, 3)
print(result)  # Imprime 8

# %% Función la raíz cuadrada de un número

import math

def square_root(raiz_cuadrada):
  return math.sqrt(raiz_cuadrada)

resultado = square_root(9)
print(resultado)  # Imprime 3


# %% Funcion factorial de 5

def factorial(n):
  if n == 0:
    return 1
  return n * factorial(n - 1)

resultado = factorial(5)
print(resultado)  # Imprimirá 120

# %% 10 número aleatorios del 1 al 100
import random

def numeros_aleatorios():
  numeros = []
  for i in range(10):
    numero = random.randint(1, 101)
    numeros.append(numero)
  return numeros

print(numeros_aleatorios())  # Imprimirá una lista de 10 números aleatorios entre 1 y 100

# %% calcular 21% iva del producto

def calcular_iva(precio):
  iva = precio * 0.21  # El 21% de IVA es 0.21
  return iva
precio = 500
iva = calcular_iva(precio)
precio_con_iva = precio + iva
print(precio_con_iva) 

# %% descontar el 21% del producto, esto es lo que nos roba el estado.

def descontar_iva(x):
  return x * 0.79
result = 500
resultado_con_iva = descontar_iva(result)
print("Esto es lo que vale realmente un producto, quitandole el 21% :",resultado_con_iva)  # Imprime 79

# %% iva de España 21% con iva y sin iva

def calcular_iva(precio):
  iva = precio * 0.21  # El 4% de IVA es 0.21
  return iva
precio = 500
iva = calcular_iva(precio)
precio_con_iva = precio + iva
print("Esto es que se gana el pais a razón del iva:",iva) # imprime 105

def descontar_iva(x):
  return x * 0.79
result = 500
resultado_con_iva = descontar_iva(result)
print("Esto es lo que vale realmente un producto, quitandole el 21% :",resultado_con_iva)  # Imprime 395

# %% iva de Andorra 4% con iva y sin iva

def calcular_iva(precio):
  iva = precio * 0.04  # El 4% de IVA es 0.21
  return iva
precio = 500
iva = calcular_iva(precio)
precio_con_iva = precio + iva
print("Esto es que se gana el pais a razón del iva:",iva) # imprime 20

def descontar_iva(x):
  return x * 0.96
result = 500
resultado_con_iva = descontar_iva(result)
print("Esto es lo que vale realmente un producto, quitandole el 4% :",resultado_con_iva)  # Imprime 480

# %% información completa de 10 coches

def info_coches(coches):
  resultado = []
  for coche in coches:
    resultado.append(f"Marca: {coche['marca']} Modelo: {coche['modelo']} Color: {coche['color']} Motor: {coche['motor']} Caballos: {coche['caballos']} Kilómetros: {coche['kilometraje']}")
  return resultado
coches = [{'marca': 'Ford', 'modelo': 'Mustang', 'color': 'Rojo', 'motor': 'V8', 'caballos': 450, 'kilometraje': 100000},
        {'marca': 'Toyota', 'modelo': 'Prius', 'color': 'Azul', 'motor': 'Híbrido', 'caballos': 122, 'kilometraje': 50000},
        {'marca': 'Peugeot', 'modelo': '208', 'color': 'Blanco', 'motor': 'Diesel', 'caballos': 82, 'kilometraje': 20000}]

info_coches(coches)


# %%
