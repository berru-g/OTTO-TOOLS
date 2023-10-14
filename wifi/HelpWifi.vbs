' Crée une interface utilisateur pour récupérer le mot de passe WiFi en utilisant netsh

Function ExecuteCommand(command)
    Dim objShell, objExec
    Set objShell = CreateObject("WScript.Shell")
    Set objExec = objShell.Exec(command)
    ExecuteCommand = objExec.StdOut.ReadAll
End Function

' récupérer le mot de passe WiFi
Sub GetWifiPassword
    ' Récupérer le nom de la box entré par l'utilisateur
    boxName = InputBox("Entrez le nom de la box WiFi :")

    ' Vérifier si l'utilisateur a entré un nom de box
    If boxName <> "" Then
        command = "netsh wlan show profile """ & boxName & """ key=clear"
        result = ExecuteCommand(command)

        MsgBox "Mot de passe WiFi pour " & boxName & " :"  & result
                ' Afficher les informations dans une fenêtre de message avec une taille plus grande
       ' Set objShell = CreateObject("WScript.Shell")
       ' objShell.Popup result, 0, "Informations WiFi pour " & boxName, 64 + 4096, 0
    Else
        MsgBox "Veuillez entrer un nom de box WiFi valide."
    End If
End Sub

GetWifiPassword
