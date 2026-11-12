import csv
import matplotlib.pyplot as plt

unidades={}

with open("ventas.csv", encoding="utf-8",newline="") as f:
    lector=csv.DictReader(f,delimiter=";")
    for venta in lector:
        if venta["fecha"] and venta["sucursal"] and venta["producto"] and venta["cantidad"] and venta["precio_unitario"]:
    #       print(venta)
            cantidad=int(venta["cantidad"])
            fecha=venta["fecha"]
            precio_unitario=float(venta["precio_unitario"].replace(",","."))
            sucursal=venta["sucursal"]
            producto=venta["producto"]
    #       print(f"{cantidad} {precio_unitario} {sucursal} {producto} {fecha}")
            unidades[producto]=unidades.get(producto,0)+cantidad
    print(unidades)
#--- Grafico de Cantidades por producto ----
productos=list(unidades.keys())
cantidades=list(unidades.values())

colores=["#2800CC","#86FFC2","#000000"]

barras=plt.bar(productos,cantidades,color=colores)
plt.bar_label(barras,fmt="%.2f")

plt.title("Grafico de cantidades de cada producto")

plt.xlabel("Productos")

plt.ylabel("Cantidades (Unidades)")

plt.show()


