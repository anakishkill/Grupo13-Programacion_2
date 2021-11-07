from io import open
import csv

class Manager:
    def validarCiudadano(self):
        pass


class Anses:
    def confirmacion(self, dato, num):
        with open("DB_usuario.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            for linea in reader:
                if dato == linea[num]:
                    return True
            return False


    def confirmarCuil(self, cuil):
        return Anses().confirmacion(cuil, 0)

    def confirmarTelef(self, telef):
        return Anses().confirmacion(telef, 1)

    def confirmarZona(self, zona):
        return Anses().confirmacion(zona, 3)

    def agregarDato(self, cuil, telef, zona):
        a = Anses().confirmarCuil(cuil)
        b = Anses().confirmarTelef(telef)
        if a or b:
            return print("Datos ya usados, intentelo de nuevo")
        else:
            f = open("DB_usuario.csv", "a", newline="")
            writer = csv.writer(f)
            tupla_nueva = (cuil, telef, zona)
            writer.writerow(tupla_nueva)
            f.close()
