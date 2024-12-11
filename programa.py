import pygame
import tkinter as tk
from tkinter import Button

# Inicializar el mezclador de audio de pygame
pygame.mixer.init()

# Función para reproducir el audio correspondiente a la letra presionada
def reproducir_audio(letra):
    try:
        # Cargar el archivo de audio asociado a la letra
        pygame.mixer.music.load(f"audios/{letra}_1.mp3")
        pygame.mixer.music.play()  # Reproducir el audio
    except Exception as e:
        print(f"Error al reproducir el audio de la letra {letra}: {e}")

# Crear la interfaz gráfica
def crear_interfaz():
    root = tk.Tk()
    root.title("Glosario Interactivo")
    root.geometry("600x200")

    # Crear botones para cada letra del abecedario
    for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        button = Button(
            root, 
            text=letra, 
            width=5, 
            height=2, 
            font=("Arial", 14), 
            command=lambda l=letra: reproducir_audio(l)
        )
        button.pack(side="left", padx=2, pady=10)

    root.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    crear_interfaz()
