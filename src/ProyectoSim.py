import tkinter as tk
import random

# Configuración inicial
GRID_SIZE = 50  # Tamaño de la cuadrícula
CELL_SIZE = 10  # Tamaño de cada célula
PROB_CONTAGIO = 0.2  # Probabilidad de contagio inicial
DISTANCIA_CONTAGIO = 1  # Distancia de contagio inicial
RESISTENCIA_FRIO = 0.5  # Resistencia al frío
RESISTENCIA_CALOR = 0.5  # Resistencia al calor

# Colores para las células
COLOR_VACIA = 'white'
COLOR_INFECTADA = 'red'

# Crear la ventana principal
root = tk.Tk()
root.title("Simulación de Expansión de Virus")

canvas = tk.Canvas(root, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE)
canvas.pack()

# Crear la cuadrícula inicial
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Variables de control
virus_list = []
running = False

def inicializar_grid():
    global virus_list
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            grid[i][j] = 0

def dibujar_grid():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = COLOR_INFECTADA if grid[i][j] == 1 else COLOR_VACIA
            canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill=color, outline='gray')

def agregar_virus(event):
    global virus_list
    x = event.x // CELL_SIZE
    y = event.y // CELL_SIZE
    virus_list.append((x, y))
    grid[y][x] = 1

def contagiar():
    nuevas_infecciones = []
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 1:  # Si la célula está infectada
                for di in range(-DISTANCIA_CONTAGIO, DISTANCIA_CONTAGIO+1):
                    for dj in range(-DISTANCIA_CONTAGIO, DISTANCIA_CONTAGIO+1):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < GRID_SIZE and 0 <= nj < GRID_SIZE:
                            if grid[ni][nj] == 0 and random.random() < PROB_CONTAGIO:
                                nuevas_infecciones.append((ni, nj))
    for ni, nj in nuevas_infecciones:
        grid[ni][nj] = 1

def actualizar():
    if running:
        contagiar()
        canvas.delete("all")
        dibujar_grid()
    root.after(100, actualizar)  # Actualizar cada 100 ms (0.1 segundos)

def toggle_simulacion():
    global running
    running = not running

def limpiar():
    global virus_list
    virus_list = []
    inicializar_grid()
    canvas.delete("all")
    dibujar_grid()

def actualizar_probabilidad(valor):
    global PROB_CONTAGIO
    PROB_CONTAGIO = float(valor)

def actualizar_distancia(valor):
    global DISTANCIA_CONTAGIO
    DISTANCIA_CONTAGIO = int(valor)

def actualizar_resistencia_frio(valor):
    global RESISTENCIA_FRIO
    RESISTENCIA_FRIO = float(valor)

def actualizar_resistencia_calor(valor):
    global RESISTENCIA_CALOR
    RESISTENCIA_CALOR = float(valor)

# Crear controles y botones
tk.Button(root, text="Toggle Simulación", command=toggle_simulacion).pack()
tk.Button(root, text="Limpiar", command=limpiar).pack()

probabilidad_label = tk.Label(root, text="Probabilidad de Contagio:")
probabilidad_label.pack()
probabilidad_entry = tk.Entry(root)
probabilidad_entry.pack()
probabilidad_entry.insert(tk.END, str(PROB_CONTAGIO))
probabilidad_entry.bind('<Return>', lambda event: actualizar_probabilidad(probabilidad_entry.get()))

distancia_label = tk.Label(root, text="Distancia de Contagio:")
distancia_label.pack()
distancia_entry = tk.Entry(root)
distancia_entry.pack()
distancia_entry.insert(tk.END, str(DISTANCIA_CONTAGIO))
distancia_entry.bind('<Return>', lambda event: actualizar_distancia(distancia_entry.get()))

resistencia_frio_label = tk.Label(root, text="Resistencia al Frío:")
resistencia_frio_label.pack()
resistencia_frio_entry = tk.Entry(root)
resistencia_frio_entry.pack()
resistencia_frio_entry.insert(tk.END, str(RESISTENCIA_FRIO))
resistencia_frio_entry.bind('<Return>', lambda event: actualizar_resistencia_frio(resistencia_frio_entry.get()))

resistencia_calor_label = tk.Label(root, text="Resistencia al Calor:")
resistencia_calor_label.pack()
resistencia_calor_entry = tk.Entry(root)
resistencia_calor_entry.pack()
resistencia_calor_entry.insert(tk.END, str(RESISTENCIA_CALOR))
resistencia_calor_entry.bind('<Return>', lambda event: actualizar_resistencia_calor(resistencia_calor_entry.get()))

canvas.bind('<Button-1>', agregar_virus)

# Inicializar y comenzar la simulación
inicializar_grid()
dibujar_grid()
actualizar()
root.mainloop()
