# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      3.4

def vorschlag_reise(anzahl_kilometer):
    if anzahl_kilometer < 3.2:
        print("Tritt die Reise zu Fuss an!")
    elif anzahl_kilometer >= 3.2 and anzahl_kilometer < 100:
        print("Tritt die Reise mit dem Auto an!")
    else:
        print("Buch Dir einen Flug!")


vorschlag_reise(102)
vorschlag_reise(2.3)