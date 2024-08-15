import tkinter as tk

class CalculadoraIVAISR:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de IVA e ISR")
        self.ventana.geometry("380x300")  # Tamaño de ventana
        self.ventana.resizable(False, False)  # No permitir cambiar tamaño
        self.ventana.eval("tk::PlaceWindow . center")  # Centrar ventana

        # Agregar título
        self.etiqueta_titulo = tk.Label(ventana, text="Calcular IVA e ISR", font=("Century Gothic", 18, "bold"))
        self.etiqueta_titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Configuración de tasa de IVA
        self.tasa_iva = 14.75  # %

        # Crear campo de entrada para el monto total
        self.etiqueta_monto = tk.Label(ventana, text="Monto total:", font=("Century Gothic", 12, "bold"))
        self.etiqueta_monto.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.entrada_monto = tk.Entry(ventana, font=("Century Gothic", 12, "bold"))
        self.entrada_monto.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Crear etiquetas para mostrar los resultados
        self.etiqueta_iva = tk.Label(ventana, text="IVA e ISR:", font=("Century Gothic", 12, "bold"))
        self.etiqueta_iva.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.etiqueta_total = tk.Label(ventana, text="Total:", font=("Century Gothic", 12, "bold"))
        self.etiqueta_total.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        # Crear label para mostrar el resultado copiable
        self.label_resultado = tk.Label(ventana, text="", font=("Century Gothic", 12, "bold"), wraplength=200)
        self.label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Crear botón para copiar el resultado
        self.boton_copiar = tk.Button(ventana, text="Copiar", font=("Century Gothic", 12, "bold"),bg="#87CEEB", fg="#FFFFFF", command=self.copiar_resultado)
        self.boton_copiar.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Crear función para calcular IVA
        self.entrada_monto.bind("<KeyRelease>", self.calcular_iva)

        # Configurar grid para que no se muevan los labels
        for i in range(6):
            ventana.grid_rowconfigure(i, weight=1)
        for i in range(2):
            ventana.grid_columnconfigure(i, weight=1)

    def calcular_iva(self, event):
        monto_total = float(self.entrada_monto.get())
        iva = monto_total * (self.tasa_iva / 100)
        total = monto_total + iva
        self.etiqueta_iva.config(text="IVA e ISR: " + format(iva, ".3f"))
        self.etiqueta_total.config(text="Total: " + format(total, ".3f"))
        self.label_resultado.config(text=format(total, ".3f"))

    def copiar_resultado(self):
        self.ventana.clipboard_clear()
        self.ventana.clipboard_append(self.label_resultado.cget("text"))

ventana = tk.Tk()
calculadora = CalculadoraIVAISR(ventana)
ventana.mainloop()