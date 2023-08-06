Dim fso, folder, indexFile, styleFile, scriptFile, shell, folderPath

' Créer une instance de FileSystemObject
Set fso = CreateObject("Scripting.FileSystemObject")

' Chemin du dossier "new project" dans le dossier "Documents"
folderPath = fso.BuildPath(WScript.CreateObject("WScript.Shell").SpecialFolders("MyDocuments"), "new project")

' Vérifier si le dossier existe déjà, sinon le créer
If Not fso.FolderExists(folderPath) Then
    Set folder = fso.CreateFolder(folderPath)
End If

' Créer les fichiers index.html, style.css et script.js dans le dossier
Set indexFile = fso.CreateTextFile(fso.BuildPath(folderPath, "index.html"), True)
indexFile.WriteLine("<!DOCTYPE html>")
indexFile.WriteLine("<html>")
indexFile.WriteLine("<head>")
indexFile.WriteLine("  <title>My New Project</title>")
indexFile.WriteLine("</head>")
indexFile.WriteLine("<body>")
indexFile.WriteLine("  <h1>Hello, world!</h1>")
indexFile.WriteLine("  <p>sub-title</p>")
indexFile.WriteLine("</body>")
indexFile.WriteLine("</html>")
indexFile.Close

Set styleFile = fso.CreateTextFile(fso.BuildPath(folderPath, "style.css"), True)
styleFile.WriteLine("/* CSS styles */")
styleFile.WriteLine("body {")
styleFile.WriteLine("  background-color: #f0f0f0;")
styleFile.WriteLine("}")
styleFile.WriteLine("h1 {")
styleFile.WriteLine("  color: #00f;")
styleFile.WriteLine("}")
styleFile.Close

Set scriptFile = fso.CreateTextFile(fso.BuildPath(folderPath, "script.js"), True)
scriptFile.WriteLine("// JavaScript code")
scriptFile.WriteLine("document.addEventListener('DOMContentLoaded', function() {")
scriptFile.WriteLine("  console.log('Hello, world!');")
scriptFile.WriteLine("});")
scriptFile.Close

' Ouvrir le dossier du nouveau projet dans l'explorateur de fichiers
Set shell = CreateObject("Shell.Application")
shell.Open folderPath
