# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Session:      6.2

# Wir beginnen mit einer leeren Liste
liste = []

element = input("Neues Element: ")

while element != "exit":
    element = input("Neues Element: ")
    # Wir möchten verhindern, dass wir 'exit' auch noch in die Liste packen
    if element != "exit":
        liste.append(element)



print("Länge der Liste:", len(liste))
print("Elemente: ", liste)