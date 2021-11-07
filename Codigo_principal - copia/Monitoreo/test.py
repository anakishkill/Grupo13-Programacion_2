import unittest

from Anses import *
#from Monitoreo.Evento import *
#from Monitoreo.Sensores import *
#from Monitoreo.Solicitudes import *

#from Usuario.Administrador import *
#from Usuario.Ciudadano import *
#from Usuario.Usuario import *

class TestAnses(unittest.TestCase):
    @classmethod
    def test_ansesconfimar(self):
        result = Anses().confirmarCuil("01-44000000-1")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
