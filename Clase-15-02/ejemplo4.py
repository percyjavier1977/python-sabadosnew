'''
Crear un programa donde ingresemos el nombre del alumno, curso y sus tres notas
calcular el puntaje, promedio, nota máxima y nota mínima.
'''
print("===SISTEMA DE NOTAS=====")
print("Nombre del alumno:")
alumno = input()

print("Ingres el curso:")
curso = input()

print("Ingrese la NOTA 1:")
n1 = int(input())

print("Ingrese la NOTA 2:")
n2 = int(input())

print("Ingrese la NOTA 3:")
n3 = int(input())

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
