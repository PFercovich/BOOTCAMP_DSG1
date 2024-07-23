import requests
import mysql.connector

def get_paises():
  url = 'https://restcountries.com/v3.1/all'
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
    print(response.json())
  else:
    print('error: ',response.status_code)
    return[]
  
def insert_paises_to_mysql(paises):
  connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='db_codigo'
  )

  if connection.is_connected():
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tbl_paises(
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   pais VARCHAR(255),
                   area VARCHAR(255)
                   )
                   """)
    
    for pais in paises:
      if pais['name']['common'] != '':
        nombre_pais = pais['name']['common']
      else:
        nombre_pais = ''
      '''if pais['capital'][0] != '':
        capital = pais['capital'][0]
      else:
        capital = ''
      '''
      area = pais['area']

      cursor.execute("""
                     INSERT INTO tbl_paises(pais,area)
                     value(%s,%s)
                     """,(nombre_pais,area))
      
      connection.commit()
    print('Paises insertados exitosamente')


paises = get_paises()
#print(type(paises))
#print(paises[0]['name']['common'])
#print(paises[0]['capital'][0])
#print(type(paises[0]))
insert_paises_to_mysql(paises)