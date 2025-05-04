# Subasta de Vickrey con 3 jugadores

# Ofertas de los jugadores
ofertas = [50, 70, 60]  # Las ofertas hechas por los jugadores

# Determinamos el ganador y el precio a pagar (el segundo precio más alto)
def subasta_vickrey(ofertas):
    # Ordenamos las ofertas de mayor a menor
    ofertas_ordenadas = sorted(ofertas, reverse=True)
    
    # El ganador es el jugador con la oferta más alta
    ganador = ofertas.index(ofertas_ordenadas[0])
    
    # El precio a pagar es el segundo precio más alto
    precio_a_pagar = ofertas_ordenadas[1]
    
    return ganador, precio_a_pagar

# Ejecutamos la subasta
ganador, precio = subasta_vickrey(ofertas)
print(f"El ganador es el jugador {ganador + 1}, que paga ${precio}.")
