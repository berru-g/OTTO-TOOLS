"""    Learn python 
      github/berru-g 23
"""
from pyautogui import sleep
import requests
from bs4 import BeautifulSoup
import webbrowser

print("--- CONCU SEARCH PRICE ---")
print("Entrez le titre du poste:")
job = input("")

concurence_url = "https://candidat.pole-emploi.fr/offres/recherche?&motsCles={}&lieux{}&offresPartenaires=true&rayon=10&tri=0"

concurence_search = requests.get(concurence_url.format(job))
concurence_soup = BeautifulSoup(concurence_search.text, "html.parser")
concurence_titles = concurence_soup.find_all(class_="media-heading-title")
subtitles = concurence_soup.find_all(class_="subtext")
prices = concurence_soup.find_all(class_="price")

print("Résultats de la recherche :")

# Print the titles
for title in concurence_titles:
    for subtitle in subtitles:
        for price in prices:
            print(title.text)
            print(subtitle.text)
            print(price.text)
            print("__________")

sleep(1)

print("Voulez-vous ouvrir une page web ? oui ou non")
reponse_web = input()
if reponse_web.lower() == "oui":
    print("Quelle est l'URL de la page web que vous souhaitez ouvrir ?")
    url = input()
    webbrowser.open(url)
elif reponse_web.lower() == "non":
    print("Vous avez choisi de ne pas ouvrir de page web.")
else:
    print("Je ne comprends pas votre réponse.")
    print("Aidez nous à améliorer cet outil, rdv sur github.com/berru-g")
sleep(100)
exit()
