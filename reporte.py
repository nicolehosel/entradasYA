# reporte.py
import sys

compras = ({"cliente": "jose", "evento": "Megadeth", "entradas": 2, "monto": 2309},
           {"cliente": "nicole", "evento": "Megadeth", "entradas": 4, "monto": 6509},
           {"cliente": "mica", "evento": "Megadeth", "entradas": 6, "monto": 8909},
            {"cliente": "delfi", "evento": "tini", "entradas": 2, "monto": 25049})


parametros = sys.argv
if len(parametros) == 2:
    evento = parametros[1]
    print("Parametro recibido", evento)
    total = 0
    for compra in compras:
        if compra["evento"] == evento:
            total+=compra["monto"]
            print("{} compra {} entradas para {} por un total de ${}".format(compra["cliente"], compra["entradas"], compra["evento"], compra["monto"]))
    print("El valor total de las entradas es:", total)
else:
    print("Error en parametros")

