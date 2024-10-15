from persona import Medico, Paciente


class PersonasFactory:
    @staticmethod
    def crear_persona(tipo, identificacion, nombre, celular, especialidad=None, correo=None):
        if tipo == "medico":
            return Medico(identificacion, nombre, celular, especialidad)
        elif tipo == "paciente":
            return Paciente(identificacion, nombre, celular, correo)
        else:
            raise ValueError("Tipo de persona inválido.")
