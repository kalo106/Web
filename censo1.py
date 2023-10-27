texto_multilinea = """
Esta es una cadena de texto
que abarca varias líneas.
Puedes escribir todo lo que quieras
sin preocuparte por los saltos de línea.
"""

print(texto_multilinea)


import sqlite3

conexion = sqlite3.connect('BaseDatos')
cursorBD = conexion.cursor()

def tablaExiste(nombreTabla):
    cursorBD.execute('''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE='table' AND name='{}' '''.format(nombreTabla))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute('''CREATE TABLE CARACTERIZACION (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE TEXT, PRECIO REAL) ''')
        return False

tablaExiste('CARACTERIZACION')

# Asegúrate de que el nombre de la tabla ('CARACTERIZACION') esté entre comillas.



import sqlite3


# Conecta a la base de datos y crea un cursor
com = sqlite3.connect('poblacion_afroFlorencia.db')
C = com.cursor()

# Define la tabla si no existe (corrección de errores de escritura)
C.execute('''CREATE TABLE IF NOT EXISTS caracterizacion (
    matricula TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    comuna TEXT,
    promedio REAL
)''')

# Inserta datos utilizando una lista de tuplas (corrección de errores de sintaxis)
nuevos_caracteres = [
    ('111', 'roberto', 'cruz', 'comuna 1', 1.0),
    ('222', 'marcos', 'marin', 'comuna 2', 2.0)
]

C.executemany('INSERT INTO caracterizacion VALUES (?, ?, ?, ?, ?)', nuevos_caracteres)

# Confirma los cambios en la base de datos
com.commit()

# Selecciona y muestra los primeros 5 registros (corrección de errores de sintaxis)
C.execute('SELECT * FROM caracterizacion')
resultados = C.fetchmany(5)
print(resultados)

# Cierra la conexión
com.close()


import sqlite3

# Función para crear la tabla si no existe
def crear_tabla_si_no_existe(conexion):
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS censo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        genero TEXT,
        direccion TEXT
    )''')
    conexion.commit()

# Función para insertar datos en la tabla
def insertar_datos(conexion, datos):
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO censo (nombre, edad, genero, direccion) VALUES (?, ?, ?, ?)', datos)
    conexion.commit()

# Función para solicitar datos al usuario
def obtener_datos_del_usuario():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    genero = input("Género: ")
    direccion = input("Dirección: ")
    return (nombre, edad, genero, direccion)

# Función principal
def main():
    conexion = sqlite3.connect('censo_poblacional.db')
    crear_tabla_si_no_existe(conexion)

    while True:
        print("\nIngrese datos del residente (o escriba 'salir' para finalizar):")
        datos = obtener_datos_del_usuario()

        if datos[0].lower() == 'salir':
            break

        insertar_datos(conexion, datos)
        print("Datos guardados con éxito.")

    conexion.close()
    print("Censo finalizado.")

if __name__ == "__main__":
    main()









