import os
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Carpeta donde está guardado este script (acá se buscan los .xlsx)
CARPETA = os.path.dirname(os.path.abspath(__file__))


def listar_xlsx():
    """Devuelve la lista de archivos .xlsx de la carpeta (ignora temporales de Excel)."""
    return sorted(
        f for f in os.listdir(CARPETA)
        if f.lower().endswith(".xlsx") and not f.startswith("~$")
    )


def cargar_grafico():

    nombre1 = caja1.get()
    nombre2 = caja2.get()

    if not nombre1 or not nombre2:
        print("Seleccioná un archivo en cada lista.")
        return

    primer_mes = os.path.join(CARPETA, nombre1)
    segundo_mes = os.path.join(CARPETA, nombre2)

    ventas = pd.read_excel(primer_mes, sheet_name="Ventas")
    negocios = pd.read_excel(primer_mes, sheet_name="Negocios")
    ventas_primer_mes = ventas.merge(negocios, on="Negocio", how="left")

    ventas_2 = pd.read_excel(segundo_mes, sheet_name="Ventas")

    print(f"Cantidad de filas del primer mes: {len(ventas)} || Cantidad de filas del segundo mes: {len(ventas_2)}")

    unir_ventas = pd.concat([ventas, ventas_2], ignore_index=True)
    unir_ventas["Facturacion"] = unir_ventas["Precio_Unitario"] * unir_ventas["Unidades"]
    totales = unir_ventas.groupby("Mes", sort=False)[["Unidades", "Facturacion"]].sum()
    print(totales)

    fig, ejes = plt.subplots(1, 2, figsize=(13, 6))
    fig.suptitle("Comparación de Ventas de Alfajores", fontsize=16, fontweight="bold")

    totales["Unidades"].plot(kind="bar", ax=ejes[0], rot=0, title="Unidades Vendidas", color=["green", "red"])
    totales["Facturacion"].plot(kind="bar", ax=ejes[1], rot=0, title="Total Facturado", color=["green", "red"])

    ejes[0].bar_label(ejes[0].containers[0])
    ejes[1].bar_label(ejes[1].containers[0], fmt="$%.0f")

    plt.tight_layout()
    plt.show()


ventana = tk.Tk()
ventana.title("Comparador de Meses")

ancho, alto = 400, 300
x = (ventana.winfo_screenwidth() - ancho) // 2
y = (ventana.winfo_screenheight() - alto) // 2
ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

archivos = listar_xlsx()

tk.Label(ventana, text="Primer mes :").pack(padx=20, pady=(15, 2))
caja1 = ttk.Combobox(ventana, values=archivos, state="readonly", width=35)
caja1.pack()

tk.Label(ventana, text="Segundo mes:").pack(pady=(10, 2))
caja2 = ttk.Combobox(ventana, values=archivos, state="readonly", width=35)
caja2.pack()

tk.Button(ventana, text="Cargar Gráficos", command=cargar_grafico).pack(pady=20)

ventana.mainloop()