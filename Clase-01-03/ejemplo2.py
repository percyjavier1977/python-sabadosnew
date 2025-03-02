USUARIO = "admin"
CLAVE = "1234"

USUARIO2 = "user"
CLAVE2 = "abcd"

USUARI03 = "root"
CLAVE3 = "5678"

usuario = input("Ingrese el usuario: ").lower()
clave = input("Ingrese la contraseña: ")


if (usuario == USUARIO and clave == CLAVE) or (usuario==USUARIO2 and clave == CLAVE2) or (usuario == USUARI03 and clave == CLAVE3):
    print("Acceso permitido")
else:
    print("Acceso denegado")
