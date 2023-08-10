from appium import webdriver
import time

# Configuration des paramètres de l'appareil
desired_caps = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "Redmi_10C",
    "appPackage": "com.weward",
    "appActivity": "com.weward"
}

# Adresse du serveur Appium
appium_server_url = "http://localhost:4723/wd/hub"

# Initialisation de la session WebDriver avec les paramètres et l'adresse du serveur Appium
driver = webdriver.Remote(appium_server_url, desired_caps)

# Boucle pour obtenir les coordonnées lors des taps
try:
    while True:
        location = driver.get_location()
        print(f"Coordonnées X : {location['x']}, Coordonnées Y : {location['y']}", end="\r")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nArrêt de l'affichage des coordonnées de tap.")

# Fermez la session WebDriver
driver.quit()
