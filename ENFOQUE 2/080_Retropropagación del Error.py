import random
import math

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Derivada de la función sigmoide
def sigmoid_derivative(x):
    return x * (1 - x)

# Función para inicializar pesos aleatorios
def initialize_weights(input_size, hidden_size, output_size):
    weights_input_hidden = [[random.uniform(-1, 1) for _ in range(hidden_size)] for _ in range(input_size)]  # Pesos de la capa de entrada a la capa oculta
    weights_hidden_output = [random.uniform(-1, 1) for _ in range(hidden_size)]  # Pesos de la capa oculta a la capa de salida
    return weights_input_hidden, weights_hidden_output

# Propagación hacia adelante
def forward_propagate(inputs, weights_input_hidden, weights_hidden_output):
    # Calcular las activaciones de la capa oculta
    hidden_layer_input = [sum([inputs[i] * weights_input_hidden[i][j] for i in range(len(inputs))]) for j in range(len(weights_input_hidden[0]))]
    hidden_layer_output = [sigmoid(x) for x in hidden_layer_input]  # Aplicar sigmoide a cada valor de la capa oculta
    
    # Calcular la salida
    output_layer_input = sum([hidden_layer_output[j] * weights_hidden_output[j] for j in range(len(hidden_layer_output))])
    output_layer_output = sigmoid(output_layer_input)  # Aplicar sigmoide a la salida
    
    return hidden_layer_output, output_layer_output

# Retropropagación
def backpropagate(inputs, hidden_layer_output, output_layer_output, y, weights_input_hidden, weights_hidden_output, learning_rate=0.1):
    # Cálculo del error en la salida
    output_error = y - output_layer_output
    output_delta = output_error * sigmoid_derivative(output_layer_output)  # Derivada para el ajuste de pesos
    
    # Propagar el error hacia atrás en la capa oculta
    hidden_error = [output_delta * weights_hidden_output[j] for j in range(len(weights_hidden_output))]
    hidden_delta = [hidden_error[j] * sigmoid_derivative(hidden_layer_output[j]) for j in range(len(hidden_layer_output))]
    
    # Actualizar los pesos
    for i in range(len(inputs)):
        for j in range(len(hidden_layer_output)):
            weights_input_hidden[i][j] += inputs[i] * hidden_delta[j] * learning_rate  # Actualización de los pesos de la capa de entrada a la capa oculta
    
    for j in range(len(hidden_layer_output)):
        weights_hidden_output[j] += hidden_layer_output[j] * output_delta * learning_rate  # Actualización de los pesos de la capa oculta a la capa de salida
    
    return weights_input_hidden, weights_hidden_output

# Función principal para entrenar la red
def train_network(X, y, input_size, hidden_size, output_size, epochs=10000, learning_rate=0.1):
    # Inicialización de pesos
    weights_input_hidden, weights_hidden_output = initialize_weights(input_size, hidden_size, output_size)
    
    # Entrenamiento
    for epoch in range(epochs):
        for i in range(len(X)):  # Iterar sobre cada entrada
            inputs = X[i]
            target = y[i]
            
            # Propagación hacia adelante
            hidden_layer_output, output_layer_output = forward_propagate(inputs, weights_input_hidden, weights_hidden_output)
            
            # Retropropagación y actualización de pesos
            weights_input_hidden, weights_hidden_output = backpropagate(inputs, hidden_layer_output, output_layer_output, target, weights_input_hidden, weights_hidden_output, learning_rate)
        
        # Mostrar el error cada 1000 épocas
        if epoch % 1000 == 0:
            error = 0
            for i in range(len(X)):
                _, output_layer_output = forward_propagate(X[i], weights_input_hidden, weights_hidden_output)
                error += sum([(y[i][j] - output_layer_output) ** 2 for j in range(len(y[i]))])  # Error cuadrático medio
            print(f"Época {epoch}, Error: {error}")
    
    return weights_input_hidden, weights_hidden_output

# Función para hacer predicciones
def predict(inputs, weights_input_hidden, weights_hidden_output):
    _, output_layer_output = forward_propagate(inputs, weights_input_hidden, weights_hidden_output)
    return output_layer_output
# Datos de entrada (X) y etiquetas (y)
X = [[0, 0], [0, 1], [1, 0], [1, 1]]  # Entradas (pueden representar datos binarios)
y = [[0], [1], [1], [0]]  # Etiquetas (función XOR)

# Parámetros
input_size = 2  # Número de entradas
hidden_size = 4  # Número de neuronas en la capa oculta
output_size = 1  # Número de salidas (clasificación binaria)

# Entrenar la red neuronal
weights_input_hidden, weights_hidden_output = train_network(X, y, input_size, hidden_size, output_size, epochs=10000, learning_rate=0.1)

# Predicción con nuevas entradas
print("\nPredicciones finales:")
for input_data in X:
    output = predict(input_data, weights_input_hidden, weights_hidden_output)
    print(f"Entrada: {input_data} -> Predicción: {output}")
