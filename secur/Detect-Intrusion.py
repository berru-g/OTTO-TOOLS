import os

# Répertoire à surveiller
directory_to_monitor = 'C:\\Users\\Documents'

# Crée un dictionnaire pour stocker les hachages des fichiers
file_hashes = {}

# Fonction pour calculer le hachage d'un fichier
def calculate_hash(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    return hash(data)

# Fonction pour vérifier l'intégrité des fichiers
def check_integrity():
    for filename in os.listdir(directory_to_monitor):
        file_path = os.path.join(directory_to_monitor, filename)
        current_hash = calculate_hash(file_path)
        
        if filename in file_hashes:
            if current_hash != file_hashes[filename]:
                print(f'Alerte ! Le fichier {filename} a été modifié !')
        else:
            file_hashes[filename] = current_hash

# Surveiller en continu
while True:
    check_integrity()
