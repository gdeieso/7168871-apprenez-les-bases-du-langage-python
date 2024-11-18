# Écrivez votre code ici !

from bs4 import BeautifulSoup

# Lecture du fichier index.html
with open("P3/P3C2/énoncé/index.html", 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Extraction des informations
# 1. Titre de la page
page_title = soup.title.string

# 2. Texte de la balise <h1>
page_heading = soup.h1.string

# 3. Récupérer les noms et les prix des produits
product_names = [h2.text for h2 in soup.find_all('h2')]
product_prices = [int(p.text.replace('Prix : ', '').replace('€', '')) for p in soup.find_all('p') if 'Prix' in p.text]

# 4. Récupérer les descriptions des produits
product_descriptions = [p.text.replace('Description : ', '') for p in soup.find_all('p') if 'Description' in p.text]

# Conversion des prix en dollars
prices_in_dollars = [f"{int(price * 1.2)}$" for price in product_prices]

# Affichage des informations extraites
print("Titre de la page :", page_title)
print("Texte de la balise <h1> :", page_heading)
print("Produits et leurs prix (en euros) :", list(zip(product_names, product_prices)))
print("Descriptions des produits :", product_descriptions)

# Affichage des nouveaux prix en dollars
products_with_prices_in_dollars = list(zip(product_names, prices_in_dollars))
print("Produits avec les prix en dollars :", products_with_prices_in_dollars)