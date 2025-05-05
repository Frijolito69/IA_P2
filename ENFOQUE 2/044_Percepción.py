# Simulación de lectura de un sensor de proximidad
def leer_sensor_distancia():
    # Imaginemos que mide distancia en centímetros
    # (por ahora ponemos un valor fijo o aleatorio si quieres hacerlo dinámico)
    return 15  # 15 cm, por ejemplo

# Función de percepción y acción
def decidir_movimiento(distancia):
    if distancia < 20:
        return "¡Detente! Objeto demasiado cerca."
    else:
        return "Todo despejado, puedes avanzar."

# Simulación del ciclo de percepción
distancia_detectada = leer_sensor_distancia()
decision = decidir_movimiento(distancia_detectada)

print(f"Distancia detectada: {distancia_detectada} cm")
print(decision)
