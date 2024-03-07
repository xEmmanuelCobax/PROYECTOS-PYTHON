import math

# Definir la ecuación de la velocidad del paracaidista
def velocity_equation(m, t):
    g = 9.8
    c = 15
    return (g * m / c) * (1 - math.exp(-c / m * t))

# Implementar el método de la falsa posición
def false_position_method(func, x0, x1, es, max_iter=1000):
    result = {
        "xl": [],
        "xu": [],
        "xr": [],
        "f(xl)": [],
        "f(xr)": [],
        "f(xl)*f(xr)": [],
        "ea": [],
        "ep": []
    }
    
    iter_count = 0
    xr = x0
    ea = 100

    while ea > es and iter_count < max_iter:
        xrold = xr
        xr = x1 - func(x1) * (x0 - x1) / (func(x0) - func(x1))
        iter_count += 1
        result["xl"].append(x0)
        result["xu"].append(x1)
        result["xr"].append(xr)
        result["f(xl)"].append(func(x0))
        result["f(xr)"].append(func(xr))
        result["f(xl)*f(xr)"].append(func(x0) * func(xr))
        result["ea"].append(ea)
        
        if xr != 0:
            ea = abs((xr - xrold) / xr) * 100

        test = func(x0) * func(xr)
        if test < 0:
            x1 = xr
        elif test > 0:
            x0 = xr
        else:
            ea = 0

    return result

def print_iteration_table(result):
    headers = ["Iteración", "xl", "xu", "xr", "f(xl)", "f(xr)", "f(xl)*f(xr)", "Error relativo porcentual (ea)", "Error porcentual (ep)"]
    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<35} {:<20}".format(*headers))
    
    for i in range(len(result["xl"])):
        values = [i+1, result["xl"][i], result["xu"][i], result["xr"][i], result["f(xl)"][i], result["f(xr)"][i],
                result["f(xl)*f(xr)"][i], result["ea"][i], "-"]
        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<35.2e} {:<20}".format(*values))

# Definir los valores iniciales
x0 = 59  # Estimación inferior
x1 = 60  # Estimación superior
es = 0.1  # Nivel de error especificado (%)

# Calcular la masa utilizando el método de la falsa posición
result = false_position_method(lambda m: velocity_equation(m, 9) - 35, x0, x1, es / 100)

# Mostrar resultados en tabla por cada iteración
print_iteration_table(result)

# Mostrar resultados finales
print("\nResultados finales:")
print("Iteración final:", len(result["xl"]))
print("Masa (m):", result["xr"][-1])
print("Error aproximado (%):", result["ea"][-1])
