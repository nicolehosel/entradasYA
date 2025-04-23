# reporte.py
import sys
import json

# Cargar datos desde archivos JSON guardados por tp1.py
try:
    with open("compras.json", "r") as f:
        compras_data = json.load(f)

    with open("eventos.json", "r") as f:
        eventos_data = json.load(f)

except FileNotFoundError:
    print("Error: No se encontraron los archivos de compras o eventos. Asegurate de ejecutar tp1.py primero y salir del sistema para guardar los datos.")
    sys.exit(1)

# Reconstrucción de objetos desde datos JSON
class Compra:
    def __init__(self, cliente_nombre, evento_nombre, cantidad_entradas, monto_total):
        self.cliente_nombre = cliente_nombre
        self.evento_nombre = evento_nombre
        self.cantidad_entradas = cantidad_entradas
        self.monto_total = monto_total

    def __str__(self):
        return f"Compra(cliente={self.cliente_nombre}, evento={self.evento_nombre}, entradas={self.cantidad_entradas}, monto={self.monto_total})"

class Evento:
    def __init__(self, nombre, ciudad, tipo, precio, cantidad_entradas_disponibles):
        self.nombre = nombre
        self.ciudad = ciudad
        self.tipo = tipo
        self.precio = precio
        self.cantidad_entradas_disponibles = cantidad_entradas_disponibles

listaCompras = [
    Compra(**c) for c in compras_data
]

dictEvento = {
    nombre: Evento(**datos) for nombre, datos in eventos_data.items()
}

def reporte_por_tipo(tipo_buscado):
    tipo_buscado = tipo_buscado.lower()
    total_recaudado = 0
    compras_encontradas = False

    print(f"\n📋 Compras para eventos tipo '{tipo_buscado}':")
    for compra in listaCompras:
        if compra.evento_nombre in dictEvento:
            evento = dictEvento[compra.evento_nombre]
            if evento.tipo == tipo_buscado:
                compras_encontradas = True
                print(compra)
                total_recaudado += compra.monto_total

    if not compras_encontradas:
        print(f"No se encontraron compras para el tipo de evento: {tipo_buscado}")
        return

    print("\n💰 Total recaudado en todos los eventos de tipo", tipo_buscado + ": $" + str(total_recaudado))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Debe ingresar el tipo de evento como parámetro.")
        print("Ejemplo: python reporte.py teatro")
        sys.exit(1)

    reporte_por_tipo(sys.argv[1])