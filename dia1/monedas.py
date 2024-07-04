# CONVERTIR DE SOLES A DÓLARES
# CONVERTIR DE DÓLARES A SOLES
# ENTRADAS
TIPO_CAMBIO_COMPRA = 3.834
TIPO_CAMBIO_VENTA = 3.851
print("CONVERTIDOR DE MONEDAS 1.0")
print("""
      [1] CONVERTIR SOLES A DÓLARES
      [2] CONVERTIR DÓLARES A SOLES
      """)
opcion = input("ELIJA UNA OPCIÓN: ")

if(opcion == "1"):
  monto_origen = float(input("INGRESE EL MONTO EN SOLES: "))
  #print(type(monto_origen))
  #PROCESO
  monto_destino = monto_origen / TIPO_CAMBIO_VENTA
  #SALIDA
  print(f"EL MONTO EN DÓLARES ES {monto_destino}")
elif(opcion == "2"):
  monto_origen = float(input("INGRESE EL MONTO EN DÓLARES: "))
  #PROCESO
  monto_destino = monto_origen * TIPO_CAMBIO_COMPRA
  #SALIDA
  print(f"EL MONTO EN SOLES ES {monto_destino}")
else:
  print("OPCIÓN NO VÁLIDA")