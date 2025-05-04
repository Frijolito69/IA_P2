import random

# Definimos un laberinto donde ' ' es camino libre, '#' es muro y 'G' es la meta
laberinto = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', 'G', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

# Posiciones posibles de movimiento: (arriba, abajo, izquierda, derecha)
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# El agente solo conoce el lugar donde está
def busqueda_online(laberinto, inicio):
    fila, columna = inicio
    visitados = set()  # Para guardar posiciones visitadas

    while True:
        print(f"Estoy en {fila}, {columna}")
        if laberinto[fila][columna] == 'G':
            print("¡Encontré la meta!")
            break
        
        visitados.add((fila, columna))
        vecinos = []

        # Revisamos vecinos accesibles
        for mov in movimientos:
            nueva_fila = fila + mov[0]
            nueva_columna = columna + mov[1]

            # Verificamos si no nos salimos del laberinto
            if 0 <= nueva_fila < len(laberinto) and 0 <= nueva_columna < len(laberinto[0]):
                if laberinto[nueva_fila][nueva_columna] != '#' and (nueva_fila, nueva_columna) not in visitados:
                    vecinos.append((nueva_fila, nueva_columna))

        if not vecinos:
            print("¡Estoy atrapado! No hay más caminos libres.")
            break

        # Elegimos un vecino aleatorio para explorar
        fila, columna = random.choice(vecinos)

# Posición inicial del agente
inicio = (2, 2)

# Ejecutamos la búsqueda
busqueda_online(laberinto, inicio)
