class Hospital:
    def __init__(self):
        self.medicos = []  # Lista para almacenar médicos
        self.pacientes = []  # Lista para almacenar pacientes
        self.citas = []  # Lista para almacenar citas

    def agregar_medico(self, medico):
        """Agrega un médico a la lista de médicos."""
        self.medicos.append(medico)
        print(f"Médico {medico.nombre} agregado exitosamente.")

    def agregar_paciente(self, paciente):
        """Agrega un paciente a la lista de pacientes."""
        self.pacientes.append(paciente)
        print(f"Paciente {paciente.nombre} agregado exitosamente.")

    def buscar_paciente(self, identificacion):
        """Busca un paciente por su identificación."""
        return next((p for p in self.pacientes if p.identificacion == identificacion), None)

    def buscar_medico(self, identificacion):
        """Busca un médico por su identificación."""
        return next((m for m in self.medicos if m.identificacion == identificacion), None)

    def agendar_cita(self, paciente, medico, fecha, motivo):
        """Agrega una cita a la lista de citas."""
        cita = {
            'paciente': paciente,
            'medico': medico,
            'fecha': fecha,
            'motivo': motivo
        }
        self.citas.append(cita)
        print(f"Cita agendada para {paciente.nombre} con {
              medico.nombre} el {fecha}.")

    def cancelar_cita(self, cita):
        """Cancela una cita existente."""
        if cita in self.citas:
            self.citas.remove(cita)
            print(f"Cita con {cita['medico'].nombre} el {
                  cita['fecha']} ha sido cancelada.")
        else:
            print("Cita no encontrada.")

    def mostrar_citas(self):
        """Muestra todas las citas agendadas."""
        if not self.citas:
            print("No hay citas agendadas.")
        else:
            for cita in self.citas:
                print(f"Cita: {cita['motivo']} - Paciente: {cita['paciente'].nombre}, Médico: {
                      cita['medico'].nombre}, Fecha: {cita['fecha']}")
