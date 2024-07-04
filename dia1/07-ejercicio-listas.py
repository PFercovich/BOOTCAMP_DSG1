#Ingresar una lista de 5 números y retornar el número mayor de la lista

numeros = []
for contador in range(1,6):
  nuevo_numero = int(input(f'Ingrese nro {contador}: '))
  numeros.append(nuevo_numero)

numero_mayor = numeros[0]
for numero in numeros:
  if(numero > numero_mayor):
    numero_mayor = numero 
print(numeros)
print(f'El número mayor es {numero_mayor}')
print(f'El número mayor es {max(numeros)}')
print(f'El número menor es {min(numeros)}')

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)
