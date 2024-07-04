# Convertidor de monedas soles/dólares
print("Conversor Soles / Dólares")
cantidad = input("La cantidad a convertir es: ")
operacion = input ("¿Convertir: Soles a Dólares (1) ó Dólares a Soles (2)? ")
tipo_cambio = 3.8

if(operacion == "1"):
  convertido = float(cantidad) / tipo_cambio
  print(f"{cantidad} soles son {round(convertido,2)} dólares (tipo de cambio = {tipo_cambio})")
elif(operacion == "2"):
  convertido = float(cantidad) * tipo_cambio
  print(f"{cantidad} dólares son {convertido} soles (tipo de cambio = {tipo_cambio})")
else:
  print("Operación inválida, reinicie la aplicación.")
  exit()