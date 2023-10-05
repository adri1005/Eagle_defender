from tkinter import *
import sqlite3
from tkinter import filedialog
import shutil
global users
users = 0
import tkinter as tk
from pydub import AudioSegment
import sutil
from mutagen.mp3 import MP3

MAX_DURACION = 5 * 60 * 1000  # Duración máxima en milisegundos (5 minutos)

MAX_DURACION = 5 * 60  # Duración máxima en segundos (5 minutos)

def cargar_cancion():
    ruta_archivo = filedialog.askopenfilename()
    if ruta_archivo:
        duracion = obtener_duracion_mp3(ruta_archivo)
        if duracion is not None and duracion <= MAX_DURACION:
            guardar_cancion(ruta_archivo, 'Canciones')
        elif duracion is not None:
            messagebox.showerror("ERROR", "La canción debe de durar menos de cinco minutos")

def obtener_duracion_mp3(ruta_archivo):
    try:
        mp3 = MP3(ruta_archivo)
        duracion = mp3.info.length  # Duración en segundos
        return duracion
    except Exception as e:
        print(f"Error al obtener la duración de la canción: {str(e)}")
        return None

def guardar_cancion(ruta_archivo, destino):
    try:
        # Copiar el archivo original a la ubicación de destino
        shutil.copy(ruta_archivo, destino)
        print("Canción guardada exitosamente.")
    except Exception as e:
        print(f"Error al guardar la canción: {str(e)}")

        
def mostrar_error(users):
    if users == 2:
        ventana_principal()
    else:
        pass
    
def login():
    def login_database():
        global users        
        conn = sqlite3.connect("2.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM test WHERE email=? AND password=?", (e1.get(), e2.get()))
        row = cur.fetchall()
        conn.close()
        print(row)
        if row != []:
            user_name = row[0][1]
            l3.config(text="Usuario encontrado con nombre: " + user_name)
            login_window.destroy()  # Destroy the login_window when done
            users +=1
            mostrar_error(users)
        else:
            l3.config(text="Usuario no encontrado")

    login_window = Tk()
    login_window.geometry("400x250")
    l1 = Label(login_window, text="Email", font="times 20")
    l1.grid(row=1, column=1)
    l2 = Label(login_window, text="Contraseña", font="times 20")
    l2.grid(row=2, column=1)
    l3 = Label(login_window, font="times 20")
    l3.grid(row=5, column=2)

    email_text = StringVar()
    e1 = Entry(login_window, textvariable=email_text)
    e1.grid(row=1, column=2)
    password_text = StringVar()
    e2 = Entry(login_window, textvariable=password_text)
    e2.grid(row=2, column=2)

    b1 = Button(login_window, text="Iniciar sesión", width=20, command=login_database)
    b1.grid(row=4, column=2)

    login_window.mainloop()

def signup():
    def signup_database():
        global users
        conn = sqlite3.connect("2.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, name text, email text, password text, birth text)")
        cur.execute("INSERT INTO test VALUES(NULL,?,?,?,?)", (e1.get(), e2.get(), e3.get(), e4.get()))
        l4 = Label(signup_window, text="Cuenta creada", font="times 15")
        l4.grid(row=6, column=2)
        conn.commit()
        conn.close()
        mostrar_error(users)
        users +=1
        mostrar_error(users)

    signup_window = Tk()
    signup_window.geometry("400x250")
    l1 = Label(signup_window, text="Nombre de usuario", font="times 20")
    l1.grid(row=1, column=1)
    l2 = Label(signup_window, text="Email", font="times 20")
    l2.grid(row=2, column=1)
    l3 = Label(signup_window, text="Contraseña", font="times 20")
    l3.grid(row=3, column=1)
    l4 = Label(signup_window, text="Fecha de nacimiento", font="times 20")
    l4.grid(row=4, column=1)

    name_text = StringVar()
    e1 = Entry(signup_window, textvariable=name_text)
    e1.grid(row=1, column=2)
    email_text = StringVar()
    e2 = Entry(signup_window, textvariable=email_text)
    e2.grid(row=2, column=2)
    password_text = StringVar()
    e3 = Entry(signup_window, textvariable=password_text)
    e3.grid(row=3, column=2)
    birth_text = StringVar()
    e4 = Entry(signup_window, textvariable=birth_text)
    e4.grid(row=4, column=2)

    b1 = Button(signup_window, text="Iniciar sesión", width=20, command=signup_database)
    b1.grid(row=5, column=2)

    signup_window.mainloop()

window = Tk()
window.geometry("300x150")

l1 = Label(window, text="Qué desea hacer?", font="times 20")
l1.grid(row=1, column=2, columnspan=2)

b1 = Button(window, text="Iniciar sesión", width=20, command=login)
b1.grid(row=2, column=2)

b2 = Button(window, text="Registrarse", width=20, command=signup)
b2.grid(row=2, column=3)

btn_cargar = tk.Button(window, text="Cargar Canción", command=cargar_cancion)
btn_cargar.grid(row=3, column=2)

def ventana_principal():
    global window

    window = Tk()
    window.geometry("900x700")
    window.resizable(width=False,height=False )
    canva1=Canvas(window, width= 900, height= 700)
    canva1.pack()

    Tanque=PhotoImage(file="Tanque.png")
    Tanque_etiqueta=canva1.create_image(450,400,image=Tanque)




    playbtn = Button(width=15,height=3,text="PLAY",command=openplayscreen)
    playbtn.place(x=400,y=100)
    window.mainloop()
    



def gamewindow():
    
    # Tamaño del mapa
    mapa_ancho = 1200
    mapa_alto = 1500

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
    woodenblock = PhotoImage(file="woodenblock.png")
    Tanque=PhotoImage(file="FONDO.png")
    Tanque_etiqueta=canvas.create_image(450,400,image=Tanque)

    def crear_cuadricula():
        pass

    cuadrados_ocupados = []

    def colocar_bloque(event):
        
        x, y = event.x, event.y
        cuadro_x = x // cuadrado_lado * cuadrado_lado
        cuadro_y = y // cuadrado_lado * cuadrado_lado
        print(f"Clic en X={x}, Y={y}, Cuadro en X={cuadro_x}, Y={cuadro_y}")
        if (cuadro_x, cuadro_y) not in cuadrados_ocupados:
            canvas.create_image(cuadro_x, cuadro_y, anchor=tk.NW, image=woodenblock)
            cuadrados_ocupados.append((cuadro_x, cuadro_y))
            ventana.update_idletasks()  # Actualizar la ventana
        else:
            print ("ocupado")

    crear_cuadricula()
    canvas.bind("<Button-1>", colocar_bloque)

    ventana.mainloop()


def openplayscreen():
    global window
    window.destroy()
    gamewindow()


window.mainloop()



