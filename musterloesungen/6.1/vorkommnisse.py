# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      6.1
 
def anz_vorkommnisse(zeichen, wort):
    # Diese Variable verwenden wir, um die Anzahl Vorkommnisse zu zählen
    counter = 0
    for buchstabe in wort:
        if buchstabe == zeichen:
            counter = counter + 1

    return counter

print(anz_vorkommnisse("a", "Halleluja"))
print(anz_vorkommnisse("e", "Mount Everest"))
print(anz_vorkommnisse("k", "Kathedrale"))