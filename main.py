import requests
from bs4 import BeautifulSoup
import pandas as pd
import webbrowser
url= 'https://www.pulzo.com/'
pulzo = requests.get(url)

s = BeautifulSoup(pulzo.text, 'lxml')
secciones = s.find('div', attrs ={'class':'container-temsDay'}).find_all('div', attrs ={'class':'container-tag'})
links_secciones = {seccion.a.get_text() : seccion.a.get("href") for seccion in secciones}

noticias = " "
for clave, valor in links_secciones.items():
    noticias+=f"<li><a href='{valor}'>"+clave+"</a></li>" 


f = open("index.html", "w")
mensaje = f"""<html>
<head></head>
<body><ul>{noticias}<ul></body>
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