def Menu(str1, str2, a, b):
    flag = True
    while flag:
        try:
            aux = int(input(f"{str1}\nIngrese {str2}: "))
            if aux < a or aux > b:
                    raise ValueError("No ingresaste un número dentro del rango.")
            else:
                flag = False   
                break
        except ValueError:
                print("El error es: No ingresaste un número")
    return aux


def cuadrados_medios(semilla,num):
    print(f"{'Iteración':<10}{'x1':<10}")
    tam1 = len(semilla)
    numero1 = int(semilla)
    for i in range(num):
        numero2 = numero1**2
        snumero2 = str(numero2)
        tam2 = len(snumero2)
        primerc = int((tam2 - tam1) / 2)
        snumero3 = snumero2[primerc:primerc+tam1]
        print(
            f"{i + 1:<10}{numero1:<10}{int(snumero3)/10000:<10}")
        numero1 = int(snumero3)

def productos_medios(iteraciones, semilla1, semilla2):
    resultados = []
    for i in range(iteraciones):
        semilla = semilla1 * semilla2
        semilla_str = str(semilla)
        mitad = len(semilla_str) // 2
        nueva_semilla = semilla_str[mitad-2:mitad+2]
        ri = int(nueva_semilla) / 10000
        resultados.append([i+1, semilla1, semilla2, semilla, nueva_semilla, round(ri, 4)])
        semilla1 = semilla2
        semilla2 = int(nueva_semilla)
    return resultados

def imprimir_tabla(resultados):
    print("Interacción | Semilla 1 | Semilla 2 | Semilla | Nueva Semilla | Ri")
    print("-" * 68)
    for fila in resultados:
        print("{:^12} | {:^9} | {:^9} | {:^7} | {:^14} | {:^6}".format(*fila))
        

