import unittest
from app.cita import Cita
from app.paciente import Paciente
from app.medico import Medico


class TestCita(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente(nombre="Juan Pérez")
        self.medico = Medico(nombre="Dr. García")

        self.fecha_hora = "2024-10-20 10:00:00"
        self.motivo = "Consulta general"

        self.cita = Cita(self.paciente, self.medico,
                         self.fecha_hora, self.motivo)

    def test_mover_cita(self):
        nueva_fecha_hora = "2024-10-21 11:00:00"
        self.cita.mover_cita(nueva_fecha_hora)
        self.assertEqual(self.cita.fecha_hora, nueva_fecha_hora)

    def test_recordatorio_cita(self):
        with self.assertLogs(level='INFO') as log:
            self.cita.recordatorio_cita()
            self.assertIn(f"Enviando notificación al paciente {
                          self.paciente.nombre}", log.output[0])

    def test_reprogramar_cita_disponible(self):
        self.medico.verificar_disponibilidad = lambda x: True  # Simular que está disponible
        nueva_fecha = "2024-10-22 09:00:00"
        self.cita.reprogramar_cita(nueva_fecha)
        self.assertEqual(self.cita.fecha_hora, nueva_fecha)

    def test_reprogramar_cita_no_disponible(self):
        # Simular que no está disponible
        self.medico.verificar_disponibilidad = lambda x: False
        nueva_fecha = "2024-10-23 09:00:00"
        self.cita.reprogramar_cita(nueva_fecha)
        self.assertNotEqual(self.cita.fecha_hora, nueva_fecha)

    def test_cancelar_cita(self):
        motivo_cancelacion = "No puedo asistir"
        self.cita.cancelar_cita(motivo_cancelacion)
        self.assertEqual(self.cita.motivo_cancelacion, motivo_cancelacion)

    def test_repr(self):
        expected_repr = f"Cita del paciente {self.paciente.nombre} con el Dr. {
            self.medico.nombre} programada para el {self.fecha_hora}"
        self.assertEqual(repr(self.cita), expected_repr)


if __name__ == '__main__':
    unittest.main()
