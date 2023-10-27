number_one = int (input('type fist number: '))
number_two= int (input('type two number: '))
number_three= int (input('type three number: '))

if number_one >  number_two and number_three:

   print('the number', number_one , 'is eldely')
   
elif number_two > number_three and number_one:
     
    print('the number', number_two , 'is eldely')
    
elif number_three > number_two and number_one:
    print('the number' , number_three , 'is the eldely')
    
    
    
number_one = int(input('Enter the first number: '))
number_two = int(input('Enter the second number: '))
number_three = int(input('Enter the third number: '))

max_number = max(number_one, number_two, number_three)

print('The largest number is:', max_number)


#DO AN HOMEWORK

class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = False

class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre, descripcion):
        tarea = Tarea(nombre, descripcion)
        self.tareas.append(tarea)

    def marcar_completada(self, tarea):
        tarea.completada = True

    def listar_tareas(self):
        for tarea in self.tareas:
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{tarea.nombre} - {tarea.descripcion} ({estado})")

# Crear una lista de tareas
mi_lista = ListaDeTareas()

# Agregar tareas
mi_lista.agregar_tarea("Hacer compras", "Comprar leche y pan")
mi_lista.agregar_tarea("Estudiar Python", "Repasar clases y ejercicios")

# Marcar una tarea como completada
mi_lista.marcar_completada(mi_lista.tareas[0])

# Listar todas las tareas
mi_lista.listar_tareas()

 