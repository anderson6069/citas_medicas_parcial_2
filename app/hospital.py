class Hospital:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.citas = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def buscar_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return paciente
        return None

    def buscar_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return medico
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
