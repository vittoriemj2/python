import matplotlib.pyplot as plt
import pandas as pd

primer_mes = input("Primer mes de comparación (archivo): ")

ventas = pd.read_excel(primer_mes, sheet_name="ventas")

print(ventas)

#agosto.xlsx