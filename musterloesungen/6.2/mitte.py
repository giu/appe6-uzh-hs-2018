# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      6.2

def mitte(liste):
    # Kopiere zuerst alle Elemente in eine neue Liste
    neue_liste = liste[:]
    # Entferne nun das erste und das letzte Element aus der neuen Liste
    del neue_liste[0]
    del neue_liste[-1]

    return neue_liste

print(mitte([1,2,3,4]))
print(mitte([1,3,2]))
print(mitte([3,2,5,20,5,100]))