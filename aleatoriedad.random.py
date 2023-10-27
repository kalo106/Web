import random

# Lista de las 18 familias
familias = ["Familia 1", "Familia 2", "Familia 3", "Familia 4", "Familia 5", "Familia 6",
            "Familia 7", "Familia 8", "Familia 9", "Familia 10", "Familia 11", "Familia 12",
            "Familia 13", "Familia 14", "Familia 15", "Familia 16", "Familia 17", "Familia 18"]

# Elige aleatoriamente una familia para el aseo
familia_elegida = random.choice(familias)

print(f"La familia encargada del aseo este sábado es: {familia_elegida}")
