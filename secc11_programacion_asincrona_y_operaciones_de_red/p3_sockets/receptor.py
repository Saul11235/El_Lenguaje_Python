import socket

# Crear socket servidor TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5000))  # IP local y puerto
server_socket.listen()

print("Esperando conexión en 127.0.0.1:5000...")

# Aceptar una conexión entrante
conn, addr = server_socket.accept()
print(f"Conectado desde: {addr}")

# Recibir el mensaje
mensaje = conn.recv(1024).decode()
print("Mensaje recibido:", mensaje)

# Cerrar la conexión
conn.close()
server_socket.close()
