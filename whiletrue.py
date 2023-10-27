num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

suma = num1 + num2 + num3

print(f"La suma de los tres números es: {suma}")


# Inicializar la variable para almacenar el producto
producto = 1

# Repetir hasta que se ingrese un número negativo
while True:
    # Leer un número desde el teclado
    numero = int(input("Ingrese un número: "))

    # Verificar si el número ingresado es positivo
    if numero > 0:
        # Multiplicar el número al producto acumulado
        producto *= numero
    else:
        break

# Mostrar el resultado final de la multiplicación
print("El producto de los números positivos ingresados es:", producto)
