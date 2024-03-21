import numpy as np

def funcion(x):
    return 2 * (x**2) - 10*x + 4

def derivada_funcion(x):
    return 4*x-10

def newton_raphson(func, derivada, x0, tolerancia, max_iter, valor_verdadero):
    iteracion = 0
    errores_porcentuales = []
    errores_aproximados = []
    while iteracion < max_iter:
        x1 = x0 - func(x0) / derivada(x0)
        error_porcentual = abs((x1 - valor_verdadero) / valor_verdadero) * 100
        error_aproximado = abs(((x1 - x0) / x1)*100)
        
        errores_porcentuales.append(error_porcentual)
        errores_aproximados.append(error_aproximado)
        
        print("{:<10} {:<25} {:<25} {:<25} {:<25}".format(iteracion, format(x0, '.15f'), format(x1, '.15f'), format(error_porcentual, '.15f'), format(error_aproximado, '.15f')))
        
        if error_aproximado < tolerancia:
            return x1, iteracion, errores_porcentuales, errores_aproximados
        
        x0 = x1
        iteracion += 1
    
    return None, iteracion, errores_porcentuales, errores_aproximados

# Parámetros para el método de Newton-Raphson y valor verdadero
tolerancia = float(input("Ingrese la tolerancia (es): "))
valor_verdadero = float(input("Ingrese el valor verdadero de la raíz: "))
x0 = float(input("Ingrese el valor inicial (x0): "))

print("{:<10} {:<25} {:<25} {:<25} {:<25}".format("Iteración", "x", "Raíz Aproximada", "Error Porcentual", "Error Aproximado"))
raiz_aprox, num_iter, errores_porcentuales, errores_aproximados = newton_raphson(funcion, derivada_funcion, x0, tolerancia, 1000, valor_verdadero)

if raiz_aprox is not None:
    print(f"\nRaíz aproximada: {format(raiz_aprox, '.15f')}")
    print(f"Iteraciones realizadas: {num_iter}")
else:
    print("El método de Newton-Raphson no converge.")
