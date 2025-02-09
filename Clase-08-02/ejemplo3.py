#Formas de usar el print
nombre = "juan gonzales"
edad = 25
peso = 75.8
altura = 1.78
aprobado =True
amiga = "Rosario"

print(nombre)
print("Hola bienvenido: " + nombre)
print("Es verdad que tienes " +  str(edad)  + " años")
print("Es verdad que tienes",edad,"años?")
print("Hola mi nombre es {} y tengo {} años, y peso {} kilos".format(nombre,edad,peso))
print(f"Hola mi nombre es {nombre} y tengo {edad} años, y peso {peso} kilos \ny estoy aqui con mi amiga {amiga}")

print("Hola mi nombre es",nombre,"y tengo",edad,"años,","y peso",peso,"kilos")

print(type(aprobado))
print("Es un tipo de dato:", type(aprobado))
print(f"Este tipo de dato es {type(aprobado)}")

type(nombre)

