calculator_match =  input('please type one number: ')

adition = 1
rest = 2
division = 3
multiplication = 4
module = 5
powers = 6

if adition == 1: 
    print('you chosse adition how operation')
    adition = int(input('type one number: '))
    adition += int(input('type two number: '))
  
    print('the result is: ' , adition)
    
    
    
''''
    rest == 2:
    print('you chosse rest how operation')
    division == 3:
    print('you chosse division how operation')
elif multiplication == 4:
    print('you chosse multiplicarion how operation')
elif module == 5:
    print('you chosse module how operation')
elif  powers == 6:
    print('you chosse powers  how operation')

'''


    
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No es posible dividir por cero."
    return a / b

def division_entera(a, b):
    if b == 0:
        return "No es posible dividir por cero."
    return a // b

def exponente(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "No es posible calcular el módulo por cero."
    return a % b

while True:
    print("Calculadora con una sola variable \n")
    print("********************")
    print("* Menú de opciones *")
    print("********************")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. División entera")
    print("6. Exponente")
    print("7. Módulo o resto")
    print("8. Salir\n")

    numero = int(input("Introduce la opción deseada:"))

    if numero == 8:
        print("¡Hasta luego!")
        break

    if numero >= 1 and numero <= 7:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if numero == 1:
            resultado = suma(num1, num2)
        elif numero == 2:
            resultado = resta(num1, num2)
        elif numero == 3:
            resultado = multiplicacion(num1, num2)
        elif numero == 4:
            resultado = division(num1, num2)
        elif numero == 5:
            resultado = division_entera(num1, num2)
        elif numero == 6:
            resultado = exponente(num1, num2)
        elif numero == 7:
            resultado = modulo(num1, num2)

        print("El resultado es:", resultado)

    else:
        print("La opción elegida no existe, vuelve a intentar.")




