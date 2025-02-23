'''
Crear un programa donde ingresemos el nombre del alumno, el curso y tres notas
debemos calcular el puntaje, promedio, nota máxima, nota mínima y una observación
'''
alumno = input("Ingrese el nombre del alumno: ").upper()
curso = input("Ingres el curso: ").upper()

n1 = float(input("Ingrese la nota 1: "))
n2 = float(input("Ingrese la nota 2: "))
n3 = float(input("Ingrese la nota 3: "))

#Formulas
puntaje = n1+n2+n3
promedio = puntaje / 3

nota_max = max(n1,n2,n3)
nota_min = min(n1,n2,n3)

#Observación: Si tiene un promedio mayor a 10 debe mostrar "Aprobado", de contrario "Desaprobado"
promedio = round(promedio,0)
if promedio>10:
    #Verdad
    obs = "Aprobado"
else:
    #Falsa
    obs = "Desaprobado"
    
#Mostrar los resultados
print("======BOLETA DE NOTAS=======")
print(f"Nombre del alumno: {alumno}")
print(f"Curso: {curso}")
print(f"Notas ingresadas: {n1} | {n2} | {n3}")
print(f"Puntaje: {puntaje} ")
print(f"Promedio: {promedio}")
print(f"Nota Máxima: {nota_max} | Nota Mínima: {nota_min}")
print(f"Observación: {obs}")