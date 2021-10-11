import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
teste = sock.connect_ex(('172.16.8.238', 8080))

if teste == 0:
    print("Jenkins está funcionando")
else:
    print("Jenkins parado... favor verificar")

sock.close()