' Crée une interface utilisateur pour récupérer le mot de passe WiFi en utilisant netsh

' Fonction pour exécuter une commande et renvoyer la sortie
Function ExecuteCommand(command)
    Dim objShell, objExec
    Set objShell = CreateObject("WScript.Shell")
    Set objExec = objShell.Exec(command)
    ExecuteCommand = objExec.StdOut.ReadAll
End Function

' Fonction pour récupérer le mot de passe WiFi
Sub GetWifiPassword
    ' Récupérer le nom de la box entré par l'utilisateur
    boxName = InputBox("Entrez le nom de la box WiFi :")

    ' Vérifier si l'utilisateur a entré un nom de box
    If boxName <> "" Then
        ' Exécuter la commande netsh pour récupérer le mot de passe WiFi
        command = "netsh wlan show profile """ & boxName & """ key=clear"
        result = ExecuteCommand(command)

        ' Afficher le résultat dans une fenêtre de message
        MsgBox "Mot de passe WiFi pour " & boxName & " :" & vbCrLf & vbCrLf & result
    Else
        ' Si l'utilisateur n'a pas entré de nom de box, afficher un message d'erreur
        MsgBox "Veuillez entrer un nom de box WiFi valide."
    End If
End Sub

' Appeler la fonction pour récupérer le mot de passe WiFi
GetWifiPassword
