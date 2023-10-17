"""    Learn python 
      github/berru-g 23
      Outil pour comparer les prix de vente de ses concurents
"""
#next step: interface web
import time
import requests
from bs4 import BeautifulSoup

print("Entrez le produit recherché:")
product = input("")

first_url = "https://www.leroymerlin.fr/search?q={}"

# Search first
first_search = requests.get(first_url.format(product))
print("request")
first_soup = BeautifulSoup(first_search.text, "html.parser")
print("parser")
first_titles = first_soup.find_all(class_="km-tile-designation")
print("title")
subtitles = first_soup.find_all(class_="mu-ml-050")
print("sub")
prices = first_soup.find_all(class_="js-main-price")
print("price")

print("Résultats de la recherche du concurent 1:")
 
# Print the titles
for title in first_titles:
    for subtitle in subtitles:
        for price in prices:
            print(title.text)
            print(subtitle.text) 
            print(price.text) 
            print("__________")
time.sleep(2)
 
print("Fin des résultats")
print("Si aucun resultat n'est trouvé alors changer le nom des class dans le script")
print("_______________")
time.sleep(4)
exit()
