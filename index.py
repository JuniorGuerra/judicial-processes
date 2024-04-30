import requests
from bs4 import BeautifulSoup

print("ejecutando programa")

# URL de la página que quieres raspar
url = "https://lanacionweb.com/tecnologia/"

# Realizar la solicitud GET a la página
response = requests.get(url)

# Verificar que la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Encontrar todos los divs que contienen los enlaces
    divs = soup.find_all("div", class_="brxe-jmzlhj")

    # Iterar sobre los divs y obtener los enlaces
    for div in divs:
        # Encontrar todos los enlaces dentro del div
        links = div.find_all("a")
        # Iterar sobre los enlaces y seguirlos
        for link in links:
            # Obtener la URL del enlace
            enlace = link.get("href")
            # Hacer algo con la URL, como seguir el enlace
            print("Enlace encontrado:", enlace)
else:
    print("La solicitud no fue exitosa. Código de estado:", response.status_code)
