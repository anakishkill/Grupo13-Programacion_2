import csv


class Manager:
    def validarCiudadano(self):
        pass


class Anses:
    #Diferenciamos si es ciudadano o admin con la variable tipo
    def __init__(self, tipo):
        self.tipo = tipo

    def confirmacion(self, dato, num):
        with open(f"../Database/DB_{self.tipo}.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            for linea in reader:
                if dato == linea[num]:
                    return True
            return False

    def confirmarNombre(self, nombre):
        return Anses(self.tipo).confirmacion(nombre, 0)

    def confirmarCuil(self, cuil):
        return Anses(self.tipo).confirmacion(cuil, 2)

    def confirmarTelef(self, telef):
        return Anses(self.tipo).confirmacion(telef, 3)

    def confirmarZona(self, zona):
        return Anses(self.tipo).confirmacion(zona, 4)

    def agregarUsuario(self, nombre, contrasena, cuil, telef, zona):
        a = Anses("ciudadano").confirmarCuil(cuil)
        b = Anses("ciudadano").confirmarTelef(telef)
        c = Anses("ciudadano").confirmarNombre(nombre)
        if a or b or c:
            return print("Datos ya usados, intentelo de nuevo")
        else:
            f = open("../Database/DB_ciudadano.csv", "a", newline="")
            writer = csv.writer(f)
            tupla_nueva = (nombre, contrasena, cuil, telef, zona, "Desbloqueado")
            writer.writerow(tupla_nueva)
            f.close()
