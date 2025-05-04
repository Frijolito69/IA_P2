import random

# Parámetros del algoritmo
LONGITUD_CROMOSOMA = 5  # 5 bits para representar números de 0 a 31
TAMANIO_POBLACION = 6
PROB_CRUCE = 0.7
PROB_MUTACION = 0.1
NUM_GENERACIONES = 10

# Función objetivo (lo que queremos maximizar)
def funcion_objetivo(x):
    return x ** 2

# Funciones auxiliares
def generar_individuo():
    return ''.join(random.choice('01') for _ in range(LONGITUD_CROMOSOMA))

def decodificar(cromosoma):
    return int(cromosoma, 2)

def fitness(cromosoma):
    return funcion_objetivo(decodificar(cromosoma))

def seleccion_ruleta(poblacion):
    suma_fitness = sum(fitness(c) for c in poblacion)
    pick = random.uniform(0, suma_fitness)
    current = 0
    for c in poblacion:
        current += fitness(c)
        if current > pick:
            return c

def cruce(padre1, padre2):
    if random.random() < PROB_CRUCE:
        punto = random.randint(1, LONGITUD_CROMOSOMA - 1)
        hijo1 = padre1[:punto] + padre2[punto:]
        hijo2 = padre2[:punto] + padre1[punto:]
        return hijo1, hijo2
    else:
        return padre1, padre2

def mutacion(cromosoma):
    nuevo = ''
    for bit in cromosoma:
        if random.random() < PROB_MUTACION:
            nuevo += '1' if bit == '0' else '0'
        else:
            nuevo += bit
    return nuevo

# Algoritmo genético principal
def algoritmo_genetico():
    # Inicializar población
    poblacion = [generar_individuo() for _ in range(TAMANIO_POBLACION)]

    for generacion in range(NUM_GENERACIONES):
        print(f"\nGeneración {generacion+1}:")
        for c in poblacion:
            print(f"{c} (x={decodificar(c)}, fitness={fitness(c)})")
        
        nueva_poblacion = []

        # Crear nueva población
        while len(nueva_poblacion) < TAMANIO_POBLACION:
            # Selección
            padre1 = seleccion_ruleta(poblacion)
            padre2 = seleccion_ruleta(poblacion)

            # Cruce
            hijo1, hijo2 = cruce(padre1, padre2)

            # Mutación
            hijo1 = mutacion(hijo1)
            hijo2 = mutacion(hijo2)

            nueva_poblacion.extend([hijo1, hijo2])

        poblacion = nueva_poblacion[:TAMANIO_POBLACION]

    # Al final, mostramos el mejor
    mejor = max(poblacion, key=fitness)
    print(f"\nMejor solución encontrada: {mejor} (x={decodificar(mejor)}, fitness={fitness(mejor)})")

# Ejecutar
algoritmo_genetico()
