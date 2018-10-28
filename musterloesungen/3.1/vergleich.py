# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      3.1

import math

def vergleich(a,b):
    if a > b:
        print("Erste Zahl ist grösser als zweite Zahl")
    elif a < b:
        print("Erste Zahl ist kleiner als zweite Zahl")
    else:
        print("Beide Zahlen sind gleich gross")

vergleich(1,2)
vergleich(100,2)
vergleich(123,123)