import psutil

def get_running_applications():
    # Obtenir la liste des processus en cours d'exécution
    all_processes = list(psutil.process_iter(['pid', 'name']))

    # Filtrer les processus pour n'afficher que les applications
    applications = [process.info for process in all_processes if process.info['name'] != '']
    
    # Afficher les applications
    print("Applications en cours d'exécution :")
    for app in applications:
        print(app['name'])

# Appelez la fonction pour afficher les applications en cours d'exécution
get_running_applications()
