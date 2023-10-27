text = "maonrimoriamcumer"
dictionary = {}  # Usaremos un diccionario vacío

# Iteramos a través de la cadena
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        # Generamos las subcadenas y las agregamos al diccionario
        key = text[i:j]
        dictionary[key] = " "

# Imprimimos las claves del diccionario
for key in dictionary.keys():
    print(key)

    
















