# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      6.3

def durchschnitt(zahlen):
    # Um den Durchschnitt zu berechnen, benötigen wir zuerst die
    # Summe bestehnd aus allen Zahlen
    summe = 0
    for zahl in zahlen:
        summe = summe + zahl

    # Der Durchschnitt berechnet sich aus der Summe aller Zahlen
    # dividiert durch die Anzahl Zahlen
    anzahl_zahlen = len(zahlen)

    avg = summe / float(anzahl_zahlen)

    return avg

print(durchschnitt([1,2,3,4]))
print(durchschnitt([4,18,30,-20]))
print(durchschnitt([3,3,3,3]))