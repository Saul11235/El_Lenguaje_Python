import socket
import threading

# Configuración del servidor
HOST = '0.0.0.0'   # Escucha en todas las interfaces
PUERTO = 12345     # Puerto donde escuchar

def manejar_cliente(conn, addr):
    print(f"[+] Nueva conexión desde {addr}")
    try:
        while True:
            datos = conn.recv(1024)
            if not datos:
                break
            mensaje = datos.decode().strip()
            print(f"[{addr}] {mensaje}")
    except Exception as e:
        print(f"[{addr}] Error: {e}")
    finally:
        print(f"[-] Conexión cerrada con {addr}")
        conn.close()

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PUERTO))
    servidor.listen()
    print(f"[*] Servidor escuchando en {HOST}:{PUERTO}...")
    try:
        while True:
            conn, addr = servidor.accept()
            hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
            hilo.start()
    except KeyboardInterrupt:
        print("\n[!] Servidor detenido manualmente.")
    finally:
        servidor.close()

if __name__ == "__main__":
    main()
