import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from hospital import Hospital
from persona_factory import PersonasFactory

console = Console()


class Main:
    def __init__(self):
        self.hospital = Hospital()
        self.cargar_datos()
        self.cargar_citas()  # Cargar citas al inicializar

    def cargar_datos(self):
        """Carga datos de pacientes y médicos desde archivos CSV."""
        # Cargar pacientes
        if os.path.exists('datos/pacientes.csv'):
            with open('datos/pacientes.csv', mode='r', encoding='utf-8') as file:
                for line in file:
                    identificacion, nombre, celular, correo = line.strip().split(',')
                    persona = PersonasFactory.crear_persona(
                        "paciente", identificacion, nombre, celular, correo=correo)
                    self.hospital.agregar_paciente(persona)

        # Cargar médicos
        if os.path.exists('datos/medicos.csv'):
            with open('datos/medicos.csv', mode='r', encoding='utf-8') as file:
                for line in file:
                    identificacion, nombre, celular, especialidad = line.strip().split(',')
                    persona = PersonasFactory.crear_persona(
                        "medico", identificacion, nombre, celular, especialidad)
                    self.hospital.agregar_medico(persona)

    def cargar_citas(self):
        """Carga citas desde el archivo CSV."""
        if os.path.exists('datos/citas.csv'):
            with open('datos/citas.csv', mode='r', encoding='utf-8') as file:
                for line in file:
                    fecha_hora, id_paciente, id_medico = line.strip().split(',')
                    paciente = self.hospital.buscar_paciente(id_paciente)
                    medico = self.hospital.buscar_medico(id_medico)

                    if paciente and medico:
                        self.hospital.agendar_cita(
                            paciente, medico, fecha_hora, motivo='Cita programada')
                    else:
                        console.print(f"[red]Paciente o médico no encontrado para la cita: {
                                      line.strip()}[/red]")

    def mostrar_menu(self):
        while True:
            console.print("\n--- Menú ---", style="bold underline")
            console.print("1. Agregar persona")
            console.print("2. Pedir cita")
            console.print("3. Cancelar cita")
            console.print("4. Asignar médico de preferencia")
            console.print("5. Ver citas pendientes")
            console.print("6. Consultar pacientes")
            console.print("7. Consultar médicos")
            console.print("8. Consultar citas")
            console.print("9. Salir")

            opcion = Prompt.ask("Seleccione una opción", choices=[
                                "1", "2", "3", "4", "5", "6", "7", "8", "9"])

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
                self.consultar_pacientes()
            elif opcion == "7":
                self.consultar_medicos()
            elif opcion == "8":
                self.consultar_citas()
            elif opcion == "9":
                console.print("Saliendo del programa...", style="bold green")
                break

    def agregar_persona(self):
        console.print("\n--- Agregar Persona ---", style="bold")
        console.print("1. Médico")
        console.print("2. Paciente")
        tipo_persona = Prompt.ask(
            "Seleccione el tipo de persona (1 o 2)", choices=["1", "2"])

        identificacion = self.obtener_dato("Ingrese la identificación: ")
        nombre = self.obtener_dato("Ingrese el nombre: ")
        celular = self.obtener_dato("Ingrese el celular: ")

        if tipo_persona == "1":
            especialidad = self.obtener_dato("Ingrese la especialidad: ")
            persona = PersonasFactory.crear_persona(
                "medico", identificacion, nombre, celular, especialidad)
            self.hospital.agregar_medico(persona)
            console.print(
                f"Médico {nombre} agregado exitosamente.", style="bold green")
        elif tipo_persona == "2":
            correo = self.obtener_dato("Ingrese el correo: ")
            persona = PersonasFactory.crear_persona(
                "paciente", identificacion, nombre, celular, correo=correo)
            self.hospital.agregar_paciente(persona)
            console.print(
                f"Paciente {nombre} agregado exitosamente.", style="bold green")
        else:
            console.print(
                "[red]Tipo de persona inválido. Solo se aceptan opciones 1 (médico) o 2 (paciente).[/red]")

    def pedir_cita(self):
        console.print("\n--- Pedir Cita ---", style="bold")
        id_paciente = self.obtener_dato(
            "Ingrese la identificación del paciente: ")
        id_medico = self.obtener_dato("Ingrese la identificación del médico: ")
        fecha = self.obtener_dato("Ingrese la fecha de la cita (YYYY-MM-DD): ")
        motivo = self.obtener_dato("Ingrese el motivo de la cita: ")

        paciente = self.hospital.buscar_paciente(id_paciente)
        medico = self.hospital.buscar_medico(id_medico)

        if paciente and medico:
            self.hospital.agendar_cita(paciente, medico, fecha, motivo)
            console.print("Cita agendada exitosamente.", style="bold green")
        else:
            console.print("[red]Paciente o médico no encontrado.[/red]")

    def obtener_dato(self, mensaje):
        """Solicita un dato al usuario y verifica que no esté vacío."""
        while True:
            dato = Prompt.ask(mensaje)
            if dato:
                return dato
            console.print(
                "[red]Este campo es obligatorio y no puede quedar vacío.[/red]")

    def cancelar_cita(self):
        console.print("\n--- Cancelar Cita ---", style="bold")
        id_paciente = self.obtener_dato(
            "Ingrese la identificación del paciente: ")
        paciente = self.hospital.buscar_paciente(id_paciente)

        if paciente:
            console.print("Citas pendientes:")
            table = Table(title="Citas Pendientes")
            table.add_column("Número", justify="right", style="cyan")
            table.add_column("Motivo", style="magenta")
            table.add_column("Médico", style="green")
            table.add_column("Fecha", style="yellow")

            for i, cita in enumerate(self.hospital.citas):
                if cita['paciente'] == paciente:
                    table.add_row(
                        str(i + 1), cita['motivo'], cita['medico'].nombre, cita['fecha'])

            console.print(table)

            opcion_cita = int(Prompt.ask(
                "Seleccione la cita a cancelar (número)"))
            if 1 <= opcion_cita <= len(self.hospital.citas):
                cita_a_cancelar = self.hospital.citas[opcion_cita - 1]
                self.hospital.cancelar_cita(cita_a_cancelar)
                console.print("Cita cancelada exitosamente.",
                              style="bold green")
            else:
                console.print("[red]Opción inválida.[/red]")
        else:
            console.print("[red]Paciente no encontrado.[/red]")

    def asignar_medico_preferencia(self):
        console.print("\n--- Asignar Médico de Preferencia ---", style="bold")
        id_paciente = self.obtener_dato(
            "Ingrese la identificación del paciente: ")
        id_medico = self.obtener_dato("Ingrese la identificación del médico: ")

        paciente = self.hospital.buscar_paciente(id_paciente)
        medico = self.hospital.buscar_medico(id_medico)

        if paciente and medico:
            paciente.asignar_medico_preferencia(medico)
            console.print(f"Médico {medico.nombre} asignado como preferencia para el paciente {
                          paciente.nombre}.", style="bold green")
        else:
            console.print("[red]Paciente o médico no encontrado.[/red]")

    def ver_citas_pendientes(self):
        console.print("\n--- Ver Citas Pendientes ---", style="bold")
        id_paciente = self.obtener_dato(
            "Ingrese la identificación del paciente: ")
        paciente = self.hospital.buscar_paciente(id_paciente)

        if paciente:
            console.print("Citas pendientes:")
            table = Table(title="Citas Pendientes")
            table.add_column("Motivo", style="magenta")
            table.add_column("Médico", style="green")
            table.add_column("Fecha", style="yellow")

            for cita in self.hospital.citas:
                if cita['paciente'] == paciente:
                    table.add_row(cita['motivo'],
                                  cita['medico'].nombre, cita['fecha'])

            console.print(table)
        else:
            console.print("[red]Paciente no encontrado.[/red]")

    def consultar_pacientes(self):
        console.print("\n--- Consultar Pacientes ---", style="bold")
        console.print("1. Buscar paciente por cédula")
        console.print("2. Mostrar todos los pacientes")
        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2"])

        if opcion == "1":
            id_paciente = self.obtener_dato(
                "Ingrese la identificación del paciente: ")
            paciente = self.hospital.buscar_paciente(id_paciente)
            if paciente:
                console.print(f"[blue]ID:[/blue] {paciente.id} [blue]Nombre:[/blue] {
                              paciente.nombre} [blue]Celular:[/blue] {paciente.celular} [blue]Correo:[/blue] {paciente.correo}")
            else:
                console.print("[red]Paciente no encontrado.[/red]")
        elif opcion == "2":
            if not self.hospital.pacientes:
                console.print("No hay pacientes registrados.")
            else:
                table = Table(title="Pacientes Registrados")
                table.add_column("ID", style="cyan")
                table.add_column("Nombre", style="magenta")
                table.add_column("Celular", style="green")
                table.add_column("Correo", style="yellow")

                for paciente in self.hospital.pacientes:
                    table.add_row(paciente.id, paciente.nombre,
                                  paciente.celular, paciente.correo)

                console.print(table)

    def consultar_medicos(self):
        console.print("\n--- Consultar Médicos ---", style="bold")
        console.print("1. Buscar médico por cédula")
        console.print("2. Mostrar todos los médicos")
        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2"])

        if opcion == "1":
            id_medico = self.obtener_dato(
                "Ingrese la identificación del médico: ")
            medico = self.hospital.buscar_medico(id_medico)
            if medico:
                console.print(f"[blue]ID:[/blue] {medico.id} [blue]Nombre:[/blue] {medico.nombre} [blue]Celular:[/blue] {
                              medico.celular} [blue]Especialidad:[/blue] {medico.especialidad}")
            else:
                console.print("[red]Médico no encontrado.[/red]")
        elif opcion == "2":
            if not self.hospital.medicos:
                console.print("No hay médicos registrados.")
            else:
                table = Table(title="Médicos Registrados")
                table.add_column("ID", style="cyan")
                table.add_column("Nombre", style="magenta")
                table.add_column("Celular", style="green")
                table.add_column("Especialidad", style="yellow")

                for medico in self.hospital.medicos:
                    table.add_row(medico.id, medico.nombre,
                                  medico.celular, medico.especialidad)

                console.print(table)

    def consultar_citas(self):
        console.print("\n--- Consultar Citas ---", style="bold")
        if not self.hospital.citas:
            console.print("No hay citas registradas.")
        else:
            table = Table(title="Citas Registradas")
            table.add_column("Motivo", style="magenta")
            table.add_column("Paciente", style="green")
            table.add_column("Médico", style="yellow")
            table.add_column("Fecha", style="blue")

            for cita in self.hospital.citas:
                table.add_row(cita['motivo'], cita['paciente'].nombre,
                              cita['medico'].nombre, cita['fecha'])

            console.print(table)


if __name__ == "__main__":
    app = Main()
    app.mostrar_menu()
