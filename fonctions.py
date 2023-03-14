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

url_test = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"

#Fonction qui permets d'extraire les données d'un livre sur une page produit 
def extract_book_data(book_url):
    response = requests.get(book_url)
    page = response.content

    soup = BeautifulSoup(page, "html.parser")

    produit_url = book_url
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

    #creation d'une liste pour le stockage de toutes les donnees d'un livre
    donnee_livre = [produit_url, upc, titre_livre, prix_incluant_taxes, prix_excluant_taxes, 
                    exemplaire_disponible, description_livre, categorie, nombre_avis, image_url]

    return donnee_livre

#fonction qui permets de trouver les liens de la page index.html pour les differentes categories
def get_url_categories(index_url):
    response = requests.get(index_url)
    page = response.content
    soup = BeautifulSoup(page, "html.parser")

    #création d'une liste pour recupérer les urls incompletes de la page web
    pages_categories = []
    #création d'une liste pour reconstruire les urls complétes des catégories
    pages_categories_full = []
    #Recuperer toutes les adresses urls des Categories
    infos_categories = soup.find("ul",{"class":"nav nav-list"}).find_all("a")
    #Création d'une boucle pour récupérer tout les "href" des balises <a>
    for i in infos_categories:
        linkfound = i.get('href')
        pages_categories.append(linkfound)
    #création d'une boucle pour reconstituer les urls completes des catégories
    for u in pages_categories :
        full_url = "http://books.toscrape.com/" + str(u)
        pages_categories_full.append(full_url)
   
    return pages_categories_full








# if __name__ == "__main__":
#     product_page = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
#     #creation d'une liste pour les en-tête
#     book_data = extract_book_data(product_page)
#     print(book_data)
