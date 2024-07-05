import os
import tabulate
import time

lista_empresas = [
  {
    'ruc': '987654',
    'razon_social': 'Las Viñas',
    'direccion': 'Av. Viñas #123'
  }
]

ANCHO = 50
opcion = 0
while(opcion < 5):
  os.system("clear")
  print("="*ANCHO)
  print(" "*10 + "CRUD DE EMPRESAS ")
  print("="*ANCHO)
  print("""
        [1] REGISTRAR EMPRESA
        [2] MOSTRAR EMPRESAS
        [3] ACTUALIZAR EMPRESA
        [4] ELIMINAR EMPRESA
        [5] SALIR
        """)
  print("="*ANCHO)

  opcion = int(input("INGRESE OPCION: "))
  os.system("clear")

  if(opcion == 1):
    print("="*ANCHO)
    print(" "*10 + "[1] REGISTRAR EMPRESA")
    print("="*ANCHO)
    ruc = input("RUC: ")
    razon_social = input("RAZÓN SOCIAL: ")
    direccion = input("DIRECCIÓN: ")
    dic_nueva_empresa = {
    'ruc': ruc,
    'razon_social': razon_social,
    'direccion': direccion
    }
    lista_empresas.append(dic_nueva_empresa)
    print("EMPRESA REGISTRADA CON ÉXITO")
  elif(opcion == 2):
    print("="*ANCHO)
    print(" "*10 + "[2] MOSTRAR EMPRESAS")
    print("="*ANCHO)
    cabeceras = ["RUC","RAZÓN SOCIAL","DIRECCIÓN"]
    tabla = [empresa.values() for empresa in lista_empresas]
    print(tabulate.tabulate(tabla,headers=cabeceras,tablefmt="grid"))
    input("presione ENTER para continuar...")
  elif(opcion == 3):
    print("="*ANCHO)
    print(" "*10 + "[3] ACTUALIZAR EMPRESA")
    print("="*ANCHO)
    valor_busqueda = input('INGRESE RUC DE LA EMPRESA A ACTUALIZAR: ')
    posicion_busqueda = -1
    for posicion in range(len(lista_empresas)):
      dic_empresa = lista_empresas[posicion]
      if valor_busqueda in dic_empresa.values():
        posicion_busqueda = posicion
        break
    if posicion_busqueda == -1:
      print("NO SE ENCONTRO LA EMPRESA SOLICITADA")
    else:
      print(f'EMPRESA A ACTUALIZAR: {lista_empresas[posicion_busqueda].get("ruc")}')
      nuevo_ruc = input("RUC: ")
      nueva_razon_social = input("RAZÓN SOCIAL: ")
      nueva_direccion = input("DIRECCIÓN: ")
      dic_actualizar_empresa = {
        'ruc':nuevo_ruc,
        'razon_social':nueva_razon_social,
        'direccion':nueva_direccion
      }
      lista_empresas[posicion_busqueda] = dic_actualizar_empresa
    print("EMPRESA ACTUALIZADA CON ÉXITO...")

  elif(opcion == 4):
    print("="*ANCHO)
    print(" "*10 + "[4] ELIMINAR EMPRESA")
    print("="*ANCHO)
    valor_busqueda = input('INGRESE RUC DE LA EMPRESA A ELIMINAR: ')
    posicion_busqueda = -1
    for posicion in range(len(lista_empresas)):
      dic_empresa = lista_empresas[posicion]
      if valor_busqueda in dic_empresa.values():
        posicion_busqueda = posicion
        break
    if posicion_busqueda == -1:
      print("NO SE ENCONTRO LA EMPRESA SOLICITADA")
    else:
      lista_empresas.pop(posicion_busqueda)
      print('EMPRESA ELIMINADA')
  elif(opcion == 5):
    print("="*ANCHO)
    print(" "*10 + "[5] SALIR")
    print("="*ANCHO)
  else:
    print("="*ANCHO)
    print(" "*10 + "OPCIÓN INVÁLIDA")
    print("="*ANCHO)
  time.sleep(1)
