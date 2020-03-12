# Chapter 12: Networked Programs

# Assignment: Following Links in HTML Using BeautifulSoup
#
# In this assignment you will write a Python program that expands on
# https://www.py4e.com/code3/urllinks.py.
# The program will use urllib to read the HTML from the data files below,
# extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position from the top
# and follow that link,
# repeat the process a number of times, and report the last name you find.


#urllinks.py:
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
#read the data and transform in one big string
html = urllib.request.urlopen(url, context=ctx).read()
#parse the data in the 'html' string from the url
soup = BeautifulSoup(html, 'html.parser')

#lista onde armazenarei todos os links (anchor tags) da página
links_list = list()

# Aloquei todas as anchor tags na lista de strings "links"
tags = soup('a')
for tag in tags:
    links_list.append(tag.get('href', None))

position = input('Enter a position: ')
position = int(position)
#initial_link = links_list[(position)]
print('The link in the position requested is', links_list[position])

new_list = list()
#follow the link in the position given by the input

#abro o link na posição dada pelo usuário
initial_link = urllib.request.urlopen(links_list[(position)],context=ctx).read()
soup_link = BeautifulSoup(initial_link, 'html.parser')

tags_link = soup_link('a') #encontro todos os novos links no link inicial
for i in tags_link :
    new_list.append(i.get('href', None))

print(new_list)


# agora eu preciso procurar uma tag que está em uma posição particular a partir do topo (?)
# follow the Link
