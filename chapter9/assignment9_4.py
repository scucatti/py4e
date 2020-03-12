# Chapter 9: Dictionaries

# Exercise 4: Write a program to read through a mail log,
# build a histogram using a dictionary to count how many messages have come
# from each email address, and print the dictionary.

# Add code to the above program to figure out who has the most messages
# in the file. After all the data has been read and the dictionary has
# been created, look through the dictionary using a maximum loop
# to find who has the most messages and print how many messages the person has.
#
fname = input('Enter a file name: ')
fhandle = open(fname)
# fhandle = open('mbox-short.txt') to test with a standard mail log

counts = dict()   # creates an empty dictionary

# separar os endereços de e-mail presentes no arquivo
# ler todas as linhas do arquivo, separar as linhas que começam com 'From'
# se a linha começar com 'From', armazenar o endereço em um dicionário
for line in fhandle :
    line = line.rstrip()   # retira os espaços em branco
    words = line.split()  # separa a linha em uma lista de palavras

    if len(words) < 2 or words[0] != 'From':
        continue

# para cada linha que começar com 'From', armazenar o endereço de email
# no histograma
    for word in words :
        # armazena o endereço de email
        # (segundo elemento da lista de palavras) no dicionario email
        email = words[1]# armazena o endereço de email
        #cria um histograma no dicionário 'counts' armazenando emails
        # e também quantas vezes ele aparece
        counts[words[1]] = counts.get(words[1],0)+1

# # print para conferir que o dicionário foi criado
# for name,value in counts.items() :
#     print(name,value)

# encontrar qual endereço de email enviou mais mensagens
max_endereco = None
max_value = None

for endereco,value in counts.items() :
    if max_value is None or value > max_value :
        max_endereco = endereco
        max_value = value

print(max_endereco,max_value)
