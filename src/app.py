# Máquina de Turing con control de límites y manejo del último carácter
# Cinta inicial con 10 cifras
cinta = ['0', '0', '0', '0', '0', '1', '0', '1', '0', '0']  # Cinta de ejemplo
cabezal = 0  # El cabezal comienza en la posición inicial
estado = 'A'  # Estado inicial

def mostrar_cinta(cinta, cabezal):
    """Función para mostrar la cinta con el cabezal marcado."""
    print('Cinta:', ''.join(cinta))
    print('       ' + ' ' * cabezal + '^')  # Marca la posición del cabezal

# Función para ejecutar la máquina de Turing
def maquina_turing(cinta):
    global estado, cabezal
    paso = 0  # Contador de pasos

    # Mostrar el estado inicial
    print(f"Paso {paso} | Estado: {estado}")
    mostrar_cinta(cinta, cabezal)

    while estado != 'H':  # 'H' representa el estado de parada
        paso += 1

        # Validar que el cabezal esté dentro de los límites de la cinta
        if cabezal < 0:
            print("El cabezal alcanzó el límite izquierdo. Se queda en la posición 0.")
            cabezal = 0  # Fijar el cabezal al límite izquierdo
        elif cabezal >= len(cinta):
            print("El cabezal alcanzó el límite derecho. Se queda en la última posición.")
            cabezal = len(cinta) - 1  # Fijar el cabezal al límite derecho

        simbolo_actual = cinta[cabezal]

        # Transiciones según la tabla
        if estado == 'A':
            if simbolo_actual == '0':
                cinta[cabezal] = '1'
                cabezal += 1  # Mover a la derecha
                estado = 'B'
            elif simbolo_actual == '1':
                cinta[cabezal] = '1'
                cabezal += 1  # Mover a la derecha
                estado = 'B'
        elif estado == 'B':
            if simbolo_actual == '0':
                cinta[cabezal] = '1'
                cabezal -= 1  # Mover a la izquierda
                estado = 'C'
            elif simbolo_actual == '1':
                cinta[cabezal] = '1'
                cabezal -= 1  # Mover a la izquierda
                estado = 'C'
        elif estado == 'C':
            if simbolo_actual == '0':
                cinta[cabezal] = '0'  # Escribe 0
                cabezal -= 1  # Mover a la izquierda
                estado = 'C'  # Permanece en C
            elif simbolo_actual == '1':
                cinta[cabezal] = '0'  # Escribe 0
                cabezal -= 1  # Mover a la izquierda
                estado = 'D'  # Cambia al estado D
        elif estado == 'D':
            if simbolo_actual == '0':
                cinta[cabezal] = '1'
                cabezal += 1  # Mover a la derecha
                estado = 'E'
            elif simbolo_actual == '1':
                cinta[cabezal] = '1'
                cabezal += 1  # Mover a la derecha
                estado = 'E'
        elif estado == 'E':
            if simbolo_actual == '0':
                cinta[cabezal] = '0'
                cabezal += 1  # Mover a la derecha
                estado = 'E'
            elif simbolo_actual == '1':
                cinta[cabezal] = '0'
                cabezal += 1  # Mover a la derecha
                estado = 'F'
        elif estado == 'F':
            if simbolo_actual == '0':
                cinta[cabezal] = '1'
                cabezal -= 1  # Mover a la izquierda
                estado = 'C'
            elif simbolo_actual == '1':
                cinta[cabezal] = '1'
                cabezal -= 1  # Mover a la izquierda
                estado = 'C'

        # Mostrar el estado actual
        print(f"Paso {paso} | Estado: {estado}")
        mostrar_cinta(cinta, cabezal)

        # Condición de parada adicional (para evitar bucles infinitos en simulación)
        if paso > 100:  # Ajustar si se desea más o menos pasos
            print("Máximo de pasos alcanzado, deteniendo la simulación.")
            break

    # Final de la simulación
    print("Fin del programa. Cinta final:")
    mostrar_cinta(cinta, cabezal)

# Ejecutar la máquina
maquina_turing(cinta)
