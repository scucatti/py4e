# write a program to retrieve a web page over a socket and
# display the reader from the web server

import socket

# programa pede ao usuário uma página da internet para abrir
page = input('Enter the web page: ')

http_page = 'http://'+ page
pieces = page.split('/')
host = pieces[0]

# recupera a página que foi pedida em um socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((host,80))
cmd = ('GET '+ http_page + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

# display both the readers and the body

decode = ''

while True:
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    # faço o decode do texto inteiro
    decode = decode + data.decode()

mysock.close()

decode = decode.split('\n')
print(decode)

for line in decode :
    line = line.rstrip()
    if line == '':
        break
    print(line)
