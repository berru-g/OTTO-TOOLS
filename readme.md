#### Crée un ficher front dans Documents, contenant; html, css, js et md puis l'ouvre dans vscode en un double click

    This script allows you to create a folder in your 'documents', including an html, css, js and readme file, then open it in Vscode, with just a double click.

```mermaid
graph LR
A[Documents] -- create --> B((new-project))
B[new-project] --> C{index.html}
B[new-project] --> D{style.CSS}
B[new-project] --> E{script.js}
C{index.html} --> F[vscode]
D{style.CSS} --> F[vscode]
E{script.js} --> F[vscode]
```

    coordonateCMD.py affiche les valeurs X et Y en temps réel / Interface
    coordonateInterface.py permet en plus de copier les coordonées d'un click puis de les afficher

#### Other Tool's
 - [Alarm crypto](https://github.com/berru-g/api-crypto-tool-s)  
 - [Wallet](https://github.com/berru-g/All-in-one-dashboard)
