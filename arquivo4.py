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
