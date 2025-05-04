import random

# Definimos la función objetivo a minimizar
def funcion_objetivo(x):
    return (x - 5) ** 2

def busqueda_tabu(inicio, max_iteraciones, tamaño_tabu):
    solucion_actual = inicio
    mejor_solucion = inicio
    lista_tabu = []  # Lista tabú para prohibir soluciones recientes

    for iteracion in range(max_iteraciones):
        # Generamos vecinos (aumentar o disminuir en 1 unidad)
        vecinos = [solucion_actual + 1, solucion_actual - 1]
        
        # Filtrar vecinos que están en la lista tabú
        vecinos_validos = [v for v in vecinos if v not in lista_tabu]

        if not vecinos_validos:
            break  # Si no hay vecinos válidos, se detiene

        # Elegimos el mejor vecino
        vecino = min(vecinos_validos, key=funcion_objetivo)

        # Actualizamos la solución actual
        solucion_actual = vecino

        # Actualizamos la mejor solución encontrada
        if funcion_objetivo(solucion_actual) < funcion_objetivo(mejor_solucion):
            mejor_solucion = solucion_actual

        # Actualizamos la lista tabú
        lista_tabu.append(solucion_actual)
        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)  # Quitamos el elemento más viejo si se excede el tamaño

        # Imprimimos progreso
        print(f"Iteración {iteracion+1}: solución actual = {solucion_actual}, mejor = {mejor_solucion}")

    return mejor_solucion

# Prueba
mejor = busqueda_tabu(inicio=0, max_iteraciones=10, tamaño_tabu=3)
print("Mejor solución encontrada:", mejor)
