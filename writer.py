import csv

def write_csv(filename, en_tete, all_book_data):
    #création d'un fichier csv pour écrire dans le fichier appelé data.csv
    with open(filename, "w", newline='', encoding='utf-8') as fichier_csv:
        #création d'un objet writer pour ce fichier avec un délimiteur
        writer = csv.writer(fichier_csv, delimiter=',')
        #création de la premiere ligne du fichier avec writer.writerow
        writer.writerow(en_tete)
        for book_data in all_book_data:
            writer.writerow(book_data)

if __name__ == '__main__':
    en_tete = ['header1', 'header2']
    book_data = [
        ['a', 'b'],
        ['j', 'c']
    ]
    filename = "data2.csv"
    write_csv(filename, en_tete, book_data)
