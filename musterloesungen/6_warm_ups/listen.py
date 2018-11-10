# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      Warm-Up: Listen besser kennenlernen

def liste_anpassen(liste): 
    if len(liste) < 3:
        print("Fehler: Die Liste enthält zu wenig Elemente")
        return

    # Erstes Element ändern
    liste[0] = 0
    # Drittes Element ändern
    liste[2] = 0

    for element in liste:
        print(element)


liste = [1,2,3,4]
liste_anpassen(liste)