# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Solicitar al usuario que elija una operación
print("Elija una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
operation = int(input("Ingrese el número de la operación deseada: "))

# Realizar la operación seleccionada
if operation == 1:
    resultado = num1 + num2
    print(f"La suma es: {resultado}")
elif operation == 2:
    resultado = num1 - num2
    print(f"La resta es: {resultado}")
elif operation == 3:
    resultado = num1 * num2
    print(f"La multiplicación es: {resultado}")
elif operatio  == 4:
    if num2 == 0:
    
        print("La división por cero no está permitida.")
    else:
        resultado = num1 / num2
        print(f"La división es: {resultado}")
else:
    print("Operación no válida.")
