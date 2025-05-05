import random

# Datos de ejemplo: posiciones en 1D
datos = [1, 2, 3, 10, 11, 12]

# Número de clusters (grupos)
k = 2

# Inicializar los centroides aleatoriamente
centroides = random.sample(datos, k)

# Número de iteraciones
num_iteraciones = 10

for iteracion in range(num_iteraciones):
    # Crear listas para los grupos
    grupos = [[] for _ in range(k)]

    # Asignar cada punto al centroide más cercano
    for punto in datos:
        distancias = [abs(punto - c) for c in centroides]
        grupo_mas_cercano = distancias.index(min(distancias))
        grupos[grupo_mas_cercano].append(punto)
    
    # Mostrar agrupamientos actuales
    print(f"Iteración {iteracion + 1}")
    for idx, grupo in enumerate(grupos):
        print(f"  Grupo {idx + 1}: {grupo}")
    
    # Actualizar los centroides: promedio de cada grupo
    nuevos_centroides = []
    for grupo in grupos:
        if grupo:  # Evitar división por cero
            nuevo_centroide = sum(grupo) / len(grupo)
        else:
            nuevo_centroide = random.choice(datos)
        nuevos_centroides.append(nuevo_centroide)
    
    centroides = nuevos_centroides
    print(f"  Nuevos centroides: {centroides}\n")
