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



#importation des packages python
import requests 
from bs4 import BeautifulSoup
import csv 

#création d'une liste de pages de toute la catégorie mystery
travel = ["books.toscrape.com/catalogue/category/books/travel_2/index.html"]
mystery = ["http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html","http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html"]

#boucle à travers chaques pages de la catégorie mystery
for i in mystery:
    response = requests.get(mystery)
    page = response.content
    soup = BeautifulSoup(page, "html.parser")
    print(page)
    #trouver tout les liens des livres sur chaques pages de la categorie
    i_data = soup.find_all("h3")
    for j in i_data:
        infos = j.find("a")["href"]
        url_livre = "http://books.toscrape.com/catalogue/" + infos

        #for k in url_livre:
        # #collecte des informations par BeautifulSoup
        # url_produit = url_livre
        # upc = soup.find("table",{"class":"table table-striped"}).find_all("td")[0].get_text()
        # titre = soup.h1.get_text()
        # prix_avec_taxes = soup.find("table", {"class":"table-striped"}).find_all("td")[3].get_text()
        # prix_sans_taxes = soup.find("table", {"class":"table-striped"}).find_all("td")[2].get_text()
        # nombre_disponible = soup.find("table", {"class":"table-striped"}).find_all("td")[5].get_text()
        # description_produit = soup.find("h2").find_next("p").get_text()
        # categorie = soup.find("ul", {"class":"breadcrumb"}).find_all("a")[2].get_text()
        # note_evaluation = soup.find("table", {"class":"table-striped"}).find_all("td")[6].get_text()

        # base_image_url = soup.find("div", {"class":"item active"}).find_next("img")["src"]
        # image_url = "http://books.toscrape.com" + base_image_url

        # #creation d'un dictionnaire pour enregister les données du livre
        # donnee_livre = {
        #     "url_produit":url_produit,
        #     "upc":upc,
        #     "titre":titre,
        #     "prix_avec_taxes":prix_avec_taxes,
        #     "prix_sans_taxes":prix_sans_taxes,
        #     "nombre_disponibilite":nombre_disponible,
        #     "description_produit":description_produit,
        #     "nom_categorie":categorie,
        #     "note_evaluation":note_evaluation,
        #     "url_image":image_url
        # }




# #création d'un fichier CSV 
# with open ("mystery.csv", "w" ) as csvfile:
#     writer = csv.writer(csvfile)








