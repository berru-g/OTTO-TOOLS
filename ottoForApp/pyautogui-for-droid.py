from appium import webdriver
import time

# Configuration des paramètres de l'appareil
desired_caps = {
    "platformName": "Android",
    "platformVersion": "11",  # Par exemple, "11"
    "deviceName": "Redmi_10C",  # Par exemple, "Android Emulator" ou le nom de votre appareil physique
    "appPackage": "com.weward",  # Le package de l'application Calculatrice (exemple)
    "appActivity": "com.weward"  # L'activité de l'application Calculatrice (exemple)
}

# Adresse du serveur Appium
appium_server_url = "http://localhost:4723/wd/hub"

# Initialisation de la session WebDriver avec les paramètres et l'adresse du serveur Appium
driver = webdriver.Remote(appium_server_url, desired_caps)

# Coordonnées (x, y) pour le point à cliquer
tap_coordinates = [(100, 200), (300, 400), (500, 600), (700, 800), (900, 1000)]

# Nombre de répétitions de la boucle
loop_count = 10

# Temps de pause entre chaque tap (en secondes)
pause_time = 2

for _ in range(loop_count):
    for x, y in tap_coordinates:
        driver.tap([(x, y)])
        time.sleep(pause_time)

# Fermez la session WebDriver
driver.quit()
