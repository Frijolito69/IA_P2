# Definimos una función para aplicar el Teorema de Bayes
def bayes_learner(prior, likelihood, evidence):
    # Calculamos la probabilidad posterior usando la fórmula de Bayes
    posterior = (likelihood * prior) / evidence
    return posterior

# Definimos los valores de nuestro ejemplo
P_H = 0.2      # Probabilidad a priori de que sea spam
P_D_given_H = 0.8  # Probabilidad de que contenga "dinero rápido" si es spam
P_D = 0.3      # Probabilidad de que cualquier correo contenga "dinero rápido"

# Llamamos a nuestra función
P_H_given_D = bayes_learner(P_H, P_D_given_H, P_D)

# Mostramos el resultado
print(f"La probabilidad de que el correo sea spam dado el dato observado es: {P_H_given_D:.3f}")
