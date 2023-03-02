import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, 'html.parser')

page_product_url = response.url
print(page_product_url)

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

#class = "price_color" pour les prix des livres
'''product_page_url ok 
● universal_ product_code (upc) ok
● title ok
● price_including_tax ok
● price_excluding_tax ok 
● number_available ok 
● product_description ok
● category ok
● review_rating ok
● image_url  ok'''