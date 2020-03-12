# Chapter 13: Python and web services

# write a Python program somewhat similar to https://py4e.com/code3/geoxml.py.
# The program will prompt for a URL,
# read the XML data from that URL using urllib
# parse and extract the comment counts from the XML data
# compute the sum of the numbers in the file and enter the sum

# cabeçalho vindo do programa de referência
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

##### fim do código inteiramente copiado ####

# promp for a url:
# enter_url = input('Enter a url: ')
# testando com os dados que eu acho que serão pedidos no site
enter_url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
#usando urllib, obter os dados xml da página
url = urllib.request.urlopen(enter_url, context=ctx).read()    #read the data and transform in one big string
xml = ET.fromstring(url)
# analisar e extrair os 'comment counts' a partir dos dados XML
comments = xml.findall('comments/comment')

sum = 0

for item in comments:
    numero = int(item.find('count').text)
    sum = sum + numero
    print(numero)

print('a soma dos números é', sum)
