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
    categorie_names = []
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
        categorie_names.append(nom)
    
    del pages_categories_full[0]

    # while True :
    #     for v in pages_categories_full :
    #         next_response = requests.get(v)
    #         next_pages = next_response.content
    #         next_soup = BeautifulSoup(next_pages,"html.parser")
    #         get_page_suivante = soup.find("li",{"class":"next"}).get("href")
    #         pages_suivantes = full_url + str(get_page_suivante)
    #         pages_categories_full.append(pages_suivantes)
    
    return pages_categories_full, categorie_names


def get_all_books_url(url):
    all_urls = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # récupérer les livres de la page
    page_urls = get_books_from_page(soup)
    all_urls.extend(page_urls)

    next_button = soup.find("li",{"class":"next"})
    while next_button is not None:
        index_url = ''
        full_url = index_url + next_button.get('href')
        response = requests.get(full_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # récupérer les livres de la page
        page_urls = get_books_from_page(soup)
        all_urls.extend(page_urls)

        next_button = soup.find('li', {'class': 'next'})
    
    return all_urls
