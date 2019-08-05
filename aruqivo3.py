# interação com usuário
num = input("Digite o numero 1:")

nome = input("Seu nome: ")
print("Bem-vindo " + nome + "!")

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# strings

nome = "Leticia"
sobrenome = "Teixeira"

print (nome + " " + sobrenome)

tamanho = len(nome)
print(tamanho)
print(nome[3])
print(sobrenome[0:4])

# transformar em minúsculo
nome = nome.lower()
sobrenome = sobrenome.upper()
print (nome)
print (sobrenome)

# função strip: remove carcteres especiais
# função split: converte a string em uma lista toda vez q o parâmetro passado for encontrado

string = "O rato roeu a roupa do rei de Roma"

busca = string.find("rei")
print(busca)

string = string.replace("rei","rainha")
print(string)
