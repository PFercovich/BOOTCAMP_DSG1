import requests
import mysql.connector

def get_pokemons(count):
  url = f'https://pokeapi.co/api/v2/pokemon/{count}'
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
    
  else:
    print('error: ',response.status_code)
    return[]
  
def insert_pokemons_to_mysql(pokemons):
  connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='db_codigo'
  )

  if connection.is_connected():
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tbl_pokemon(
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   nombre VARCHAR(255),
                   imagen VARCHAR(255),
                   habilidad VARCHAR(255)
                   )
                   """)
    pokemons2 = pokemons["forms"]
    pokemons3 = pokemons["abilities"]
    print(type(pokemons3))
    pokemons4 = pokemons["sprites"]
    for pokemon in pokemons2:
      nombre=pokemon['name']
      imagen=pokemons4['front_default']
      print(nombre)
      print(imagen)
      habilidad=pokemons3[0]['ability']['name']
      
      print(habilidad)

      cursor.execute("""
                    INSERT INTO tbl_pokemon(nombre,imagen,habilidad)
                    values(%s,%s,%s)
                    """,(nombre,imagen,habilidad))
      
      connection.commit()
    print('Pokemones insertados exitosamente')

for i in range(1,151,1):
  pokemones = get_pokemons(i)
  insert_pokemons_to_mysql(pokemones)