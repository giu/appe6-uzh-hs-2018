# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      6.4

def min_max(zahlen):
    min_wert = min(zahlen)
    max_wert = max(zahlen)

    return [min_wert, max_wert]

print(min_max([102,-2,30,400]))
print(min_max([-123,430,5000,-300]))