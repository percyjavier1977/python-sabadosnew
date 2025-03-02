
#Mostrar solo los numero impares del 1 al 10
for i in range(1,11,2):
    print(i)
    
print("----------------------")
#Mostrar solo los número pares del 1 al 10
for i in range(2,11,2):
    print(i)

print("----------------------")

for i in range(1,11):
    if i % 2 == 0:
        print(i)
        
#hacer la sumatorio de un número ingresado
suma = 0
n = int(input("Ingrese un número: "))        
for i in range(1,n+1):
    #suma = suma + i
    suma +=i


print(f"la sumarotia de {n} es: {suma}")