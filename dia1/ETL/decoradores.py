def asteriscos(func):
  def envoltura():
    print('*'*30)
    func()
    print('*'*30)
  return envoltura

@asteriscos
def saludo():
  print("hola mundo")

#saludo = asteriscos(saludo)
saludo()
