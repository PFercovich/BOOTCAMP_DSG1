# De las siguiente lista retorna los números pares
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

pares = []
for numero in numeros:
  if (numero%2 == 0):
    pares.append(numero)

print(pares)

#LIST COMPREHENSIONS
pares2 = [numero for numero in numeros if numero % 2 == 0]
print(pares2)