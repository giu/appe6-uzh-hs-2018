# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      6.5.3

# In dieses Dictionary fügen wir Stichworte inkl. Beschreibungen hinzu
wissensdatenbank = {
    "Python":       "Python ist eine interpretierte Programmiersprache",
    "Interpreter":  "Ein Interpreter ist ein Computerprogramm, das einen Quellcode einliest, analysiert und ausführt",
    "Programmierung": "Programmierung bezeichnet die Tätigkeit, Computerprogramme zu erstellen"
}

print("==============================")
print("Wissensdatenbank Version 6.5.3")
print("==============================")

befehl = input("Befehl: ")

# Die Befehlseingabe; wird nur durch Eingabe von 'exit' beendet
while befehl != "exit":
    if befehl == "exit":
        break

    # Aufgabe 6.5.3
    elif befehl == "insert":
        stichwort = input("Stichwort: ")
        beschreibung = input("Beschreibung: ")

        # Diese Boolesche Variable verwenden wir um herauszufinden, 
        # ob sich das Stichwort bereits in der Datenbank befindet.
        # 
        # Wir müssen dies noch vor dem Hinzufügen abfragen, da wir den 
        # Benutzer darüber informieren wollen, ob ein Stichwort NEU hinzugefügt wurde,
        # oder die Beschreibung eines BESTEHENDEN Stichwortes aktualisiert wurde.
        ist_stichwort_in_datenbank = stichwort in wissensdatenbank

        wissensdatenbank[stichwort] = beschreibung

        # Falls ein Eintrag zum Stichwort bereits existiert informieren wir den Benutzer darüber, 
        # dass die Beschreibung nun aktualisiert wird;
        # ansonsten informieren wir den Benutzer lediglich über dessen Erstellung
        if ist_stichwort_in_datenbank:
            print("Ein Eintrag zum Stichwort '" + stichwort + "' befindet sich bereits in der Wissensdatenbank; die Beschreibung wird nun aktualisiert!")
        else:
            print("Der Eintrag zum Stichwort '" + stichwort + "' wurde neu hinzugefügt!")

    elif befehl == "delete":
        print("delete wurde eingegeben")

    # Aufgabe 6.5.2
    elif befehl == "list":
        for (stichwort, beschreibung) in wissensdatenbank.items():
            print("> " + stichwort + ": " + beschreibung)

    else:
        print("Befehl existiert nicht!")

    befehl = input("Befehl: ")

print("Auf wiedersehen!")