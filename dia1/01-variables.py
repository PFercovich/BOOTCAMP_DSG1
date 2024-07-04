# INPUTS(ENTRADAS)
numero1 = input("Ingrese nro 1: ")
numero2 = input("Ingrese nro 2: ")
print(type(numero1))

# PROCESO
numero1 = int(numero1)
print(type(numero1))
suma = numero1 + int(numero2)

# OUTPUT(SALIDA)
#print("la suma es ",suma)
print("La suma de "+ str(numero1) + " + " + numero2 + " es " + str(suma))