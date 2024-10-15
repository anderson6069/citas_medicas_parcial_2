class Persona:
    def __init__(self, identificacion, nombre, celular):
        self.id = identificacion
        self.nombre = nombre
        self.celular = celular


class Paciente(Persona):
    def __init__(self, identificacion, nombre, celular, correo):
        super().__init__(identificacion, nombre, celular)
        self.correo = correo


class Medico(Persona):
    def __init__(self, identificacion, nombre, celular, especialidad):
        super().__init__(identificacion, nombre, celular)
        self.especialidad = especialidad
        self.medico_preferido = None

    def asignar_medico_preferencia(self, medico):
        self.medico_preferido = medico


class PersonasFactory:
    @staticmethod
    def crear_persona(tipo, identificacion, nombre, celular, especialidad=None, correo=None):
        if tipo == "paciente":
            return Paciente(identificacion, nombre, celular, correo)
        elif tipo == "medico":
            return Medico(identificacion, nombre, celular, especialidad)
        else:
            raise ValueError("Tipo de persona no válido.")
