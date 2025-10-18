"""
Hacer una programa que muestre 10 números aleatorios con ciclos For.
"""
from random import randint, uniform, random
for contador in range(10):
    numero = randint(0, 1000)
    print(numero)
    