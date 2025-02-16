a = 10
b = 8

mayor = a > b
menor = a < b
igual = a == b
diferente = a != b

operador_y = a + b == 18 and a * b == 80 and a > b
operador_o = a + b == 15 or a * b == 50 or a < b


#Salidad de datos
print("")

print(f"¿El número {a} es mayor que el número {b}? RESPUESTA: {mayor}")
#print("¿El numero",a,"es mayor que el numero",b,"?")
print(f"¿El número {a} es menor que el número {b}? RESPUESTA: {menor}")
print(f"¿El número {a} es igual que el número {b}? RESPUESTA: {igual}")
print(f"¿El número {a} es diferente que el número {b}? RESPUESTA: {diferente}")
print("La respuesta es:",operador_y)
print("La respuesta es:",operador_o)