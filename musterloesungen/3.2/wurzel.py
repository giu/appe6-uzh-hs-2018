# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      3.2

import math

def wurzel(a,b):
    produkt = a * b
    if produkt < 0:
        print("Fehler: Produkt ist negativ")
    else:
        print(math.sqrt(produkt))

wurzel(-4,4)
wurzel(-3,-3)
wurzel(1,2)