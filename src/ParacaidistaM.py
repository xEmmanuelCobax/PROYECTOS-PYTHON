import numpy as np
import matplotlib.pyplot as plt

g = 9.8
c = float(input("Ingrese el valor de resistencia: "))
v = float(input("Ingrese el valor de velocidad máxima: "))

# Cálculo de la masa
m = c / (g * (1 - np.exp(-c/v)))

print("La masa calculada es:", m)

# Graficar
t = np.arange(0, 50, 0.5)
m_values = c / (g * (1 - np.exp(-c/v*t)))

plt.plot(t, m_values, color="blue")  # Cambio de variable a m_values
plt.grid(True)
plt.xlabel("t")
plt.ylabel("m")  # Cambio de etiqueta a "m"
plt.title("m = c / (g * (1 - np.exp(-c/v*t)))")  # Cambio de título
plt.show()
