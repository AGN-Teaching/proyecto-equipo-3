class Cliente:
    # Método constructor de la clase cliente
    def __init__(self, rfc, tipo, nombre, correo_electronico=None, razon_social=None, persona_contacto=None):
        self.rfc = rfc
        self.tipo = tipo
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.razon_social = razon_social
        self.persona_contacto = persona_contacto

    # Método getter de los datos en forma de cadena
    def __str__(self):
        if self.tipo == "persona física":
            return f"Cliente: {self.rfc} ({self.tipo}) - {self.nombre} - Correo: {self.correo_electronico}"
        elif self.tipo == "persona moral":
            return f"Cliente: {self.rfc} ({self.tipo}) - {self.razon_social} - Contacto: {self.persona_contacto} - Correo: {self.correo_electronico}"
        else:
            return f"Cliente: {self.rfc} - Tipo desconocido"
