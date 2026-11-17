import matplotlib.pyplot as plt
import pandas as pd

primer_mes = input("Primer mes de comparación (archivo): ")

ventas = pd.read_excel(primer_mes, sheet_name="Ventas")

#print(ventas)

negocios=pd.read_excel(primer_mes, sheet_name="Negocios")

ventas_primer_mes = ventas.merge(negocios, on="Negocio", how="left")

print(ventas_primmer_mes)

