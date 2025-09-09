
import sqlite3

# 1. Conectar a una base de datos (se crea si no existe)
conexion = sqlite3.connect("mi_base_de_datos.db")

# 2. Crear un cursor (permite ejecutar comandos SQL)
cursor = conexion.cursor()

# 3. Crear una tabla (si no existe)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER,
        ciudad TEXT
    )
""")
print("Tabla 'personas' creada (si no existía).")

# 4. Insertar datos en la tabla
cursor.execute("INSERT INTO personas (nombre, edad, ciudad) VALUES (?, ?, ?)", ("Ana", 30, "Madrid"))
cursor.execute("INSERT INTO personas (nombre, edad, ciudad) VALUES (?, ?, ?)", ("Luis", 25, "Barcelona"))
conexion.commit()  # Guardar cambios
print("Datos insertados.")

# 5. Consultar datos
cursor.execute("SELECT * FROM personas")
filas = cursor.fetchall()
print("Registros en la tabla 'personas':")
for fila in filas:
    print(fila)

# 6. Actualizar datos
cursor.execute("UPDATE personas SET ciudad = ? WHERE nombre = ?", ("Valencia", "Luis"))
conexion.commit()
print("Ciudad actualizada para Luis.")

# 7. Eliminar registros
cursor.execute("DELETE FROM personas WHERE nombre = ?", ("Ana",))
conexion.commit()
print("Registro de Ana eliminado.")

# 8. Cerrar la conexión
conexion.close()
print("\nConexión cerrada.")
