import csv
import matplotlib.pyplot as plt

unidades={}

with open("ventas.csv", encoding="utf-8",newline="") as f:
    lector=csv.DictReader(f, delimiter=";")
    for venta in lector:
        if venta["sucursal"] and venta["producto"] and venta["fecha"] and venta["cantidad"] and venta["precio_unitario"]:
           cantidad=int(venta["cantidad"])
           precio_unitario=float(venta["precio_unitario"].replace(",","."))  
           sucursal=venta["sucursal"]
           producto=venta["producto"]
           print(f"{cantidad} {precio_unitario} {sucursal} {producto}")
           unidades[producto]=unidades.get(producto, 0)+cantidad
    print(unidades)