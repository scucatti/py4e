# Chapter 11: Regex

# Read through and parse a file with text and numbers
# Extract all the numbers in the file and compute the sum of the numbers

import re

name = input('Enter a file: ')
handle = open(name)

sum = 0.0

for line in handle :
    line = line.rstrip()
    #procura por números na linha, incluindo números float
    y = re.findall('[0-9.]+', line)
#se não encontrar nenhum número, voltar e pegar outra linha
    if len(y) < 1:
        continue
#se encontrar um número, adicionar na soma de todos os números do texto
    for num in y:
        num = float(num)
        sum = sum + num
        # print(num)

print('Sum of numbers:', sum)
