

respuesta = input("¿Ingresó la tarjeta s/n:? ").lower()
if respuesta == "s":
    for i in range(1,4):
        CONTRASEÑA = 12345
        contra = int(input(f"INTENTO N° {i}... Ingrese su contraseña: "))
        if contra == CONTRASEÑA:
            
            print("Contraseña correcta..")
            print("====OPCIONES====")
            print("1.CONSULTAR")
            print("2.RETIRAR")
            print("3.DEPOSITAR")
            break
        else:
            print("Contraseña incorrecta")
        

    else:
        print("¡tarjeta Bloqueada!")
        
else:
    print("Ingrese su tarjeta")