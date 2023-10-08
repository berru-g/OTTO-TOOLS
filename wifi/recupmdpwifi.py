import subprocess

def get_wifi_passwords():
    try:
        wifi_profiles = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8", "ignore").split("\n")
        wifi_profiles = [line.split(":")[1].strip() for line in wifi_profiles if "Tous les profils utilisateurs" in line]

        wifi_passwords = {}
        for profile in wifi_profiles:
            try:
                wifi_info = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8", "ignore")
                password_line = [line.strip() for line in wifi_info.split("\n") if "Contenu de la clé" in line][0]
                password = password_line.split(":")[1].strip()
                wifi_passwords[profile] = password
            except subprocess.CalledProcessError:
                wifi_passwords[profile] = "Mot de passe non disponible (nécessite une autorisation d'administrateur)"
        
        return wifi_passwords
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")
        return None

if __name__ == "__main__":
    wifi_passwords = get_wifi_passwords()
    if wifi_passwords:
        print("\nListe des mots de passe WiFi enregistrés :\n")
        for ssid, password in wifi_passwords.items():
            print(f"{ssid} : {password}")
    else:
        print("\nImpossible de récupérer les mots de passe WiFi.")
