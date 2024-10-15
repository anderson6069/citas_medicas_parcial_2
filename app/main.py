from hospital import Hospital
from persona_factory import PersonasFactory


class Main:
    def __init__(self):
        self.hospital = Hospital()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Agregar persona")
            print("2. Pedir cita")
            print("3. Cancelar cita")
            print("4. Asignar médico de preferencia")
            print("5. Ver citas pendientes")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_persona()
            elif opcion == "2":
                self.pedir_cita()
            elif opcion == "3":
                self.cancelar_cita()
            elif opcion == "4":
                self.asignar_medico_preferencia()
            elif opcion == "5":
                self.ver_citas_pendientes()
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida.")

    def agregar_persona(self):
        print("\n--- Agregar Persona ---")
        print("1. Médico")
        print("2. Paciente")
        tipo_persona = input("Seleccione el tipo de persona (1 o 2): ")

        identificacion = self.obtener_dato("Ingrese la identificación: ")
        nombre = self.obtener_dato("Ingrese el nombre: ")
        celular = self.obtener_dato("Ingrese el celular: ")

        if tipo_persona == "1":
            especialidad = self.obtener_dato("Ingrese la especialidad: ")
            persona = PersonasFactory.crear_persona(
                "medico", identificacion, nombre, celular, especialidad)
            self.hospital.agregar_medico(persona)
        elif tipo_persona == "2":
            correo = self.obtener_dato("Ingrese el correo: ")
            persona = PersonasFactory.crear_persona(
                "paciente", identificacion, nombre, celular, correo=correo)
            self.hospital.agregar_paciente(persona)
        else:
            print(
                "Tipo de persona inválido. Solo se aceptan opciones 1 (médico) o 2 (paciente).")

    def pedir_cita(self):
        print("\n--- Pedir Cita ---")
        id_paciente = self.obtener_dato(
            "Ingrese la identificación del paciente: ")
        id_medico = self.obtener_dato("Ingrese la identificación del médico: ")
        fecha = self.obtener_dato("Ingrese la fecha de la cita (YYYY-MM-DD): ")
        motivo = self.obtener_dato("Ingrese el motivo de la cita: ")

        paciente = self.hospital.buscar_paciente(id_paciente)
        medico = self.hospital.buscar_medico(id_medico)

        if paciente and medico:
            self.hospital.agendar_cita(paciente, medico, fecha, motivo)
            print("Cita agendada exitosamente.")
        else:
            print("Paciente o médico no encontrado.")

    def obtener_dato(self, mensaje):
        """Solicita un dato al usuario y verifica que no esté vacío."""
        while True:
            dato = input(mensaje).strip()
            if dato:
                return dato
            print("Este campo es obligatorio y no puede quedar vacío.")

    def cancelar_cita(self):
        print("\n--- Cancelar Cita ---")
        id_paciente = self.obtener_dato(
            "Ingrese la identificación del paciente: ")
        paciente = self.hospital.buscar_paciente(id_paciente)

        if paciente:
            print("Citas pendientes:")
            for i, cita in enumerate(self.hospital.citas):
                if cita['paciente'] == paciente:
                    print(
                        f"{i + 1}. {cita['motivo']} - Médico: {cita['medico'].nombre}, Fecha: {cita['fecha']}")

            opcion_cita = int(
                input("Seleccione la cita a cancelar (número): "))
            if 1 <= opcion_cita <= len(self.hospital.citas):
                cita_a_cancelar = self.hospital.citas[opcion_cita - 1]
                self.hospital.cancelar_cita(cita_a_cancelar)
                print("Cita cancelada exitosamente.")
            else:
                print("Opción inválida.")
        else:
            print("Paciente no encontrado.")

    def asignar_medico_preferencia(self):
        print("\n--- Asignar Médico de Preferencia ---")
        id_paciente = self.obtener_dato(
            "Ingrese la identificación del paciente: ")
        id_medico = self.obtener_dato("Ingrese la identificación del médico: ")

        paciente = self.hospital.buscar_paciente(id_paciente)
        medico = self.hospital.buscar_medico(id_medico)

        if paciente and medico:
            paciente.asignar_medico_preferencia(medico)
            print(f"Médico {medico.nombre} asignado como preferencia para el paciente {
                  paciente.nombre}.")
        else:
            print("Paciente o médico no encontrado.")

    def ver_citas_pendientes(self):
        print("\n--- Ver Citas Pendientes ---")
        id_paciente = self.obtener_dato(
            "Ingrese la identificación del paciente: ")
        paciente = self.hospital.buscar_paciente(id_paciente)

        if paciente:
            print("Citas pendientes:")
            for cita in self.hospital.citas:
                if cita['paciente'] == paciente:
                    print(f"Cita: {
                          cita['motivo']} - Médico: {cita['medico'].nombre}, Fecha: {cita['fecha']}")
        else:
            print("Paciente no encontrado.")


# Iniciar el programa
if __name__ == "__main__":
    main = Main()
    main.mostrar_menu()
