class Producto:
    # Método constructor de la clase producto
    def __init__(self, nombre_producto, precio, cantidad):
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.cantidad = cantidad

    # Calculamos el subtotal de uno de los productos
    def calcular_subtotal(self):
        return self.precio * self.cantidad
