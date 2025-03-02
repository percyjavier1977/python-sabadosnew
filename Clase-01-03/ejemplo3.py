print("====CLINICA EL ANGEL=====")
paciente = input("Ingrese el nombre del paciente: ").upper()
print(f"Bienvenido a la clinica en 'EL ANGEL' estimado {paciente}")
peso = float(input("Ingrese su peso(KL): "))
altura = float(input("Ingrese su altura(M): "))

imc = peso /  (altura ** 2)

print(f"Tu IMC es: {imc:.2f}")

if imc <18.5:
    obs = "BAJO PESO"
elif imc >=18.5 and imc <=24.9:
    obs = "PESO NORMAL"
elif imc >=25 and imc <=29.9:
    obs = "SOBRE PESO"
elif imc >=30 and imc <=34.9:
    obs = "OBESIDAD GRADO 1"
elif imc >=35  and imc <=39.9:
    obs = "OBESIDAD GRADO 2"
else:
    obs = "OBESIDAD GRADO 3 (Mórbida)" 

print(f"Clasificación: {obs}")

if imc <18.5:
    obs = "BAJO PESO"
elif 18.5<= imc <=24.9:
    obs = "PESO NORMAL"
elif 25<= imc <=29.9:
    obs = "SOBRE PESO"
elif 30<= imc <=34.9:
    obs = "OBESIDAD GRADO 1"
elif 35<= imc <=39.9:
    obs = "OBESIDAD GRADO 2"
else:
    obs = "OBESIDAD GRADO 3 (Mórbida)" 

print(f"Clasificación: {obs}")