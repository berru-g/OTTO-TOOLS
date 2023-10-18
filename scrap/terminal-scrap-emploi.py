"""    Learn python 
      github/berru-g 23
"""

from pyautogui import sleep
import requests
from bs4 import BeautifulSoup
import webbrowser
from pyfiglet import Figlet
# font: slant, isometric1 et 2
f = Figlet(font='isometric1')
print (f.renderText('PolAmploa'))
 
print("╭─────────────────────────────╮")
print("| Entrez le titre du poste:   |")
print("╰─────────────────────────────╯")
job = input("")
print("╭─────────────────────────────╮")
print("| Entrez l emplacement:       |")
print("╰─────────────────────────────╯")
location = input("")
print(" ────────────────────────────")

#poleemploi_url = "https://candidat.pole-emploi.fr/offres/recherche?lieux={}&motsCles={}&offresPartenaires=true&range=0-19&rayon=10&tri=0"
poleemploi_url = "https://candidat.pole-emploi.fr/offres/recherche?&motsCles={}&lieux{}&offresPartenaires=true&rayon=10&tri=0"
"""jeudisdotcom_url = "https://www.lesjeudis.com/recherche?keywords={}&location={}"
indeed_url = "https://fr.indeed.com/emplois?q={}&l={}"""

# Search Pole Emploi
poleemploi_search = requests.get(poleemploi_url.format(job, location))
poleemploi_soup = BeautifulSoup(poleemploi_search.text, "html.parser")
poleemploi_titles = poleemploi_soup.find_all(class_="media-heading-title")
subtitles = poleemploi_soup.find_all(class_="subtext")
dates = poleemploi_soup.find_all(class_="date")

print("Résultats de la recherche sur Pole Emploi:")

# Print the titles
for title in poleemploi_titles:
    for subtitle in subtitles:
        for date in dates:
            print(title.text)
            print(subtitle.text)
            print(date.text)
            print("__________")

sleep(1)
"""
# Search jeudisdotcom.com
jeudisdotcom_search = requests.get(jeudisdotcom_url.format(job, location))
jeudisdotcom_soup = BeautifulSoup(jeudisdotcom_search.text, "html.parser")
jeudisdotcom_titles = jeudisdotcom_soup.find_all(class_=["data-results-title.dark-blue-text.b" , "data-results-content block job-listing-item"])

print("Résultats de la recherche sur jeudis.com:")
for title in jeudisdotcom_titles:
    print(title.text)

sleep(1)
 
# Search Indeed.com
indeed_search = requests.get(indeed_url.format(job, location))
indeed_soup = BeautifulSoup(indeed_search.text, "html.parser")
indeed_titles = indeed_soup.find_all(id_=["jobTitle-37b88858c4da5049","jobTitle css-1h4a4n5 eu4oa1w0"]) # [.,.] recup une class si l'autre n'existe pas. # [.,.] recup une class si l'autre n'existe pas.

print("Résultats de la recherche sur Indeed.com:")
for title in indeed_titles:
    print(title.text)
    
sleep(1)

print("Fin des résultats")


print("Voulez-vous ouvrir une page web ?")
reponse_web = input()
if reponse_web.lower() == "oui":
    print("Quelle est l'URL de la page web que vous souhaitez ouvrir ?")
    url = input()
    webbrowser.open(url)
elif reponse_web.lower() == "non":
    print("Vous avez choisi de ne pas ouvrir de page web.")
else:
    print("Je ne comprends pas votre réponse.")
    print("Aidez nous à améliorer cet outil, rdv sur github.com/berru-g")"""
sleep(20)
exit()
