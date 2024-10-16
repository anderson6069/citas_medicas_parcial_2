import unittest
from app.hospital import Hospital
from app.paciente import Paciente
from app.medico import Medico


class TestHospital(unittest.TestCase):

    def setUp(self):
        self.hospital = Hospital()

        self.paciente = Paciente(id=1, nombre="Juan Pérez")
        self.medico = Medico(nombre="Dr. García", especialidad="Cardiología")

        self.hospital.agregar_medico(self.medico)
        self.hospital.agregar_paciente(self.paciente)

    def test_agregar_medico(self):
        self.assertIn(self.medico, self.hospital.medicos)

    def test_agregar_paciente(self):
        self.assertIn(self.paciente, self.hospital.pacientes)

    def test_buscar_medico(self):
        medicos_encontrados = self.hospital.buscar_medico("Cardiología")
        self.assertIn(self.medico, medicos_encontrados)

    def test_buscar_paciente(self):
        paciente_encontrado = self.hospital.buscar_paciente(1)
        self.assertEqual(paciente_encontrado, self.paciente)

    def test_agendar_cita(self):
        fecha_hora = "2024-10-20 10:00:00"
        self.hospital.agendar_cita(
            self.paciente, self.medico, fecha_hora, "Consulta")
        self.assertEqual(len(self.hospital.citas), 1)

    def test_buscar_cita(self):
        fecha_hora = "2024-10-20 10:00:00"
        self.hospital.agendar_cita(self.paciente, self.medico, fecha_hora)
        citas_encontradas = self.hospital.buscar_cita(self.paciente)
        self.assertEqual(len(citas_encontradas), 1)
        self.assertEqual(citas_encontradas[0]['paciente'], self.paciente)


if __name__ == '__main__':
    unittest.main()
