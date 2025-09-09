
# Servidor web simple que sirve archivos desde el directorio actual
import http.server
import socketserver

# Puerto donde correrá el servidor
PUERTO = 8000

# Crear handler (manejador de peticiones)
Handler = http.server.SimpleHTTPRequestHandler

# Crear el servidor
with socketserver.TCPServer(("", PUERTO), Handler) as httpd:
    print(f"Sirviendo en http://localhost:{PUERTO}")
    httpd.serve_forever()
