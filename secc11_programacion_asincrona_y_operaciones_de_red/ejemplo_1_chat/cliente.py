import socket

HOST = 'localhost'
PUERTO = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PUERTO))
    print("Conectado al servidor. Escribe mensajes:")
    while True:
        mensaje = input("> ")
        if mensaje.lower() == "salir":
            print('Se ha salido...')
            break
        s.sendall(mensaje.encode())
