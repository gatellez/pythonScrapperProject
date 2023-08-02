import requests
from bs4 import BeautifulSoup
import pandas as pd
import webbrowser


url= 'https://www.larepublica.co/'
pulzo = requests.get(url)

s = BeautifulSoup(pulzo.text, 'lxml')
secciones = s.find('ul', attrs ={'class':'tags'}).find_all('li')
try:
    links_secciones = {seccion.a.get_text() : seccion.a.get("href") for seccion in secciones if seccion.a }
except:
    pass



noticias = " "
for clave, valor in links_secciones.items():
    noticias+=f"<li><a href='{valor}'>"+clave+"</a></li>" 


f = open("index.html", "w")
mensaje = f"""<html>
<head></head>
<body><ol>{noticias}<ol></body>
</html>"""

f.write(mensaje)
f.close()
webbrowser.open_new_tab("index.html")





#for articulo in links_secciones:
#    print(['-'*100])
#    print (articulo)
#    print(['-'*100])

#sec=[]
#for link in links_secciones:
#  try:
#    sec.append(requests.get(link))
#  except Exception as e:
#    print("Error")
#    print(e)
#    print('\n')

#s_seccion = []
#for s_s in sec:
#  s_seccion.append(BeautifulSoup(s_s.text, 'lxml'))

#print(s_seccion[0].prettify)