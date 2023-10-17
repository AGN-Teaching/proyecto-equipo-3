class Cliente:
    # Método constructor de la clase cliente
    def __init__(self, rfc, tipo, nombre, correo_electronico=None, razon_social=None, persona_contacto=None):
        self.rfc = rfc
        self.tipo = tipo
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.razon_social = razon_social
        self.persona_contacto = persona_contacto

    def obtener_Rfc(self):
        return self.rfc

    def obtener_Tipo(self):
        return self.tipo

    def obtener_Nombre(self):
        return self.nombre

    def obtener_Correo_electronico(self):
        return self.correo_electronico

    def obtener_Razon_social(self):
        return self.razon_social

    def obtener_Persona_contacto(self):
        return self.persona_contacto