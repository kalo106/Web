# Leer tres valores numéricos desde el teclado
valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))
valor3 = float(input("Ingrese el tercer valor: "))

# Verificar si alguno de los valores es negativo
hay_negativo = valor1 < 0 or valor2 < 0 or valor3 < 0

# Sumar los tres valores
suma = valor1 + valor2 + valor3

# Imprimir el resultado de la suma
print("La suma de los tres valores es:", suma)

# Indicar si hay algún valor negativo entre los tres números
if hay_negativo:
    print("Hay al menos un número negativo entre los tres valores ingresados.")
else:
    print("No hay números negativos entre los tres valores ingresados.")
