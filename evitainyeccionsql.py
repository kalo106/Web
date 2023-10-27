import sqlite3

# Conexión a la base de datos SQLite (en memoria para este ejemplo)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Crear una tabla de usuarios
cursor.execute('''CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

# Datos de usuario proporcionados por el usuario (simulación)
nombre_usuario = "Alice"
edad_usuario = 30

# Evitar la inyección SQL utilizando consultas parametrizadas
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre_usuario, edad_usuario))
conn.commit()

# Consulta segura utilizando parámetros
nombre_buscar = "Alice"
cursor.execute("SELECT * FROM usuarios WHERE nombre = ?", (nombre_buscar,))
resultado = cursor.fetchall()

# Mostrar los resultados
print(resultado)

# Cerrar la conexión a la base de datos
conn.close()
