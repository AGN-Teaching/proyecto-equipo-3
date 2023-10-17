import uuid
from xml.etree import ElementTree as ET
# Naturalmente se tienen que tener descargado ambos paquetes
from fpdf import FPDF

class Factura:
    # Método constructor de la clase factura
    def __init__(self, compra):
        self.compra = compra # Crea una instancia de la clase compra y se utiliza como atributo
        self.cfid = str(uuid.uuid4())

    def generar_factura_pdf(self):
        # Se crea un archivo pdf que representará a la factura
        pdf = FPDF() # Crea objeto pdf
        pdf.add_page() # Le agrega una página
        # Se agregan elementos con cierto fórmato
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Factura", ln=True, align='C')
        pdf.cell(200, 10, txt="", ln=True, align='C')
        pdf.cell(200, 10, txt="Fecha: " + self.compra.fecha, ln=True)
        pdf.cell(200, 10, txt="RFC del cliente: " + self.compra.cliente.rfc, ln=True)
        pdf.cell(200, 10, txt="Nombre del cliente: " + self.compra.cliente.nombre, ln=True)
        pdf.cell(200, 10, txt="Comprobante fiscal: " + self.cfid, ln=True)
        pdf.cell(200, 10, txt="Total: $" + str(self.compra.total), ln=True)
        pdf.output("factura.pdf") # Se guarda el pdf como factura.pdf

    def generar_factura_xml(self):
        # Se crea un archivo XML que representará a la factura
        root = ET.Element("Factura") # Se crea un elemento raíz factura
        compra_element = ET.SubElement(root, "Compra")
        # Se agregan elementos
        ET.SubElement(compra_element, "Fecha").text = self.compra.fecha
        ET.SubElement(compra_element, "RFCCliente").text = self.compra.cliente.rfc
        ET.SubElement(compra_element, "NombreCliente").text = self.compra.cliente.nombre  # Utilizar el nombre del cliente
        ET.SubElement(compra_element, "CFID").text = self.cfid
        ET.SubElement(compra_element, "Total").text = str(self.compra.total)

        tree = ET.ElementTree(root) # Se crea un árbol XML con el elemento raíz
        tree.write("factura.xml") # Se guarda el XML como factura.xml
