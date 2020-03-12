# Chapter 10: Tuples

# This program counts the distribution of the hour of the day for each of
# the messages.
# You can pull the hour from the "From" line by finding the time string
# and then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour, print out the counts,
# one per line, sorted by hour.

fname = input('Enter a file name: ')
fhandle = open(fname)

#criando o dicionário que vai contar quantas vezes os emails foram enviados
# para cada hora
counts = dict()

# primeiro encontrar as linhas que começam com 'From'
for line in fhandle :
    line = line.rstrip() #tira os espaços em branco
    words = line.split()  #separa a linha em uma lista de palavras

    if len(words) < 2 or words[0] != 'From' :
        #vamos ignorar as linhas que não começam com 'From'
        continue

    # para cada lista de palavras criada para as linhas que começam com From
    # queremos só a hora que o email foi enviado, sem se importar com os
    # minutos e segundos
    horario = words[5].split(':')
    #a hora que o email foi enviado é a primeira posição da lista
    #"time_list" --> time_list[0]
    hour = horario[0]
    #criar um dicionário que conta quantas vezes os emails foram enviados
    # para cada hora que aparece no arquivo
    counts[hour] = counts.get(hour,0)+1

# criamos uma lista de tuples com os itens do dicionário organizados por hora
lst = sorted(counts.items())

#por fim, printar as informações de cada tuple
# primeiro mostrando o horário, depois quantos emails foram enviados no horário
for h,c in lst :
     print(h,c)
