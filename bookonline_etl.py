'''  ____                       __                   _____                ___                              
    /\  _`\                    /\ \                 /\  __`\             /\_ \      __                     
    \ \ \L\ \    ___     ___   \ \ \/'\             \ \ \/\ \     ___    \//\ \    /\_\     ___       __   
     \ \  _ <'  / __`\  / __`\  \ \ , <     _______  \ \ \ \ \  /' _ `\    \ \ \   \/\ \  /' _ `\   /'__`\ 
      \ \ \L\ \/\ \L\ \/\ \L\ \  \ \ \\`\  /\______\  \ \ \_\ \ /\ \/\ \    \_\ \_  \ \ \ /\ \/\ \ /\  __/ 
       \ \____/\ \____/\ \____/   \ \_\ \_\\/______/   \ \_____\\ \_\ \_\   /\____\  \ \_\\ \_\ \_\\ \____\
        \/___/  \/___/  \/___/     \/_/\/_/             \/_____/ \/_/\/_/   \/____/   \/_/ \/_/\/_/ \/____/
                                                                                                       

____ _   _ ____ ___ ____ _  _ ____    ___  ____    ____ _  _ ____ _  _ ____ _ _    _    ____ _  _ ____ ____
[__   \_/  [__   |  |___ |\/| |___    |  \ |___    [__  |  | |__/ |  | |___ | |    |    |__| |\ | |    |___
___]   |   ___]  |  |___ |  | |___    |__/ |___    ___] |__| |  \  \/  |___ | |___ |___ |  | | \| |___ |___'''

#importation package py 
import requests
from bs4 import BeautifulSoup
import csv 


product_page = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(product_page)
page = response.content

soup = BeautifulSoup(page, "html.parser")

produit_url = product_page
upc = soup.find("table").find_all("td")[0].get_text()
titre_livre = soup.find("h1").get_text()
prix_incluant_taxes = soup.find("table").find_all("td")[3].get_text()
prix_excluant_taxes = soup.find("table").find_all("td")[2].get_text()
exemplaire_disponible = soup.find("table").find_all("td")[5].get_text()
description_livre = soup.find("h2").find_next("p").get_text()
categorie = soup.find("ul", {"class":"breadcrumb"}).find_all("a")[-1].get_text()
nombre_avis = soup.find("table").find_all("td")[6].get_text()

base_url_image = soup.find("div", {"class":"item active"}).find_next("img")["src"]
image_url = "http://books.toscrape.com/catalogue/" + base_url_image

donnee_livre = {"produit_url":produit_url , 
                "upc": upc, 
                "titre_livre":titre_livre, 
                "prix_incluant_taxes":prix_incluant_taxes,
                "prix_excluant_taxes":prix_excluant_taxes, 
                "exemplaire_disponible":exemplaire_disponible,
                "description_livre":description_livre,
                "categorie":categorie,
                "nombre_avis":nombre_avis,
                "image_url":image_url,
}

#creation d'une liste pour les en-tête
en_tete = ["product_page_url","universal_ product_code (upc)","title","price_including_tax",
            "price_excluding_tax","number_available","product_description","category","review_rating", 
            "image_url",]

#création d'un fichier csv pour écrire dans le fichier appelé data.csv
with open("data.csv", "w") as fichier_csv:
    #création d'un objet writer pour ce fichier avec un délimiteur
    writer = csv.writer(fichier_csv, delimiter=',')
    #création de la premiere ligne du fichier avec writer.writerow
    writer.writerow(en_tete)
    #boucle qui parcours les données -zip et permet d'itérer
    for elt in zip(donnee_livre):
        writer.writerow([donnee_livre])

