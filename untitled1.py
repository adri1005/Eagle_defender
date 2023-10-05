import tkinter as tk

# Tamaño del mapa
mapa_ancho = 1500
mapa_alto = 2000

# Tamaño de cada cuadrado imaginario
cuadrado_lado = 65.5

# Inicialización de cuadrados
cuadrados_libres = set()

# Crear ventana
ventana = tk.Tk()
ventana.title("Mapa Cuadriculado")

# Crear lienzo
canvas = tk.Canvas(ventana, width=mapa_ancho, height=mapa_alto)
canvas.pack()

def crear_cuadricula():
    pass

cuadrados_ocupados = []

def colocar_bloque(event):
    x, y = event.x, event.y
    cuadro_x = x // cuadrado_lado * cuadrado_lado
    cuadro_y = y // cuadrado_lado * cuadrado_lado
    print(f"Clic en X={x}, Y={y}, Cuadro en X={cuadro_x}, Y={cuadro_y}")
    if (cuadro_x, cuadro_y) not in cuadrados_ocupados:
        bloque = canvas.create_rectangle(cuadro_x, cuadro_y, cuadro_x + cuadrado_lado, cuadro_y + cuadrado_lado, fill="red")
        cuadrados_ocupados.append((cuadro_x, cuadro_y))
        ventana.update_idletasks()  # Actualizar la ventana
    else:
        print ("dddddd")

crear_cuadricula()
canvas.bind("<Button-1>", colocar_bloque)

ventana.mainloop()
