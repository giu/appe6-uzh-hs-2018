# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      5.1

# Die Anzahl Versuche, die der Benutzer bis jetzt gebraucht hat
anzahl_versuche = 0

# Die maximale Anzahl Versuche, die der Benutzer hat
max_anzahl_versuche = 3

# Die korrekten Logindaten
richtiger_benutzername = "user"
richtiges_passwort = "mypass"

# Eine Variable um festzuhalten, ob der Benutzer sich erfolgreich eingeloggt hat
ist_login_erfolgreich = False

while anzahl_versuche < max_anzahl_versuche:
    benutzername = input("Bitte Benutzername eingeben: ")
    passwort = input("Bitte Passwort eingeben: ")

    if benutzername == richtiger_benutzername and passwort == richtiges_passwort:
        # Benutzer hat sich erfolgreich eingeloggt
        ist_login_erfolgreich = True
        # Wir verlassen die while-Schleife deshalb
        break
    else:
        anzahl_versuche = anzahl_versuche + 1
        print("Falsches Login (Fehlversuch " + str(anzahl_versuche) + " von " + str(max_anzahl_versuche) + ")")

if ist_login_erfolgreich:
    print("Login erfolgreich!")
else:
    print("Leider wurden die Logindaten", anzahl_versuche, "mal falsch eingegeben; Du bist nun gesperrt!")
