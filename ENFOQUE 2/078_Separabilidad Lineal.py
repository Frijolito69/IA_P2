# Perceptrón para clasificación binaria
def perceptron(X, y, epochs=10, eta=0.1):
    # Inicializamos los pesos y el sesgo
    weights = np.zeros(X.shape[1])  # Pesos para 2 características
    bias = 0
    errors = []

    for _ in range(epochs):
        total_error = 0
        for xi, target in zip(X, y):
            # Calculamos la salida
            net_input = np.dot(xi, weights) + bias
            output = 1 if net_input >= 0 else 0  # Activación de umbral

            # Actualizamos los pesos y sesgo si hay un error
            error = target - output
            weights += eta * error * xi
            bias += eta * error
            total_error += abs(error)

        errors.append(total_error)
    
    return weights, bias, errors

# Entrenamos el Perceptrón
weights, bias, errors = perceptron(X, y)

# Mostramos los resultados
print(f"Pesos finales: {weights}")
print(f"Sesgo final: {bias}")

# Graficamos la evolución del error
plt.plot(errors)
plt.xlabel('Épocas')
plt.ylabel('Errores')
plt.title('Evolución del error en el entrenamiento')
plt.grid(True)
plt.show()
