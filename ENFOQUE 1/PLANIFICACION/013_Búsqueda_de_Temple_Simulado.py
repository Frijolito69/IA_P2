import random
import math

# Definimos la función objetivo
def funcion_objetivo(x):
    return (x - 5) ** 2

def temple_simulado(inicio, temperatura_inicial, tasa_enfriamiento, max_iteraciones):
    solucion_actual = inicio
    mejor_solucion = inicio
    temperatura = temperatura_inicial

    for iteracion in range(max_iteraciones):
        # Generar un vecino aleatorio (sumar o restar un número pequeño)
        vecino = solucion_actual + random.choice([-1, 1])

        # Calculamos el cambio de energía (diferencia de costos)
        delta = funcion_objetivo(vecino) - funcion_objetivo(solucion_actual)

        # Decidir si aceptamos el vecino
        if delta < 0:
            # Mejor solución, aceptamos siempre
            solucion_actual = vecino
        else:
            # Peor solución, aceptamos con probabilidad e^(-delta/temperatura)
            probabilidad = math.exp(-delta / temperatura)
            if random.random() < probabilidad:
                solucion_actual = vecino

        # Actualizamos la mejor solución encontrada
        if funcion_objetivo(solucion_actual) < funcion_objetivo(mejor_solucion):
            mejor_solucion = solucion_actual

        # Enfriar la temperatura
        temperatura *= tasa_enfriamiento

        # Imprimimos progreso
        print(f"Iteración {iteracion+1}: solución actual = {solucion_actual}, mejor = {mejor_solucion}, temperatura = {temperatura:.2f}")

        # Condición de paro adicional (temperatura muy baja)
        if temperatura < 1e-3:
            break

    return mejor_solucion

# Prueba
mejor = temple_simulado(inicio=0, temperatura_inicial=100, tasa_enfriamiento=0.9, max_iteraciones=100)
print("Mejor solución encontrada:", mejor)
