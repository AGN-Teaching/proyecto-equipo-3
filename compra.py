from datetime import datetime

class Compra:
    # Método constructor de la clase Compra
    def __init__(self, cliente, producto):
        self.cliente = cliente # Crea una instancia de la clase cliente y se utiliza como atributo
        self.producto = producto # Crea una instancia de la clase producto y se utiliza como atributo
        self.fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Se registra la fecha y hora
        # Se inicializa el iva y el total en 0
        self.total = 0.0
        self.iva = 0.0

    # Cálcula el total final incluyendo el iva
    def calcular_total(self):
        for producto in self.producto:
            self.total += producto.calcular_subtotal()
        self.iva = self.total * 0.16
        self.total += self.iva
