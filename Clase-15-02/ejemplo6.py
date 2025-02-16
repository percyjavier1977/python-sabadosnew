'''
Crear un programa donde ingresemos, el nombre del cliente, producto, cantidad, precio
debemos calcular el importe, el descuento y total a pagar
'''

print("======SISTE DE SUPERMERCADO======")
cliente = input("Nombre del cliente:\n").upper()
producto = input("Producto:\n").upper()
cantidad = int(input("Ingrese la cantidad:\n"))
precio = float(input("Ingrese el precio unitario:\n"))

#Formulas

importe = cantidad * precio
#Descuento: Se aplica el 2% solo alos cliente con un importe superior a 300 soles
if importe > 300:
    #Verdadera
    descuento = 2/100 * importe
    

tpago = importe - descuento

#Salidad de datos
print("====DETALLE DE LA VENTA=====")
print(f"Cliente--------------------------: {cliente}")
print(f"Producto-------------------------: {producto}")
print(f"Cantidad comprada----------------: {cantidad}")
print(f"Precio unitario------------------: S/{precio:.2f}")
print(f"Importe--------------------------: S/{importe:.2f}")
print(f"Descuento:-----------------------: S/{descuento:.2f}")
print(f"Total a pagar--------------------: S/{tpago:.2f}")

