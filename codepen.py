import time
import random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

#Téléchargez le pilote geckodriver à partir du site officiel : https://github.com/mozilla/geckodriver/releases
# Spécifiez le chemin d'accès complet au binaire Firefox (geckodriver)
firefox_binary_path = '/chemin_vers_geckodriver/geckodriver'  # Remplacez par le chemin correct pour votre système

# Configuration du navigateur Firefox
options = Options()
options.binary_location = firefox_binary_path

# Délai aléatoire entre 0.5 et 1.2 seconde
def random_delay():
    return random.uniform(0.5, 1.2)

# Automatisation des clics sur les boutons
def automate_clicks():
    driver = webdriver.Firefox(options=options)

    driver.get("https://codepen.io/trending")  # Remplacez par l'URL de votre application

    time.sleep(5)  # Attendre quelques secondes pour que l'application se charge

    for _ in range(10):  # Répéter la boucle 10 fois
        # Cliquez sur le bouton "Love"
        love_button = driver.find_element(By.CSS_SELECTOR, ".Button-module_root-xw+9D.ContentGridItemMeta-module_stat-9ZbUV.loves.heart-button")
        love_button.click()

        # Attendre aléatoirement entre 0.5 et 1.2 seconde
        time.sleep(random_delay())

        # Cliquez sur le bouton "Next Page"
        next_page_button = driver.find_element(By.XPATH, "//button[@aria-label='Next Page']")
        next_page_button.click()

        # Attendre aléatoirement entre 0.5 et 1.2 seconde avant la prochaine itération
        time.sleep(random_delay())

    driver.quit()

# Exécution du script
if __name__ == "__main__":
    automate_clicks()
