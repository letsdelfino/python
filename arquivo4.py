# -*- coding: utf-8 -*-
#função

def soma(x, y):
    print(x+y)

soma(3,4)

# manipulação de arquivos

arquivo = open("Arquivo.txt", "a+")

arquivo.write("Esse é o meu arquivo")
linhas = arquivo.readlines()
print(linhas)
texto = arquivo.read()
print(texto)

arquivo.close()

lista = ["maça", "abacate", "laranja", "melancia"]
lista2 = [1,2,3,4,5]
lista3 = ["maça", 0,"abacate",4 , 9.5, "laranja", "melancia"]

print(lista + lista2 + lista3)

lista.append("limão")
print(lista)

if 2 in lista2:
    print ("2 está na lista")

del lista[0:2]
print(lista)

lista4 = [4444.812398, 0, 234234, 4, 3, 1234, 98]
lista4.sort()
print(lista4)

lista4.reverse()
print(lista4)

import random

numero = random.randint(0,10)
print(numero)

lista5 = [4,10,14]
numero = random.choice(lista5)
print(numero)
