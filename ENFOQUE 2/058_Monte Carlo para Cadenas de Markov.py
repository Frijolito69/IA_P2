import random
import math
import matplotlib.pyplot as plt

# Definir la función de densidad de la distribución objetivo (en este caso N(0, 1))
def p(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x**2)

# Función de Metropolis-Hastings
def metropolis_hastings(num_iter=10000):
    # Estado inicial arbitrario
    x_current = random.uniform(-5, 5)
    
    # Lista para almacenar las muestras
    muestras = []
    
    for _ in range(num_iter):
        # Propuesta de un nuevo estado
        x_propuesto = x_current + random.gauss(0, 1)  # Propuesta usando una distribución normal N(0, 1)
        
        # Cálculo de la razón de aceptación
        r = p(x_propuesto) / p(x_current)
        
        # Aceptación o rechazo del nuevo estado
        if random.random() < min(1, r):
            x_current = x_propuesto
        
        # Almacenar la muestra
        muestras.append(x_current)
    
    return muestras

# Generar muestras usando Metropolis-Hastings
num_iter = 10000
muestras = metropolis_hastings(num_iter)

# Mostrar el histograma de las muestras
plt.hist(muestras, bins=50, density=True, alpha=0.6, color='g')
plt.title(f'Muestras generadas con Metropolis-Hastings\n(Distribución Normal N(0, 1))')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()
