class Hospital:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.citas = []

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def buscar_medico(self, id_medico):
        for medico in self.medicos:
            if medico.identificacion == id_medico:
                return medico
        return None

    def buscar_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.identificacion == id_paciente:
                return paciente
        return None

    def agendar_cita(self, paciente, medico, fecha, motivo):
        cita = {
            'paciente': paciente,
            'medico': medico,
            'fecha': fecha,
            'motivo': motivo
        }
        self.citas.append(cita)

    def cancelar_cita(self, cita):
        self.citas.remove(cita)
