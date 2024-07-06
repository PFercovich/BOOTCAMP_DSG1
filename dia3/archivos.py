f = open('alumnos.txt','w')
f.write('Pedro Fercovich,pedro@gmail.com,123456')
f.close()

fa = open('alumnos.txt','a')
fa.write('\n')
fa.write('ana martinez,ana@gmail.com,1234')
fa.close()

fr = open('alumnos.txt','r')
data_alumnos = fr.read()
print(data_alumnos)
print(type(data_alumnos))
fr.close()

#print("archivo creado")