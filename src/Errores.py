import pandas as pd
from math import exp, factorial

# Definir la función para calcular el término de la serie de Maclaurin
def termino_maclaurin(x, n):
    return x**n / factorial(n)

# Definir la función para calcular el valor aproximado de e^x utilizando la serie de Maclaurin
def aproximacion_e(x, n):
    return sum(termino_maclaurin(x, i) for i in range(n))

# Valor verdadero de e^0.3
e_verdadero = exp(0.3)

# Definir el valor de x y el número de términos en la serie de Maclaurin
x = 0.3
num_terminos = 5

# Crear una lista para almacenar los datos de la tabla
data = []

# Calcular y agregar cada término a la lista de datos
for i in range(1, num_terminos + 1):  # Comenzar desde 1
    valor_aproximado = aproximacion_e(x, i)
    error_porcentual = abs((valor_aproximado - e_verdadero) / e_verdadero) * 100
    if i == 1:
        error_aproximado = None  # No hay valor aproximado anterior en la primera iteración
    else:
        error_aproximado = abs((data[i-2]["Valor Aproximado"] - valor_aproximado) / valor_aproximado * 100)  # Ajustar el índice
    data.append({"Término": i, "Valor Aproximado": valor_aproximado, 
                "Error Porcentual": error_porcentual, "Error Aproximado": error_aproximado})

# Crear el DataFrame a partir de la lista de datos
tabla = pd.DataFrame(data)

# Mostrar la tabla
print(tabla)