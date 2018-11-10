# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      4.1

def vergleiche(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

print(vergleiche(3,1))
print(vergleiche(-1,4))
print(vergleiche(42,42))