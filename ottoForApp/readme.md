Dans cet exemple, les coordonnées (x, y) que vous avez fournies sont définies dans la liste tap_coordinates. Le script tapera sur chaque point de la liste et attendra la durée spécifiée dans pause_time (en secondes) entre chaque tap. Le script répétera cette séquence de tap 10 fois.

N'oubliez pas de remplacer les valeurs dans VERSION_ANDROID_DE_VOTRE_APPAREIL, NOM_DE_VOTRE_APPAREIL, com.android.calculator2, com.android.calculator2.Calculator, et d'ajuster les coordonnées tap_coordinates selon vos besoins.

N'hésitez pas à personnaliser ce script en fonction de votre application et de vos besoins spécifiques.

Connectez votre appareil Android à votre ordinateur.

Ouvrez une fenêtre de terminal (ou invite de commande) et exécutez la commande suivante pour obtenir la liste des packages installés sur votre appareil :

        adb shell pm list packages

Vous verrez une liste de packages. Cherchez le nom de package associé à l'application dont vous souhaitez automatiser les actions.