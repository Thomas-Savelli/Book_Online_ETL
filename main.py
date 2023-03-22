from fonctions import extract_book_data, get_url_categories, get_all_books_url
from writer import write_csv
import requests
from bs4 import BeautifulSoup



if __name__ == '__main__':
    
    product_page = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    book_data = extract_book_data(product_page)
    en_tete = ["product_page_url","universal_product_code (upc)","title","price_including_tax",
                "price_excluding_tax","number_available","product_description","category","review_rating", "image_url"]

    index_url = "http://books.toscrape.com/index.html"

    # trouver les urls de toutes les catégories
    # la liste url_category sert de repertoire principale pour trouver toutes les pages principales des categories
    # la liste categorie_names contient les noms des categories pour une utilisation futur avec les fichiers csv 
    url_categories, categorie_names = get_url_categories(index_url)

    # Boucle pour trouver toutes les pages de livres dans les pages des categories
    for url in url_categories:
        books_urls = get_all_books_url(url)
        print(books_urls)

        all_books_data = []
        # for book_url in books_urls:
        #     book_data = extract_book_data(book_url)
        #     all_books_data.append(book_data)
         
        # write_csv('nomcategor', en_tete, all_books_data)
