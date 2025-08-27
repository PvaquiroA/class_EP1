# Con interacción de consola
# Calcule X números aleatorios en un rango determinado
import random

print("\n**** Generador de números aleatorios ****\n")

cantidad = int(input("Ingresa la cantidad de números que deseas: "))
minimo = int(input("Ingresa el valor mínimo del rango: "))
maximo = int(input("Ingresa el valor máximo del rango: "))

numeros = random.sample(range(minimo, maximo + 1), cantidad)

print(f"Los números son: {numeros}")