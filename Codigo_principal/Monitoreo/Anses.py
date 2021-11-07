from io import open

class Manager:
    def validarCiudadano(self):
        pass


class Anses:
    def confirmacion(self, dato):
        with open("Doc_anses.txt", "r") as file:
            l = file.readlines()
            for i in l:
                if i == f"{dato}\n":
                    return True
            return False

    def confirmarCuil(self, cuil):
        return Anses().confirmacion(cuil)

    def confirmarTelef(self, telef):
        return Anses().confirmacion(telef)

    def confirmarZona(self, zona):
        return Anses().confirmacion(zona)

    def agregarDato(self, cuil, telef, zona):
        a = Anses().confirmarCuil(cuil)
        b = Anses().confirmarTelef(telef)
        if a or b:
            return print("Datos ya usados, intentelo de nuevo")
        else:
            with open("Doc_anses.txt", "a") as file:
                C = f"\n{cuil}"
                T = f"\n{telef}"
                Z = f"\n{zona}"
                file.write(C)
                file.write(T)
                file.write(Z)
                file.close()
