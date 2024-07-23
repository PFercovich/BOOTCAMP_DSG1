import requests
from bs4 import BeautifulSoup

url = "https://www.sunat.gob.pe/"
#url = "https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx"
#url = "https://elperuano.pe/"
#url = "https://www.google.com/finance/quote/PEN-USD?sa=X&ved=2ahUKEwjYpcby2baHAxXgF7kGHY7gBb0QmY0JegQIFxAp"
#url = "https://cuantoestaeldolar.pe/"
#url = "https://www.sbs.gob.pe/app/pp/sistip_portal/paginas/publicacion/tipocambiopromedio.aspx"
#url = "https://kambista.com/tipo-de-cambio/"
url = "https://www.bcrp.gob.pe/"

def obtener_tipocambio():
  response = requests.get(url)
  if(response.status_code  == 200):
    #print(response.text)
    #content = response.content#
    #soup = BeautifulSoup(content)
    #file = open('prueba.html','wb')#
    #file.write(content)#
    #file.close#
    html = BeautifulSoup(response.text,'html.parser')
    """ul_dolar = html.find('strong',{'id':'sell-rate'})
    print(ul_dolar.get_text())"""
    #id = html.select('#sell-rate')
    #print(id[0].get_text())
    #tabla = html.find('table',{"class":"tip-table"})
    #dolar = html.find('li',{'class':'compra'})
    #dolar = html.find_all('ul')
    #dolar = html.find('li')
    #dolar = html.find('li',string='Compra: 3.736')
    
    #tabtc = html.find('tipo-de-cambio')

    #texto = html.get_text()
    #objetivo = texto.find(text='Compra:')

    #print(html)
    #print(html.find('strong id='))
    """id = html.select('#valcompra')
    print(id[0].get_text())"""
    #print(html)

    print(html.prettify())
    #print(html.title)
    
    """print(html.get_text())
    var = html.get_text().find('Compra:')
    print(var)
    print(type(var))"""

    #print(html.select('div'))
    #print(objetivo)
    #print(html.get_text(separator=' / '))

    #print(content)#
    #print(soup)#
    #print(dolar)
    #print(dolar.text)
    #print(tabtc)
  else:
    print(f"error: {response.status_code}")
  
if __name__ == "__main__":
  obtener_tipocambio()