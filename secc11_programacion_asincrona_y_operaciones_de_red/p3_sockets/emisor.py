import socket

# Crear socket cliente TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar con el receptor (servidor)
client_socket.connect(('127.0.0.1', 5000))

# Enviar el mensaje
mensaje = "MENSAJE DESDE emisor.py"
print("Estoy mandando el mensaje..." )
client_socket.send(mensaje.encode())

# Cerrar la conexión
client_socket.close()
print("Conexion cerrada")
