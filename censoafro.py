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
