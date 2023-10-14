import uuid

class Recibo:
    # Método constructor de la clase recibo
    def __init__(self, compra):
        self.compra = compra # Crea una instancia de la clase compra y se utiliza como atributo
        self.identificador = str(uuid.uuid4())

    # Método que imprime el recibo con la información de compra
    def generar_recibo(self):
        print("Recibo")
        print("Identificador:", self.identificador)
        print("Fecha:", self.compra.fecha)
        print("RFC del cliente:", self.compra.cliente.rfc)
        print("Productos:")
        for producto in self.compra.producto:
            print(f"- {producto.nombre_producto}: ${producto.precio} x {producto.cantidad} = ${producto.calcular_subtotal()}")
        print("Subtotal: ${:.2f}".format(self.compra.total - self.compra.iva))
        print("IVA (16%): ${:.2f}".format(self.compra.iva))
        print("Total: ${:.2f}".format(self.compra.total))
