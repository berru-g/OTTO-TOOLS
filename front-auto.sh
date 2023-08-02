#!/bin/bash

# Chemin du dossier "new project" dans le dossier "Documents"
folder_path="$HOME/Documents/new project"

# Vérifier si le dossier existe déjà, sinon le créer
if [ ! -d "$folder_path" ]; then
    mkdir -p "$folder_path"
fi

# Créer les fichiers index.html, style.css et script.js dans le dossier
index_file="$folder_path/index.html"
style_file="$folder_path/style.css"
script_file="$folder_path/script.js"

echo "<!DOCTYPE html>" > "$index_file"
echo "<html>" >> "$index_file"
echo "<head>" >> "$index_file"
echo "  <title>My New Project</title>" >> "$index_file"
echo "</head>" >> "$index_file"
echo "<body>" >> "$index_file"
echo "  <h1>Hello, world!</h1>" >> "$index_file"
echo "</body>" >> "$index_file"
echo "</html>" >> "$index_file"

echo "/* CSS styles */" > "$style_file"
echo "body {" >> "$style_file"
echo "  background-color: #f0f0f0;" >> "$style_file"
echo "}" >> "$style_file"
echo "h1 {" >> "$style_file"
echo "  color: #00f;" >> "$style_file"
echo "}" >> "$style_file"

echo "// JavaScript code" > "$script_file"
echo "document.addEventListener('DOMContentLoaded', function() {" >> "$script_file"
echo "  console.log('Hello, world!');" >> "$script_file"
echo "});" >> "$script_file"

# Ouvrir Visual Studio Code depuis le dossier du nouveau projet
code "$folder_path"
