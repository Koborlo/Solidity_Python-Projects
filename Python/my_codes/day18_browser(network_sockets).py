import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
full_data = ''
while True:
    data = mysock.recv(512)
    if len(data) <1 :    break
    chunk = data.decode()
    print(chunk, end="")
    full_data += chunk
mysock.close()
bag ={}
words = full_data.split()
for word in words:  bag[word] = bag.get(word,0) + 1
print(bag)
for count, word in sorted([(v, k) for k, v in bag.items()], reverse=True):
    print(word, count)
