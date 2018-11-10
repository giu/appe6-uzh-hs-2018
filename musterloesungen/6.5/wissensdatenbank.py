# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      6.5; Vorgegebenes Grundgerüst für alle Teilaufgaben von 6.5

# In dieses Dictionary fügen wir Stichworte inkl. Beschreibungen hinzu
wissensdatenbank = {
    "Python":       "Python ist eine interpretierte Programmiersprache",
    "Interpreter":  "Ein Interpreter ist ein Computerprogramm, das einen Quellcode einliest, analysiert und ausführt",
    "Programmierung": "Programmierung bezeichnet die Tätigkeit, Computerprogramme zu erstellen"
}

print("==============================")
print("Wissensdatenbank Version 6.5.0")
print("==============================")

befehl = input("Befehl: ")

# Die Befehlseingabe; wird nur durch Eingabe von 'exit' beendet
while befehl != "exit":
	if befehl == "exit":
		break
	else:
		print("Befehl existiert nicht!")

	befehl = input("Befehl: ")

print("Auf wiedersehen!")