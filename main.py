import requests
from bs4 import BeautifulSoup
import pandas as pd

url= 'https://www.pulzo.com/'
pulzo = requests.get(url)

s = BeautifulSoup(pulzo.text, 'lxml')
secciones = s.find('div', attrs ={'class':'container-temsDay'}).find_all('div', attrs ={'class':'container-tag'})
links_secciones = [seccion.a.get("href") for seccion in secciones]

sec=[]
for link in links_secciones:
  try:
    sec.append(requests.get(link))
  except Exception as e:
    print("Error")
    print(e)
    print('\n')

s_seccion = []
for s_s in sec:
  s_seccion.append(BeautifulSoup(s_s.text, 'lxml'))

print(s_seccion[0].prettify)