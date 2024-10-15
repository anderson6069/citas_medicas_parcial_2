class Persona:
    def __init__(self, identificacion, nombre, celular):
        self.identificacion = identificacion
        self.nombre = nombre
        self.celular = celular


class Medico(Persona):
    def __init__(self, identificacion, nombre, celular, especialidad):
        super().__init__(identificacion, nombre, celular)
        self.especialidad = especialidad


class Paciente(Persona):
    def __init__(self, identificacion, nombre, celular, correo):
        super().__init__(identificacion, nombre, celular)
        self.correo = correo
        self.medico_preferencia = None

    def asignar_medico_preferencia(self, medico):
        self.medico_preferencia = medico
