import matplotlib.pyplot as plt
import pandas as pd

primer_mes = input("Primer mes de comparación (archivo): ")
ventas = pd.read_excel(primer_mes, sheet_name="Ventas")
negocios = pd.read_excel(primer_mes, sheet_name="Negocios")
ventas_primer_mes = ventas.merge(negocios, on="Negocio", how="left")

segundo_mes = input("Segundo mes de comparación (archivo): ")
ventas_2 = pd.read_excel(segundo_mes, sheet_name="Ventas")

print(f"Cantidad de filas del primer mes: {len(ventas)} || Cantidad de filas del segundo mes: {len(ventas_2)}")

unir_ventas = pd.concat([ventas, ventas_2], ignore_index=True)
print(f"La cantidad final de filas es: {len(unir_ventas)}")