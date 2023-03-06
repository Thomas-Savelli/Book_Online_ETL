#importation des packages python
import requests
from bs4 import BeautifulSoup
import csv 


#création d'une fonction permettant de collecter toutes les informations voulues sur la page d'un produit (livre)
def extraction_donnee_livre (livre_url):
    response = requests.get(livre_url)
    page = response.content
    soup = BeautifulSoup(page, "html.parser")

    page_product_url = response.url
   
    title = soup.h1.get_text()

    categorie_tag = soup.find("ul", {"class":"breadcrumb"}).find_all("a")
    categorie = categorie_tag[-1].get_text()

    product_description = soup.find("div", {"id": "product_description"}).find_next("p").get_text()

    product_informations = soup.find("table", {"class": "table table-striped"})
    liste_product_information = product_informations.find_all("td")
    upc = liste_product_information[0].get_text()
    price_including_tax = liste_product_information[3].get_text()
    price_excluding_tax = liste_product_information[2].get_text()
    number_available = liste_product_information[5].get_text()
    review_rating = liste_product_information[6].get_text()

    image_livre = soup.find("div", {"class":"item active"}).find_next('img')
    image_url = image_livre['src']

    #création d'un dictionnaire contenant les informations d'un livre
    informations_livre = {
        'url_produit' : page_product_url,
        "titre" : title,
        "categorie" : categorie,
        "description" : product_description,
        "code_produit" : upc,
        "prix_avec_tax" : price_including_tax,
        "prix_sans_tax" : price_excluding_tax,
        "stock" : number_available,
        "note_evaluation" : review_rating,
        "url_image" : image_url,
    }

    return informations_livre

#Création d'une liste pour stocker toutes les informations des livres
informations_completes_livres = []

#Création d'une boucle pour explorer toutes les pages du site
for numero_page in range (1,51): #50 pages en tout 
    url = "http://books.toscrape.com/catalogue/category/books_1/page-{numero_page}.html"
    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, "html.parser")
    print(numero_page)


















