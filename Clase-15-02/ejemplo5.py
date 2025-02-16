print("===SISTEMA DE NOTAS=====")
alumno = input("Nombre del alumno: ")
curso = input("Ingrese el curso: ")
n1 = int(input("Ingrese la NOTA 1:\n"))
n2 = int(input("Ingrese la NOTA 2:\n"))
n3 = int(input("Ingrese la NOTA 3:\n"))

#Formulas
puntaje = (n1+n2+n3)
promedio = puntaje / 3
nota_max = max(n1,n2,n3)
nota_min = min(n1,n2,n3)

#Salida de datos
print(f"Alumno------------------: {alumno.upper()}")
print(f"Alumno------------------: {alumno.title()}")
print(f"Curso-------------------: {curso.capitalize()}")
print(f"Notas ingresadas--------: {n1} | {n2} | {n3}")
print(f"Puntaje-----------------: {puntaje}")
print(f"Promedio----------------: {round(promedio,2)}")
print(f"Promedio----------------: {promedio:.2f}")
print(f"Nota máxima-------------: {nota_max}")
print(f"Nota mínima-------------: {nota_min}")
