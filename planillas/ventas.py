import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

# primer_mes = input("Primer mes de comparación (archivo): ")
# ventas = pd.read_excel(primer_mes, sheet_name="Ventas")
# negocios = pd.read_excel(primer_mes, sheet_name="Negocios")
# ventas_primer_mes = ventas.merge(negocios, on="Negocio", how="left")

# segundo_mes = input("Segundo mes de comparación (archivo): ")
# ventas_2 = pd.read_excel(segundo_mes, sheet_name="Ventas")

# print(f"Cantidad de filas del primer mes: {len(ventas)} || Cantidad de filas del segundo mes: {len(ventas_2)}")

# unir_ventas = pd.concat([ventas, ventas_2], ignore_index=True)
# unir_ventas["Facturacion"] = unir_ventas["Precio_Unitario"] * unir_ventas["Unidades"]
# totales = unir_ventas.groupby("Mes", sort=False)[["Unidades", "Facturacion"]].sum()
# print(totales)

# fig, ejes = plt.subplots(1, 2, figsize=(13, 6))
# fig.suptitle("Comparación de Ventas de Alfajores", fontsize=16, fontweight="bold")

# totales["Unidades"].plot(kind="bar", ax=ejes[0], rot=0, title="Unidades Vendidas", color=["green", "red"])
# totales["Facturacion"].plot(kind="bar", ax=ejes[1], rot=0, title="Total Facturado", color=["green", "red"])

# ejes[0].bar_label(ejes[0].containers[0])
# ejes[1].bar_label(ejes[1].containers[0], fmt="$%.0f")

# plt.tight_layout()
# plt.show()

ventana = tk.Tk()
ventana.title("Comparador de Meses")

ancho, alto = 600, 400
x = (ventana.winfo_screenwidth() - ancho) // 2
y = (ventana.winfo_screenheight() - alto) // 2
ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

ventana.mainloop()