"""    Learn python 
      github/berru-g 23
"""
import requests
from bs4 import BeautifulSoup

print("--POLAMPLOA--")
print("Entrez le titre du poste:")
job = input("")
print("Entrez l emplacement:")
location = input("")

poleemploi_url = "https://candidat.pole-emploi.fr/offres/recherche?&motsCles={}&lieux={}&offresPartenaires=true&rayon=10&tri=0"

poleemploi_search = requests.get(poleemploi_url.format(job, location))
poleemploi_soup = BeautifulSoup(poleemploi_search.text, "html.parser")
poleemploi_titles = poleemploi_soup.find_all(class_="media-heading-title")
subtitles = poleemploi_soup.find_all(class_="subtext")
dates = poleemploi_soup.find_all(class_="date")

print("Résultats de la recherche sur Polamploa:")

for title in poleemploi_titles:
    for subtitle in subtitles:
        for date in dates:
            print(title.text)
            print(subtitle.text)
            print(date.text)
            print("__________")

exit()
