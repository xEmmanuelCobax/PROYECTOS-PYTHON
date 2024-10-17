def hamming(bits):
    """Genera un código Hamming para una cadena de bits dada."""

    # bits es una cadena de '0' y '1'
    n = len(bits)
    r = 0
    # Encuentra el número de bits de paridad necesarios
    while (2**r) < (n + r + 1):
        r += 1

    # Inicializa el código Hamming con ceros
    hamming_code = list("0" * (n + r))
    j = 0

    # Coloca los bits de datos en sus posiciones correctas
    for i in range(1, n + r + 1):
        if (i & (i - 1)) != 0:  # i es potencia de 2, reservar para bits de paridad
            hamming_code[i - 1] = bits[j]
            j += 1

    # Calcula los bits de paridad
    for i in range(r):
        parity_bit = 2**i
        count = 0
        for j in range(parity_bit - 1, n + r, 2 * parity_bit):
            count += sum(map(int, hamming_code[j : j + parity_bit]))
        hamming_code[parity_bit - 1] = str(count % 2)

    return "".join(hamming_code)


def get_user_input():
    """Solicita al usuario que ingrese una cadena válida de bits."""

    while True:
        data = input("Por favor, ingrese una cadena de bits (solo '0' y '1'): ")
        if all(bit in "01" for bit in data) and len(data) > 0:
            return data
        else:
            print("Entrada no válida. Asegúrese de ingresar solo '0' y '1'.")


# Ejecución del programa
if __name__ == "__main__":
    user_data = get_user_input()
    hamming_code = hamming(user_data)
    print(f"El código Hamming para los datos {user_data} es {hamming_code}")
