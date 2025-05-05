import random

# Datos de ejemplo: número de caras obtenidas en 5 lanzamientos
# No sabemos qué moneda se usó en cada caso
datos = [5, 4, 1, 0, 3, 2, 5, 1]

# Inicializamos las probabilidades de sacar cara con cada moneda
p_cara_A = 0.6  # suposición inicial
p_cara_B = 0.5

# Número de iteraciones del algoritmo
num_iteraciones = 10

for iteracion in range(num_iteraciones):
    # Paso E: calcular la responsabilidad (probabilidad de que un dato venga de cada moneda)
    responsabilidades_A = []
    responsabilidades_B = []
    
    for caras in datos:
        cruces = 5 - caras
        
        # Probabilidad de que el dato venga de la moneda A
        prob_A = (p_cara_A ** caras) * ((1 - p_cara_A) ** cruces)
        
        # Probabilidad de que el dato venga de la moneda B
        prob_B = (p_cara_B ** caras) * ((1 - p_cara_B) ** cruces)
        
        # Normalizamos para que sumen 1
        total = prob_A + prob_B
        resp_A = prob_A / total
        resp_B = prob_B / total
        
        responsabilidades_A.append(resp_A)
        responsabilidades_B.append(resp_B)
    
    # Paso M: actualizar las probabilidades usando las responsabilidades
    sum_cara_A = 0.0
    sum_cara_B = 0.0
    total_A = 0.0
    total_B = 0.0
    
    for i, caras in enumerate(datos):
        cruces = 5 - caras
        
        sum_cara_A += responsabilidades_A[i] * caras
        sum_cara_B += responsabilidades_B[i] * caras
        total_A += responsabilidades_A[i] * 5
        total_B += responsabilidades_B[i] * 5
    
    # Actualizamos las probabilidades
    p_cara_A = sum_cara_A / total_A
    p_cara_B = sum_cara_B / total_B

    # Mostramos los parámetros en cada iteración
    print(f"Iteración {iteracion + 1}")
    print(f"  Probabilidad de cara con moneda A: {p_cara_A:.4f}")
    print(f"  Probabilidad de cara con moneda B: {p_cara_B:.4f}\n")
