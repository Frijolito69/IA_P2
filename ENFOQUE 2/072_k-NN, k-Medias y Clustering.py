import math

# Datos de entrenamiento: (punto, clase)
datos = [
    ([1, 2], 'Rojo'),
    ([2, 3], 'Rojo'),
    ([3, 3], 'Azul'),
    ([6, 5], 'Azul'),
    ([7, 8], 'Azul')
]

# Punto a clasificar
nuevo_punto = [3, 4]

# Número de vecinos
k = 3

# Función para calcular la distancia euclidiana
def distancia(p1, p2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p1, p2)))

# Calcular las distancias
distancias = []
for punto, etiqueta in datos:
    d = distancia(punto, nuevo_punto)
    distancias.append((d, etiqueta))

# Ordenar por distancia y tomar los k vecinos más cercanos
distancias.sort()
vecinos_cercanos = distancias[:k]

# Votar la clase más común
conteo = {}
for _, etiqueta in vecinos_cercanos:
    if etiqueta not in conteo:
        conteo[etiqueta] = 0
    conteo[etiqueta] += 1

# Elegir la clase con más votos
clase_asignada = max(conteo, key=conteo.get)

print(f"El nuevo punto {nuevo_punto} se clasifica como: {clase_asignada}")
