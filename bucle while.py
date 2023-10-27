# Pide al usuario que ingrese su nombre
nombre_usuario = input("Escribe tu nombre: ")

# Saluda al usuario utilizando el nombre ingresado
print("Hola", nombre_usuario, ", esto es el incremento y decremento de una variable\n")

print("Incremento o aumento:")
x = 1  # Valor inicial de x
print("El valor inicial de x es:", x)

# Realiza el incremento de x cuatro veces
x += 4
print("El valor final de x es:", x, "\n")

print("Decremento o disminución:")
print("El valor inicial de x es:", x)

# Realiza el decremento de x cuatro veces
x -= 4
print("El valor final de x es: ", x) 





#while buckle infinite cuando x+=0
'''
x = 0
while x <10:
       print(x)
       x +=    0
       print(x)
'''
       
# bucle While        
x = 0
contador = 0

while x <= 10:
 for _ in range(10):      
               print('1', 'charly', 'x+= 1')
               x += 1
               contador += 1
  
# Inicializa el contador en 0
contador = 0

# Incrementa el contador cada vez que ocurre un evento
for _ in range(10):  # Supongamos que ocurre el evento 10 veces
    contador += 1

# El contador ahora contiene el recuento de eventos
print("El contador es:", contador)
       
                    
       