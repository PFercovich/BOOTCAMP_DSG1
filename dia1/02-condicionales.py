#ENTRADA
print("MI CALCULADORA")
numero1 = input("Numero 1: ")
numero2 = input("Numero 2: ")
operacion = input("Ingrese el tipo de operación(suma|resta): ")

#PROCESO
if(operacion == "suma"):
  resultado = int(numero1) + int(numero2)
elif:
  resultado = int(numero1) - int(numero2)
else:
  print("Operación no existe")
  exit()

#SALIDA
print(f"El resultado es {resultado}")
