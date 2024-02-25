def bisection_method(func, xl, xu, true_value, max_iter=50, tolerance=1e-5):
    """
    Método de la bisección para encontrar la raíz de una función.
    
    Parámetros:
        func (función): La función para la cual encontrar la raíz.
        xl (float): Límite inferior del intervalo inicial.
        xu (float): Límite superior del intervalo inicial.
        true_value (float): Valor verdadero de la raíz (para calcular el error porcentual).
        max_iter (int): Número máximo de iteraciones permitidas.
        tolerance (float): Tolerancia para la convergencia.
    
    Devuelve:
        result (dict): Diccionario con los resultados de la iteración.
    """
    result = {
        "xl": [],
        "xu": [],
        "xr": [],
        "f(xl)": [],
        "f(xu)": [],
        "f(xr)": [],
        "f(xl)*f(xr)": [],
        "ea": [],
        "ep": []
    }
    
    iter_count = 0
    xr = None
    ea = None
    ep = None
    
    while iter_count < max_iter:
        xr = (xl + xu) / 2.0
        f_xl = func(xl)
        f_xu = func(xu)
        f_xr = func(xr)
        f_xl_x_f_xu = f_xl * f_xu
        
        ea = abs((xr - xu) / xr) * 100 if xr != 0 else None
        ep = abs((true_value - xr) / true_value) * 100
        
        result["xl"].append(xl)
        result["xu"].append(xu)
        result["xr"].append(xr)
        result["f(xl)"].append(f_xl)
        result["f(xu)"].append(f_xu)
        result["f(xr)"].append(f_xr)
        result["f(xl)*f(xr)"].append(f_xl_x_f_xu)
        result["ea"].append(ea)
        result["ep"].append(ep)
        
        if ea and ea <= tolerance:
            break
        
        if f_xl_x_f_xu< 0:
            xu = xr
        elif f_xl_x_f_xu > 0:
            xl = xr
        else:
            ea = 0
            break
        
        iter_count += 1
    
    return result

def print_iteration_table(result):
    """
    Imprime una tabla con los resultados de cada iteración.
    
    Parámetros:
        result (dict): Diccionario con los resultados de la iteración.
    """
    headers = ["Iteración", "xl", "xu", "xr", "f(xl)", "f(xu)", "f(xr)", "f(xl)*f(xr)", "Error relativo porcentual (ea)", "Error porcentual (ep)"]
    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<35} {:<20}".format(*headers))
    
    for i in range(len(result["xl"])):
        values = [i+1, result["xl"][i], result["xu"][i], result["xr"][i], result["f(xl)"][i], result["f(xu)"][i],
                result["f(xr)"][i], result["f(xl)*f(xr)"][i], result["ea"][i], result["ep"][i]]
        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<35} {:<20}".format(*values))

# Ejemplo de uso:
def get_function():
    """
    Solicita al usuario ingresar una función en forma de cadena y la convierte en una función de Python.
    
    Devuelve:
        función: La función ingresada por el usuario.
    """
    import sympy as sp
    
    while True:
        try:
            expression = input("Ingrese la función (usando 'x' como variable): ")
            x = sp.symbols('x')
            func = sp.sympify(expression)
            return sp.lambdify(x, func, 'numpy')
        except (ValueError, SyntaxError):
            print("Función no válida. Inténtelo de nuevo.")

func = get_function()
xl = float(input("Ingrese el valor de xl: "))
xu = float(input("Ingrese el valor de xu: "))
true_value = float(input("Ingrese el valor verdadero de la raíz: "))

result = bisection_method(func, xl, xu, true_value)
print_iteration_table(result)
