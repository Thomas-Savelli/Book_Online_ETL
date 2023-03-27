from fonctions import extract_book_data, get_url_categories, get_all_books_url
import csv
import os
import requests
 
if __name__ == '__main__':
    
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

        all_books_data = []
        for book_url in books_urls:
            book_data = extract_book_data(book_url)
            all_books_data.append(book_data)
           
        # création du dossier csv_data s'il n'existe pas déjà
        if not os.path.exists("csv_data"):
            os.mkdir("csv_data")

        # CREATION FICHIER CSV PAR CATEGORIE
        # Création d'un nom de fichier en combinant le nom de la catégorie et l'extension CSV
        filename = os.path.join("csv_data", f"{categorie_names[url_categories.index(url)]}.csv")
        
        # Ouvrir le fichier CSV en mode écriture
        with open(filename, mode="w", newline='', encoding="utf-8") as csv_file:
            
            # Créer un objet writer CSV
            writer = csv.writer(csv_file)
            # Écrire la ligne d'en-tête dans le fichier CSV
            writer.writerow(en_tete)
            # Écrire les données des livres dans le fichier CSV
            writer.writerows(all_books_data)    

        # créer un fichier images_data si inexistant et télécharger les images de chaques livres
        if not os.path.exists('images_data'):
            os.mkdir("images_data")
        # Boucle pour itérer sur chaques url de livre
        for book_data in all_books_data:
            image_url = book_data[-1]
            # titre images = upc car unique
            title = book_data[1]
            image_data = requests.get(image_url).content
            
            with open(f"images_data/{title}.jpg", "wb") as f:
                f.write(image_data)