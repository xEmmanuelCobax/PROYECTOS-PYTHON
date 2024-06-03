def gauss_seidel(A, b, x0, tol, max_iter):
    n = len(A)
    x = x0.copy()
    iteraciones = [x.copy()]
    dif = tol + 1
    k = 0
    
    while dif > tol and k < max_iter:
        x_ant = x.copy()
        for i in range(n):
            suma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - suma) / A[i][i]
        
        errores_relativos = [abs((x[i] - x_ant[i]) / x[i]) for i in range(n) if x[i] != 0]
        if not errores_relativos:
            break
        
        dif = max(errores_relativos)
        iteraciones.append(x.copy())
        k += 1
        
    return x, iteraciones

def es_diagonalmente_dominante(A):
    n = len(A)
    for i in range(n):
        suma = sum(abs(A[i][j]) for j in range(n) if j != i)
        if abs(A[i][i]) <= suma:
            return False
    return True

def hacer_diagonalmente_dominante(A, b):
    n = len(A)
    for i in range(n):
        max_val = abs(A[i][i])
        max_index = i
        for j in range(i+1, n):
            if abs(A[j][i]) > max_val:
                max_val = abs(A[j][i])
                max_index = j
        if max_index != i:
            # Intercambiar filas
            A[i], A[max_index] = A[max_index], A[i]
            b[i], b[max_index] = b[max_index], b[i]

# Elección del tamaño del sistema
tamano_sistema = int(input("Ingrese el tamaño del sistema (2 o 3): "))
if tamano_sistema not in [2, 3]:
    print("Tamaño de sistema no válido. Debe ser 2 o 3.")
else:
    A = []
    b = []
    
    print(f"Ingrese las ecuaciones del sistema de tamaño {tamano_sistema}x{tamano_sistema}:")
    for i in range(tamano_sistema):
        coeficientes_str = input(f"Coeficientes de la ecuación {i+1} (sin el término independiente, separados por espacios): ")
        independiente_str = input(f"Término independiente de la ecuación {i+1}: ")
        coeficientes = list(map(int, coeficientes_str.split()))
        termino_independiente = int(independiente_str)
        A.append(coeficientes)
        b.append(termino_independiente)
    
    # Verificar si la matriz es diagonalmente dominante
    if not es_diagonalmente_dominante(A):
        print("La matriz no es diagonalmente dominante. Haciendo los cambios necesarios...")
        hacer_diagonalmente_dominante(A, b)
        print("La matriz ha sido modificada para ser diagonalmente dominante.")
        print("Nueva matriz:")
        for fila in A:
            print(fila)
        print("Nuevos términos independientes:")
        print(b)
    
    # Continuar con el método Gauss-Seidel
    x0 = []
    print("Ingrese la aproximación inicial (x0) separando los valores con espacios:")
    aproximacion = input().split()
    for valor in aproximacion:
        x0.append(float(valor))
    
    tolerancia = float(input("Ingrese la tolerancia para el método: "))
    max_iteraciones = int(input("Ingrese el número máximo de iteraciones: "))

    solucion, iteraciones = gauss_seidel(A, b, x0, tolerancia, max_iteraciones)

    # Mostrar iteraciones en forma de tabla
    print("\nIteraciones:")
    print("k\t", end="")
    for i in range(tamano_sistema):
        print(f"x{i+1}\t", end="")
    print()
    for k, iteracion in enumerate(iteraciones):
        print(f"{k}\t", end="")
        for valor in iteracion:
            print(f"{valor:.4f}\t", end="")
        print()

    print("\nSolución final:")
    for i in range(tamano_sistema):
        print(f"x{i+1} = {solucion[i]:.4f}")
