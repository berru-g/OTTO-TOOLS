import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def open_url_at_8am(url):
    # Récupérer l'heure actuelle
    current_time = time.localtime()

    # Attendre jusqu'à 8h si nécessaire
    while current_time.tm_hour < 8:
        time.sleep(60)  # Attendre 1 minute avant de vérifier l'heure suivante
        current_time = time.localtime()

    # Ouvrir l'URL avec requests
    response = requests.get(url)

    if response.status_code == 200:
        print("Contenu de la page :", response.text)
    else:
        print("La requête a échoué avec le code d'état :", response.status_code)
#Créez une fonction pour effectuer un clic à un endroit défini sur la page avec Selenium :
def click_element_at_location(url, x, y):
    # Ouvrir l'URL avec Selenium
    driver = webdriver.Chrome()  # Utilisez le navigateur de votre choix (Chrome, Firefox, etc.)

    driver.get(url)

    # Attendre un court instant pour permettre au chargement de la page de se terminer
    time.sleep(2)

    # Trouver l'élément à cliquer en utilisant les coordonnées x et y
    element = driver.find_element(By.XPATH, f'//*[contains(@onclick,"{x},{y}")]')

    # Effectuer le clic à l'endroit spécifié
    action = ActionChains(driver)
    action.move_to_element(element).click().perform()

    # Fermer le navigateur après le clic
    driver.quit()
#Appelez les fonctions avec l'URL et les coordonnées spécifiées :
url = "https://www.example.com"
open_url_at_8am(url)

click_x = 100
click_y = 200
click_element_at_location(url, click_x, click_y)
