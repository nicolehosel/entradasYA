#1 Modelado del sistema
class Evento:
    def __init__(self, nombre, ciudad, tipo, precio, cantidad_entradas_disponibles):
        self.nombre = nombre
        self.ciudad = ciudad
        self.tipo = tipo
        self.precio = precio
        self.cantidad_entradas_disponibles = cantidad_entradas_disponibles

    def __str__(self):
        return f"Evento(nombre={self.nombre}, ciudad={self.ciudad}, tipo={self.tipo}, precio={self.precio}, cantidad_entradas_disponibles={self.cantidad_entradas_disponibles})"

listaEvento = []
dictEvento = {}
conjuntoEvento = set()

def nuevoEvento():
    nombre = input("Ingrese el nombre:").strip().lower()
    ciudad = input("Ingrese la ciudad:").strip().lower()
    tipo = input("Ingreso el tipo de evento:").strip().lower()
    precio = int(input("Ingrese el precio:"))
    cantidad_entradas_disponibles = int(input("Ingrese el numero de entradas disponibles:"))
    nuevoEvento = Evento(nombre, ciudad, tipo, precio, cantidad_entradas_disponibles)
    listaEvento.append(nuevoEvento)
    dictEvento[nuevoEvento.nombre] = nuevoEvento
    conjuntoEvento.add(nuevoEvento)

def buscarEvento():
    evento = input("Ingrese el nombre del evento que desea buscar:").strip().lower()
    if evento in dictEvento:
        print(dictEvento[evento])
    else:
        print("El evento no existe")

def mostrarEventos():
    for evento in dictEvento.values():
        print(evento)

class Cliente:
    def __init__(self, nombre, DNI, email):
        self.nombre = nombre
        self.DNI = DNI
        self.email = email

    def __str__(self):
        return f"Cliente(nombre={self.nombre}, DNI={self.DNI}, email={self.email})"

listaClientes = []
dictCliente = {}

def nuevoCliente():
    nombre = input("Ingrese el nombre:").strip().lower()
    DNI = input("Ingrese el DNI:").strip().lower()
    email = input("Ingrese el email:").strip().lower()
    nuevoCliente = Cliente(nombre, DNI, email)
    listaClientes.append(nuevoCliente)
    dictCliente[nuevoCliente.nombre] = nuevoCliente

def buscarCliente():
    cliente = input("Ingrese el nombre del cliente que desea buscar:").strip().lower()
    if cliente in dictCliente:
        print(dictCliente[cliente])
    else:
        print("El cliente no existe")

def mostrarClientes():
    for cliente in dictCliente.values():
        print(cliente)

class Compra:
    def __init__(self, cliente_nombre, evento_nombre, cantidad_entradas, monto_total):
        self.cliente_nombre = cliente_nombre
        self.evento_nombre = evento_nombre
        self.cantidad_entradas = cantidad_entradas
        self.monto_total = monto_total

    def __str__(self):
        return f"Compra(cliente={self.cliente_nombre},evento={self.evento_nombre}, cantidad entradas={self.cantidad_entradas}, monto_total={self.monto_total})"


listaCompras = []

def nuevaCompra():
    cliente_nombre = input("Ingrese el nombre del cliente:").strip().lower()
    evento_nombre = input("Ingrese el nombre del evento:").strip().lower()
    if evento_nombre not in dictEvento:
        print("Evento no encontrado")
        return
    evento = dictEvento[evento_nombre]

    cantidad_entradas = int(input("Ingrese cantidad de entradas:"))

    if cantidad_entradas > evento.cantidad_entradas_disponibles:
        print("No hay mas entradas disponibles")
        return

    monto_total = cantidad_entradas * evento.precio

    evento.cantidad_entradas_disponibles -= cantidad_entradas

    nuevaCompra = Compra(cliente_nombre, evento_nombre, cantidad_entradas, monto_total)
    listaCompras.append(nuevaCompra)

    print("El monto total de la compra es:", monto_total)
    print("Compra registrada correctamente")

def mostrarCompras():
    for compra in listaCompras:
        print(compra)

def resumenEntradasVendidas():
    ventas_por_evento = {}
    for compra in listaCompras:
        if compra.evento_nombre in ventas_por_evento:
            ventas_por_evento[compra.evento_nombre] += compra.cantidad_entradas
        else:
            ventas_por_evento[compra.evento_nombre] = compra.cantidad_entradas

    print("RESUMEN ENTRADAS VENDIDAS POR EVENTO")
    for evento, total in ventas_por_evento.items():
        print(f"Evento: {evento}, Entradas vendidas: {total}")

def resumenEntradasVendidasTipo():
    ventas_por_tipo = {}
    for compra in listaCompras:
        evento = dictEvento[compra.evento_nombre]
        tipo_evento = evento.tipo

        if tipo_evento in ventas_por_tipo:
            ventas_por_tipo[tipo_evento] += compra.cantidad_entradas
        else:
            ventas_por_tipo[tipo_evento] = compra.cantidad_entradas

    print("RESUMEN DE ENTRADAS VENDIDAS POR TIPO DE EVENTO")
    for tipo, total in ventas_por_tipo.items():
        print(f"Tipo de evento: {tipo}, Entradas vendidas: {total}")

#2 Menu Iterativo

print("-" * 25)
print("EntradasYA - Menu")
print("-" * 25)

while True:
    try:
        print("")
        print("1. Agregar nuevos eventos")
        print("2. Agregar nuevos clientes")
        print("3. Registrar una compra")
        print("4. Ver listado de compras")
        print("5. Ver resumen de ventas")
        print("6. Buscar evento")
        print("7. Buscar cliente")
        print("8. Salir del sistema")
        print("")
        seleccione_opcion = int(input("Elija una opcion (1-6):"))

        if seleccione_opcion == 1:
            nuevoEvento()
            print("")
            print("Evento agregado correctamente")

        elif seleccione_opcion == 2:
            nuevoCliente()
            print("")
            print("Cliente agregado correctamente")

        elif seleccione_opcion == 3:
            nuevaCompra()
            print("")


        elif seleccione_opcion == 4:
            for compra in listaCompras:
                print(compra)

        elif seleccione_opcion == 5:
            resumenEntradasVendidas()
            resumenEntradasVendidasTipo()

        elif seleccione_opcion == 6:
            buscarEvento()

        elif seleccione_opcion == 7:
            buscarCliente()

        elif seleccione_opcion == 8:
            print("Saliendo del sistema")
            break

    except ValueError:
        print("Error: Ingrese un valor valido")









