import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

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

        plt.style.use("seaborn-darkgrid")
        plt.plot(x_vals, y_vals, color="red", linewidth=2, label=expresion)
        plt.title("Representación Gráfica de la Función")
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.axhline(0, color='black', linestyle='--', linewidth=0.7)
        plt.axvline(0, color='black', linestyle='--', linewidth=0.7)
        plt.legend()
        plt.show()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos")

ventana = tk.Tk()
ventana.title("Calculadora de Función Lineal")
ventana.geometry("420x380")
ventana.configure(bg="#d9f0ff")

titulo = tk.Label(ventana, text="Gráfica de Función", font=("Verdana", 16, "bold"), bg="#d9f0ff", fg="#004080")
titulo.pack(pady=10)

tk.Label(ventana, text="Pendiente (m):", font=("Verdana", 12), bg="#d9f0ff").pack()
input_pendiente = tk.Entry(ventana, font=("Verdana", 12), justify="center")
input_pendiente.pack()

tk.Label(ventana, text="Intercepto (b):", font=("Verdana", 12), bg="#d9f0ff").pack()
input_intercepto = tk.Entry(ventana, font=("Verdana", 12), justify="center")
input_intercepto.pack()

tk.Label(ventana, text="Rango mínimo de x:", font=("Verdana", 12), bg="#d9f0ff").pack()
input_xmin = tk.Entry(ventana, font=("Verdana", 12), justify="center")
input_xmin.pack()

tk.Label(ventana, text="Rango máximo de x:", font=("Verdana", 12), bg="#d9f0ff").pack()
input_xmax = tk.Entry(ventana, font=("Verdana", 12), justify="center")
input_xmax.pack()

btn_calcular = tk.Button(ventana, text="Graficar", command=generar_grafica, font=("Verdana", 12, "bold"), bg="#336699", fg="white")
btn_calcular.pack(pady=15)

etiqueta_resultado = tk.Label(ventana, text="", font=("Verdana", 12), bg="#d9f0ff", fg="#004080")
etiqueta_resultado.pack()

ventana.mainloop()
