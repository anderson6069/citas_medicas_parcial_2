import unittest
from app.persona import Persona, Medico, Paciente


class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("12345", "Juan Perez", "3216549870")

    def test_inicializacion_persona(self):
        self.assertEqual(self.persona.identificacion, "12345")
        self.assertEqual(self.persona.nombre, "Juan Perez")
        self.assertEqual(self.persona.celular, "3216549870")


class TestMedico(unittest.TestCase):
    def setUp(self):
        self.medico = Medico("54321", "Dr. Gomez", "3216541234", "Cardiología")

    def test_inicializacion_medico(self):
        self.assertEqual(self.medico.identificacion, "54321")
        self.assertEqual(self.medico.nombre, "Dr. Gomez")
        self.assertEqual(self.medico.celular, "3216541234")
        self.assertEqual(self.medico.especialidad, "Cardiología")


class TestPaciente(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("98765", "Ana Lopez",
                                 "3216549876", "ana@example.com")

    def test_inicializacion_paciente(self):
        self.assertEqual(self.paciente.identificacion, "98765")
        self.assertEqual(self.paciente.nombre, "Ana Lopez")
        self.assertEqual(self.paciente.celular, "3216549876")
        self.assertEqual(self.paciente.correo, "ana@example.com")

    def test_asignar_medico_preferencia(self):
        medico = Medico("54321", "Dr. Gomez", "3216541234", "Cardiología")
        self.paciente.asignar_medico_preferencia(medico)
        self.assertEqual(self.paciente.medico_preferencia, medico)


if __name__ == "__main__":
    unittest.main()
