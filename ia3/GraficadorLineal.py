import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generar_grafica():
    try:
        pendiente = float(input_pendiente.get())
        intercepto = float(input_intercepto.get())

        try:
            x_inicio = float(input_xmin.get())
            x_final = float(input_xmax.get())
            if x_inicio >= x_final:
                raise ValueError
        except:
            x_inicio, x_final = -10, 10

        expresion = f"y = {pendiente}x + {intercepto}"
        etiqueta_resultado.config(text=f"Ecuación: {expresion}")

        x_vals = np.linspace(x_inicio, x_final, 500)
        y_vals = pendiente * x_vals + intercepto

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(x_vals, y_vals, color="#fdd835", linewidth=2, label=expresion)  # Amarillo brillante
        ax.axhline(0, color='#6200ea', linestyle='--', linewidth=0.7)  # Lila
        ax.axvline(0, color='#6200ea', linestyle='--', linewidth=0.7)  # Lila
        ax.set_title("Gráfica de la Función Lineal", fontsize=16, color="#e040fb")  # Lila brillante
        ax.set_xlabel("Eje X", fontsize=12, color="#f50057")  # Rosa vibrante
        ax.set_ylabel("Eje Y", fontsize=12, color="#f50057")  # Rosa vibrante
        ax.legend()
        ax.grid(True)

        canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos")

ventana = tk.Tk()
ventana.title("Calculadora de Función Lineal")
ventana.geometry("600x650")
ventana.configure(bg="#000")

titulo = tk.Label(ventana, text="Gráfica de Función", font=("Arial", 18, "bold"), bg="#000", fg="#00c853") 
titulo.pack(pady=20)

tk.Label(ventana, text="Pendiente (m):", font=("Arial", 12), bg="#000", fg="#00c853").pack()
input_pendiente = tk.Entry(ventana, font=("Arial", 12), justify="center", bd=2, relief="solid", fg="#6200ea")  
input_pendiente.pack(pady=5)

tk.Label(ventana, text="Intercepto (b):", font=("Arial", 12), bg="#000", fg="#00c853").pack()
input_intercepto = tk.Entry(ventana, font=("Arial", 12), justify="center", bd=2, relief="solid", fg="#6200ea") 
input_intercepto.pack(pady=5)

tk.Label(ventana, text="Rango mínimo de x:", font=("Arial", 12), bg="#000", fg="#00c853").pack()
input_xmin = tk.Entry(ventana, font=("Arial", 12), justify="center", bd=2, relief="solid", fg="#6200ea")  
input_xmin.pack(pady=5)

tk.Label(ventana, text="Rango máximo de x:", font=("Arial", 12), bg="#000", fg="#00c853").pack()
input_xmax = tk.Entry(ventana, font=("Arial", 12), justify="center", bd=2, relief="solid", fg="#6200ea")  
input_xmax.pack(pady=5)

btn_calcular = tk.Button(ventana, text="Graficar", command=generar_grafica, font=("Arial", 12, "bold"), bg="#00c853", fg="white", bd=2, relief="solid")  
btn_calcular.pack(pady=20)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), bg="#000", fg="#00c853")
etiqueta_resultado.pack()

frame_grafica = tk.Frame(ventana, bg="#000")
frame_grafica.pack(pady=20)

ventana.mainloop()
