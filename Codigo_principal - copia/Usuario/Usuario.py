from Monitoreo.Anses import *


class Usuario:
    tipo_usuario = ()

    def checkNombre(self, valor, tipo):
        nombre = input("Ingresar un nombre de usuario: ")
        check1 = Anses(tipo).confirmarNombre(nombre, tipo)
        while check1 == valor:
            nombre = input("Nombre de usuario incorrecto. Ingresar un nombre de usuario: ")
            check1 = Anses(tipo).confirmarNombre(nombre, tipo)
        return nombre

    def checkContra(self):
        contra = input("Ingresar una contraseña: ")
        contra2 = input("Vuelva a ingresar su contraseña: ")
        while contra != contra2:
            contra = input("Contraseñas distintas. Ingrese nuevamente su contraseña: ")
            contra2 = input("Vuelva a ingresar su contraseña: ")
        return contra

    def checkCuil(self, valor, tipo):
        cuil = input("Ingrese su CUIL: ")
        while Anses(tipo).confirmarCuil(cuil, tipo) == valor:
            cuil = input("CUIL incorrecto. Ingrese su CUIL: ")
        return cuil

    def checkTelef(self, valor, tipo):
        telef = input("Ingrese su número de teléfono: ")
        while Anses(tipo).confirmarTelef(telef, tipo) == valor:
            telef = input("Número de teléfono incorrecto. Ingrese su número de teléfono: ")
        return telef

    def registrar(self):
        nombre = Usuario().checkNombre(True, "ciudadano")
        contra = Usuario().checkContra()
        cuil = Usuario().checkCuil(True, "ciudadano")
        telef = Usuario().checkTelef(True, "ciudadano")

        zona = input("Ingrese su zona actual: ")

        Anses("ciudadano").agregarUsuario(nombre, contra, cuil, telef, zona, "ciudadano")

    def ingresar(self):
        tipo_usuario = input("¿Es usted ciudadano (c) o administrador (a)? ")
        ingreso = input("¿Desea ingresar por usuario (u), teléfono (t), o CUIL (c)? ")
        if tipo_usuario == "c":
            if ingreso == "u":
                nombre = Usuario().checkNombre(False, "ciudadano")
                contra = Usuario().checkContra()
                if nombre and contra:
                    print("Ingreso completo, bienvenido")
            elif ingreso == "t":
                telef = Usuario().checkTelef(False, "ciudadano")
                contra = Usuario().checkContra()
                if telef and contra:
                    print("Ingreso completo, bienvenido")
            elif ingreso == "c":
                cuil = Usuario().checkCuil(False, "ciudadano")
                contra = Usuario().checkContra()
                if cuil and contra:
                    print("Ingreso completo, bienvenido")
            tipo_usuario = ("ciudadano")

        elif tipo_usuario == "a":
            if ingreso == "u":
                nombre = Usuario().checkNombre(False, "admin")
                contra = Usuario().checkContra()
                if nombre and contra:
                    print("Ingreso completo, bienvenido")
            elif ingreso == "t":
                telef = Usuario().checkTelef(False, "admin")
                contra = Usuario().checkContra()
                if telef and contra:
                    print("Ingreso completo, bienvenido")
            elif ingreso == "c":
                cuil = Usuario().checkCuil(False, "admin")
                contra = Usuario().checkContra()
                if cuil and contra:
                    print("Ingreso completo, bienvenido")
            tipo_usuario = ("administrador")
