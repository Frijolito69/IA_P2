import random

# Definir probabilidades condicionales
P_A_true = 0.3  # Probabilidad de que A sea True
P_A_false = 1 - P_A_true  # Probabilidad de que A sea False

# Probabilidad de B dada A
def P_B_given_A(A):
    if A:  # Si A es True
        return 0.8  # Probabilidad de que B sea 1 dado que A es True
    else:  # Si A es False
        return 0.2  # Probabilidad de que B sea 1 dado que A es False

# Probabilidad de C dada B
def P_C_given_B(B):
    if B:  # Si B es 1
        return 0.9  # Probabilidad de que C sea 1 dado que B es 1
    else:  # Si B es 0
        return 0.1  # Probabilidad de que C sea 1 dado que B es 0

# Ponderación de Verosimilitud
def ponderacion_de_verosimilitud(num_muestras=1000):
    # Inicializar variables
    total_peso = 0
    total_ponderado_A = 0
    
    for _ in range(num_muestras):
        # 1. Muestreo de las variables no observadas (A y B)
        A = random.random() < P_A_true  # True con probabilidad P_A_true
        B = random.random() < P_B_given_A(A)  # Dependiente de A
        
        # 2. Ponderación de la muestra (probabilidad de la observación)
        C_observado = 1  # Sabemos que C es observado como 1
        
        # Calculamos la verosimilitud de C dado B
        verosimilitud = P_C_given_B(B) if C_observado else (1 - P_C_given_B(B))
        
        # 3. Ponderar la muestra por la verosimilitud
        peso = verosimilitud
        
        # 4. Acumulamos las ponderaciones y las muestras de A
        total_peso += peso
        total_ponderado_A += peso * A
    
    # 5. Promediamos las muestras ponderadas
    probabilidad_A_dado_B = total_ponderado_A / total_peso
    return probabilidad_A_dado_B

# Calcular la probabilidad de A dado B
probabilidad_A_dado_B = ponderacion_de_verosimilitud()
print(f"P(A | B = 1) = {probabilidad_A_dado_B:.4f}")
