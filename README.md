# Books Online / Systeme de Surveillance des prix  


Ce programme a pour objectif de faciliter la tâche de suivi des prix des livres d'occasion sur les sites web de concurrents de Books Online. Il s'agit d'un scraper développé en Python qui extrait les informations tarifaires d'autres librairies en ligne. Dans cette version bêta, le programme se concentre sur la récupération des prix chez un revendeur de livres en ligne nommé Books to Scrape, au moment de son exécution. L'application est développée pour être exécutable à la demande et ne surveille pas les prix en temps réel sur la durée. Il permettra à Books Online de gagner du temps et de rester compétitif sur le marché.

## **Pour commencer**

Télécharger l’intégralité du repository sur : https://github.com/Thomas-Savelli/Books_Online_ETL.git

### 1/ Pré-requis

Assurez-vous de posséder l’intégralité du repository : 

- main.py
- fonctions.py
- requirements.txt
- .gitignore
- README.md

### 2/ Installation

Une fois le repository téléchargé et stocké localement : 

- ouvrez votre terminal et rendez-vous dans le dossier contenant l’intégralité des fichiers du repository.
    `` cd '.\Desktop\OpenClassrooms\Parcours DA PYTHON\Projet 2\soutenance_p2\' ``

- Créer un environnement virtuel afin de récupérer les dépendances et packages du projet.  
    *exemple procedure* : ``python -m venv env``

- Contrôler avec ``ls`` que vous disposez maintenant d’un dossier **env**. Si ce n’est pas le cas, réitérer cette 
    étape en contrôlant la syntaxe de la ligne de commande. Sinon activer votre nouvel environnement virtuel. 

    *exemple procédure (powershell):* ``.\env\Scripts\activate``   
    *exemple procédure (windows):* ``.\env\Scripts\activate.bat``  
    *exemple procédure (autres): ``source env/bin/activate``

    Si vous rencontrez des difficultés vous pouvez vous référer sur le site : 
    *https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows/18713789#18713789*

    Pour contrôler la réussite de cette manœuvre, vous devriez avoir un (env) devant votre ligne de commande :    
    ``(env) PS C:\Users\thoma\Desktop\OpenClassrooms\Parcours DA PYTHON\Projet 2\soutenance_p2>``  
    
    PS : Taper seulement ``deactivate`` pour fermer ce dernier.  
- Pour finir, télécharger avec **pip** les packages et dépendances requis pour le bon fonctionnement du code avec le requirements.txt en entrant la commande suivante *(dans votre environnement virtuel !)* :   
    ``pip install -r requirements.txt ``  
    Une fois le téléchargement effectué et l'installation terminée, vous êtes prêt à exécuter le code.  

## **Exécuter le programme**

- Dans votre terminal, rendez-vous à l’emplacement  du dossier télécharger et activer votre environnement virtuel.  

- Exécuter le code en tapant la commande : ``python main.py``  

- Attendez que le programme s’exécute complètement, cela peut prendre quelques minutes. 

- Le programme a été exécuté, vous devriez donc disposer des deux dossiers contenant les données extraites à l’intérieur du dossier source :  
    _ **csv_data** : contenant toutes les data scraper au format csv classées par catégorie  
    _ **images_data** : contenant toutes les images enregistrées des livres du site scraper 
  
## **Lecture optimale des données csv**

Dans l'optique où l'ouverture direct d'un fichier csv avec Microsoft Excel rendrait une lecture non optimale, merci d'utiliser cette procédure :

- Ouvrir un tableur Excel vierge
- Selectionner dans le menu >``Données > Données externes > Fichier texte``
- Importer le fichier csv désiré
- Puis dans l'assistant importation de texte sélectionner les configurations suivantes :

        _ type de données d'origine (étape 1 sur 3) : Délimité
        _ Séparateur (étape 2 sur 3) : Virgule
        _ Format de données en colonne (étape 3 sur 3) : Standard
        _ Puis cliquer sur Terminer et OK




## Fabriqué avec

* Python - 3.11.1 - [*https://docs.python.org/fr/3/tutorial/index.html*]  
* requests - 2.28.2 - [*https://requests.readthedocs.io/en/latest/*] - HTTP library   
* BeautifulSoup4 - 4.12.0 - [*https://www.crummy.com/software/BeautifulSoup/*] - Screen-scraping library  
* os - [*https://docs.python.org/fr/3/library/os.html?highlight=os#module-os*] - Diverses interfaces pour le système d'exploitation  
* csv - [*https://docs.python.org/fr/3/library/csv.html?highlight=csv#module-csv*] - Lecture et écriture de fichiers CSV  
* tqdm - [https://pypi.org/project/tqdm/] - indicateur de progression    
* IDE - [*https://code.visualstudio.com/*] - Visual Studio Code     
* PowerShell - [*https://learn.microsoft.com/fr-fr/powershell/scripting/overview?view=powershell-7.3*]  
* GitHub - [*https://github.com/*]   

## Versions

**Dernière version stable :** Beta 1.0  
**Dernière version :** Beta 1.0  

## Auteurs  
* **Sam** - ``Responsable d'équipe - Books Online``
* **Thomas Savelli** [https://github.com/Thomas-Savelli] - ``analyste marketing - Books Online``   



