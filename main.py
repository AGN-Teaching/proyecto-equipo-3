from cliente import Cliente
from producto import Producto
from compra import Compra
from recibo import Recibo
from factura import Factura

# Optenemos los datos de cliente con su respectivo manejo de errores
while True:
    rfc = input("Ingrese su RFC: ")
    try:
        if len(rfc) == 13:
            tipo = "persona física"
            nombre = input("Ingrese su nombre: ")
            correo_electronico = input("Ingrese su correo electrónico: ")
            cliente1 = Cliente(rfc, tipo, nombre, correo_electronico=correo_electronico)
            break
        elif len(rfc) == 12:
            tipo = "persona moral"
            razon_social = input("Ingrese la razón social: ")
            persona_contacto = input("Ingrese el nombre de la persona de contacto: ")
            correo_electronico = input("Ingrese el correo electrónico: ")
            cliente1 = Cliente(rfc, tipo, razon_social, persona_contacto, correo_electronico)
            break
        else:
            # Manejo de error
            raise ValueError("El RFC debe tener 12 dígitos (moral) o 13 dígitos (física)")
    except ValueError as e:
        print(e)

# Optenemos los datos de compra con su respectivo manejo de error
productos = []
while True:
    nombre_producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if nombre_producto.lower() == 'fin':
        break
    try:
        precio_producto = float(input("Ingrese el precio del producto: "))
        cantidad_producto = int(input("Ingrese la cantidad del producto: "))
        if precio_producto <= 0 or cantidad_producto <= 0:
            # Manejo de error
            raise ValueError("Tanto el precio como la cantidad deben ser números positivos.")
        producto = Producto(nombre_producto, precio_producto, cantidad_producto)
        productos.append(producto)
    except ValueError as e:
        print("Error:", e)

if not productos:
    print("Debe ingresar al menos un producto.")
else:
    compra1 = Compra(cliente1, productos)
    compra1.calcular_total()
    recibo1 = Recibo(compra1)

    # Se genera y se imprime el recibo
    print("\nGenerando recibo:")
    recibo1.generar_recibo()

    # Pedimos el identificador del recibo para generar las facturas
    identificador_recibo = input("Ingrese el identificador del recibo para generar la factura (o 'fin' para salir): ")
    if identificador_recibo.lower() == 'fin':
        exit()

    if identificador_recibo != recibo1.identificador:
        print("El identificador del recibo no coincide. Intente nuevamente.")
    else:
        factura1 = Factura(compra1)
        factura1.generar_factura_pdf()
        factura1.generar_factura_xml()
        print(f"Factura generada con éxito para el recibo con identificador {identificador_recibo}")
