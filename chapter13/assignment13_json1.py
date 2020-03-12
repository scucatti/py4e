# The program will prompt for a URL,
# read the JSON data from that URL using urllib
# and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import json

# prompt for a url
# enter_url = input('Enter a URL: ')

# URL para teste
enter_url = 'http://py4e-data.dr-chuck.net/comments_278292.json'
#read the data and transform in one big string
url = urllib.request.urlopen(enter_url).read()

info = json.loads(url)    #gets the info of json from the url

#extraio só os comments do link
comments = info['comments']

sum = 0

# vou varrer cada dicionário e extrair o count
for element in comments:
    sum = sum + element['count']
    
print(sum)
