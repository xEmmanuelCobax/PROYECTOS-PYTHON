import math

# Función que representa la velocidad del paracaidista en función de la masa
def velocidad_paracaidista(masa):
    g = 9.8
    c = 15
    t = 9
    v = 35
    return v - (g * masa / c) * (1 - math.exp(-c / masa * t))

# Implementación del método de la falsa posición utilizando ModFalsePos
def ModFalsePos(xl, xu, es, imax):
    iter = 0
    xr_old = 0
    
    while True:
        fl = velocidad_paracaidista(xl)
        fu = velocidad_paracaidista(xu)
        xr = xu - fu * (xl - xu) / (fl - fu)
        fr = velocidad_paracaidista(xr)
        iter += 1
        
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100
        else:
            ea = 0
        
        test = fl * fr
        
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
        else:
            ea = 0
        
        if ea < es or iter >= imax:
            break
        
        xr_old = xr
    
    return xr

# Llamada a la función de la falsa posición
xl = 1
xu = 100
es = 0.001
imax = 100
masa_aproximada = ModFalsePos(xl, xu, es, imax)

# Imprimir el resultado final
print(f"La masa aproximada es: {masa_aproximada:.8f} kg")