def multiplicador_constante(semilla, constante, num_iteraciones):
    # Encabezado de la tabla
    print(f"{'Iteración':<10}{'Constante':<10}{'Semilla':<10}{'Resultado Semilla':<20}{'xn+1':<10}{'ri':<15}")

    # Iterar y mostrar resultados en la tabla
    for i in range(num_iteraciones):
        # Generar número aleatorio
        resultado_semilla = semilla * constante

        # Convertir a cadena y obtener los 4 dígitos de en medio
        resultado_semilla_str = str(resultado_semilla)
        xn_1 = resultado_semilla_str[(
            len(resultado_semilla_str) // 2) - 2: (len(resultado_semilla_str) // 2) + 2]

        # Calcular ri dividiendo xn+1 entre 10000
        ri = int(xn_1) / 10000.0

        # Mostrar resultados en la tabla
        print(
            f"{i + 1:<10}{constante:<10}{semilla:<10}{resultado_semilla:<20}{xn_1:<10}{ri:<15}")

        # Actualizar semilla para la siguiente iteración
        semilla = int(xn_1)
class GeneradorCongruencialLineal:
    def _init_(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.current_value = seed
        self.valores_generados = []

    def generar_siguiente(self):
        self.current_value = (self.a * self.current_value + self.c) % self.m
        self.valores_generados.append(self.current_value)
        return self.current_value

    def tiempo_de_vida(self, valor):
        if valor not in self.valores_generados:
            return -1  # El valor no se repite, no tiene tiempo de vida
        primera_aparicion = self.valores_generados.index(valor)
        ultima_aparicion = len(self.valores_generados) - 1
        return ultima_aparicion - primera_aparicion + 1


def Congruencial_Lineal(semilla, cmultiplicativa,caditiva, modulo, num_iteraciones): 
    print(f"{'Iteración':<10}{'x':<15}{'x / (m - 1)':<20}")
    iteraciones = {}
    for i in range(num_iteraciones):  
        if semilla in iteraciones:
            print(f"Repetición detectada en la iteración {i + 1}. Terminando generación.")
            break
        iteraciones[semilla] = i
        numero = (cmultiplicativa * semilla + caditiva) % modulo
        numero2 = numero / (modulo - 1)
        print(f"{i + 1:<10}{numero:<15}{numero2:<20}")
        semilla = numero
        
def Congruencial_Multiplicativo(semilla, cmultiplicativa, modulo, num_iteraciones): 
    print(f"{'Iteración':<10}{'x':<15}{'x / (m - 1)':<20}")
    iteraciones = {}
    for i in range(num_iteraciones):  
        if semilla in iteraciones:
            print(f"Repetición detectada en la iteración {i + 1}. Terminando generación.")
            break
        iteraciones[semilla] = i
        numero = (cmultiplicativa * semilla) % modulo
        numero2 = numero / (modulo - 1)
        print(f"{i + 1:<10}{numero:<15}{numero2:<20}")
        semilla = numero
        
def Congruencial_Aditivo(secuencia, modulo, num_iteraciones):
    n = len(secuencia)
    print(f"{'Iteración':<10}{'xi':<10}{'ri':<10}")
    
    for i in range(n, n + num_iteraciones):
        xi = (secuencia[i - 1] + secuencia[i - n]) % modulo
        ri = xi / (modulo - 1)
        print(f"{i + 1:<10}{xi:<10}{ri:<10}")
        secuencia.append(xi)


if __name__ == "__main__": 
    decicion = Menu("\t\t\tMENU PRINCIPAL\nIngrese el número de lo que quiere realizar\n1-Método de los cuadrados medios\n2-Método de los productos medios\n3-Método del multiplicador constante\n4-Algoritmo Congruencial Mixto (lineal)\n5-Algoritmo Congruencial Multiplicativo\n6-Algoritmo Congruencial Aditivo","un numero dentro del rango", 1, 6)
    if decicion == 1:
        semilla = input("Escriba semilla: ")
        it = int(input("Escriba las iteraciones: "))
        cuadrados_medios (semilla,it)
    elif decicion == 2:
        iteraciones = int(input("Ingrese el número de iteraciones: "))
        semilla1 = int(input("Ingrese la semilla 1: "))
        semilla2 = int(input("Ingrese la semilla 2: "))
        resultados = productos_medios(iteraciones, semilla1, semilla2)
        imprimir_tabla(resultados)
    elif decicion == 3:
        semilla = int(input("Ingrese la semilla: "))
        constante = int(input("Ingrese la constante: "))
        num_iteraciones = int(input("Ingrese el número de iteraciones:"))
        multiplicador_constante(semilla, constante, num_iteraciones)
    elif decicion == 4:
        semilla = int(input("Escriba una semilla: "))
        cmultiplicativa = int(input("Escriba una constante multiplicativa: "))
        caditiva = int(input("Escriba una constante aditiva: "))
        modulo = int(input("Escriba el módulo: "))
        num_iteraciones = int(input("Ingrese el número de iteraciones:"))
        Congruencial_Lineal(semilla,cmultiplicativa,caditiva,modulo,num_iteraciones)
    elif decicion == 5:
        semilla = int(input("Escriba una semilla: "))
        cmultiplicativa = int(input("Escriba una constante multiplicativa: "))
        modulo = int(input("Escriba el módulo: "))
        num_iteraciones = int(input("Ingrese el número de iteraciones:"))
        Congruencial_Multiplicativo(semilla,cmultiplicativa,modulo,num_iteraciones)
    elif decicion == 6:
        secuencia = []
        numero = int(input("Escriba el número de semillas (Secuencia): "))
        for i in range(numero):
            num = int(input(f"Escriba el número {i + 1}: "))
            secuencia.append(num)

        modulo = int(input("Escriba el valor del módulo: "))
        num_iteraciones = int(input("Escriba el número de iteraciones adicionales: "))

        Congruencial_Aditivo(secuencia, modulo, num_iteraciones)
    else:
        print("Error: No eligio un numero dentro del rango")#uWU, no we