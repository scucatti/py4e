# Chapter 12: Networked programs

# Scraping HTML Data with BeautifulSoup

# In this assignment you will write a Python program to use urllib to read the
# HTML from the data files below,and parse the data, extracting numbers and
# compute the sum of the numbers in the file

import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

sum = 0  #variável que irei usar para somar os números

#url = input('Enter - ')
url = 'http://python-data.dr-chuck.net/comments_42.html'
#read the data and transform in one big string
html = urllib.request.urlopen(url).read()
#parse the data in the 'html' string from the url
soup = BeautifulSoup(html,'html.parser')

# agora eu preciso encontrar os números da variável 'soup'
# os números na página estão dentro dos elementos 'span',
# então preciso selecionar só esses elementos
elementos_span = soup('span')

# encontrar os números dentro desses elementos_span
for elemento in elementos_span:
    elemento = str(elemento)
    #procura usando regex os numeros e gera uma lista de strings com eles
    numbers = re.findall('[0-9]+', elemento)

    for number in numbers :
        #adiciona os números presentes no elemento examinado na soma
        sum = sum + int(number)
        print('numero', int(number), 'adicionado, a soma agora é',sum)
