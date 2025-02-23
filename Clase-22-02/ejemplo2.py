#Mostrar si un número ingresado es par o impar


numero = int(input("Ingrese un número que se mayor a cero:\n"))
if numero == 0:
    print("Ingresaste cero")
else:
    if numero % 2 == 0:
        print("Número par")
    else:
        print("Número impar")

print()


    
if numero == 0:
    mensaje = "Ingresaste cero"
elif numero % 2 == 0:
    mensaje = "Número Par"
else:
    mensaje = "Número Impar"

print(mensaje)
