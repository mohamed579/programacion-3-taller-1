#Hacer un programa que te pregunte cual es tu nombre y si le pones un nombre falso, el programa no lo acepte
#-----------------------------------------------------------

#importando el modulo para usar casos de prueba
import unittest

class Taller1(unittest.TestCase):
    #preparando el set de datos a validar
    def setUp(self):
        #se solicita al usuario que introduzca un nombre
        self.name = input("Validacion de nombre para el acceso.\n\nCual es tu nombre? --> ")
    
    #ejecutando el test
    def test_nombre(self):
        #se especifica el nombre que debe aceptar la aplicacion
        self.assertEqual(self.name, 'Mohamed')

    #borrando el set de datos
    def tearDown(self):
        del(self.name)

if __name__ == '__main__':
    unittest.main()