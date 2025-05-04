import random

# Definimos la función objetivo
def funcion_objetivo(x):
    return (x - 5) ** 2

def busqueda_haz_local(k, max_iteraciones):
    # Inicializar k soluciones aleatorias entre -10 y 10
    soluciones = [random.randint(-10, 10) for _ in range(k)]

    for iteracion in range(max_iteraciones):
        vecinos = []

        # Generamos vecinos de todas las soluciones actuales
        for s in soluciones:
            vecinos.append(s + 1)  # vecino a la derecha
            vecinos.append(s - 1)  # vecino a la izquierda

        # Combinamos soluciones actuales y sus vecinos
        candidatos = soluciones + vecinos

        # Elegimos los k mejores candidatos
        soluciones = sorted(candidatos, key=funcion_objetivo)[:k]

        # Imprimimos progreso
        print(f"Iteración {iteracion+1}: soluciones actuales = {soluciones}")

        # Si alguna solución es óptima (muy cerca de 5), terminamos
        if any(funcion_objetivo(s) == 0 for s in soluciones):
            break

    # Devolvemos la mejor solución encontrada
    mejor = min(soluciones, key=funcion_objetivo)
    return mejor

# Prueba
mejor = busqueda_haz_local(k=3, max_iteraciones=20)
print("Mejor solución encontrada:", mejor)
