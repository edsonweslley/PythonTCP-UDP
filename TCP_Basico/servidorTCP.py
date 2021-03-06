def handle_client(client_socket):
    request = client_socket.recv(1024)
    
    print "[*] Recebido: %s" % request
    
    client_socket.send("[*] Mensagem recebida pelo servidor")
    
    client_socket.close()

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)
print "[*] Escutando em %s:%d" % (bind_ip,bind_port)

while True:
    client,addr = server.accept()
    
    print "[*] Conexao aceita de %s:%d" % (addr[0], addr[1])
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
                                           