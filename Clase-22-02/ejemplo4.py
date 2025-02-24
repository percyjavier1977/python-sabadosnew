'''
crear un programa donde ingersemos un numero y que muestre el dia de la semana.
'''

ndia = int(input("Ingrese un número entre 1 y 7: "))
bandera = 0

if ndia == 1:
    dia = "Lunes"
elif ndia == 2:
    dia = "Martes"
elif ndia == 3:
    dia = "Miércoles"
elif ndia == 4:
    dia = "Jueves"
elif ndia == 5 :
    dia = "Viernes"
elif ndia == 6:
    dia = "Sábado"
elif ndia == 7:
    dia = "Domingo"
else:
    bandera = 1

if bandera !=1:
    print("Ingresó el dia:",dia.upper())

else:
    print("Dia no existe")
    
print()    
    
if ndia >=1 and ndia <=7:
    print("Ingresó el dia:",dia.upper())
else:
    print("Dia no existe")