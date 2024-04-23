import unittest

def buscar_datos(*args, **kwargs):
    for key , value in kwargs.items():
        existe = True
        for i, n in value.items():
            if n not in args:
                existe = False
        if existe:
            return key
    return "La persona no esta en la base de datos"
     
database = {
    "persona1":{
        "primer_nombre":"Lucas",
        "segundo_nombre": "Gerardo",
        "primer_apellido": "Zapata",
        "segundo_apellido": "Campanello", 

     },
    "persona2": {
        "primer_nombre": "Ruben",
        "segundo_nombre": "Dario",
        "primer_apellido": "Insua",

     },
    "persona3": {
        "primer_nombre": "Leandro",
        "segundo_nombre": "Atilio",
        "primer_apellido": "Romagnoli",
       
    },
    "persona4": {
        "primer_nombre": "Martin",
        "segundo_nombre": "Ignacio",
        "primer_apellido": "Tarantoviez",
       
    },
    "persona5": {
        "primer_nombre": "Mariano",
        "segundo_nombre": "Agustin",
        "primer_apellido": "Lopez",
       
    }

}
   
   
class TestKwargs(unittest.TestCase):

    def test_persona1(self):
        resultado = buscar_datos("Lucas", "Gerardo", "Zapata", "Campanello",**database)
        self.assertEqual(resultado,"persona1")

    def test_no_existe_la_persona(self):
        resultado = buscar_datos("Anibal", "Roberto", "Fernandez", **database)
        self.assertEqual(resultado,"La persona no esta en la base de datos")
    
    def test_persona3(self):
        resultado = buscar_datos("Leandro", "Atilio","Romagnoli",**database)
        self.assertEqual(resultado,"persona3")

    def test_persona2(self):
        resultado = buscar_datos("Ruben", "Dario", "Insua", **database)
        self.assertEqual(resultado,"persona2")


    def test_persona4(self):
        resultado = buscar_datos("Martin", "Ignacio","Tarantoviez",**database)
        self.assertEqual(resultado,"persona4")

    def test_persona5(self):
        resultado = buscar_datos("Mariano", "Agustin","Lopez",**database)
        self.assertEqual(resultado,"persona5")

    def test_no_existe_la_persona_2(self):
        resultado = buscar_datos("Roberto", "Nahuel","Barrios", "Hernandez", **database)
        self.assertEqual(resultado,"La persona no esta en la base de datos")

unittest.main()