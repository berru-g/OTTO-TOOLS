tasks = []

while True:
    print("Options :")
    print("Tapez 'add' pour ajouter une tâche")
    print("Tapez 'list' pour afficher la liste de tâches")
    print("Tapez 'quit' pour quitter le programme")
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        task = input("Entrez une nouvelle tâche : ")
        tasks.append(task)
    elif user_input == "list":
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Option non valide")
