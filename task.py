from pyfiglet import Figlet
# font: slant, isometric1 et 2
f = Figlet(font='isometric1')
print (f.renderText('task'))

tasks = []

while True:
    print("add - list or quit")
   
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
