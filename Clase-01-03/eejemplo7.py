
import random
numero_suerte = random.randint(1,10)


intentos = 3

for i in range(intentos):
    numero = int(input(f"Intento:{i+1}... Adivina el número de la surte: (1-5): "))
     
    if numero == numero_suerte:
        print("¡Felicidades..adivinaste el número!")
        break
    else:
        if i < 2:
            print("Intente otra ves")
else:
    #Solo sale cuando se cumplen todos los bucles
    print(f"Lo siento el número de la suerte era {numero_suerte}. ¡Intentalo otra vez!")

