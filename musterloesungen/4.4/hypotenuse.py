# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      4.4

import math

def hypotenuse(a,b):
    if a < 0 or b < 0:
        return 

    summe_quadrat = a**2 + b**2
    c = math.sqrt(summe_quadrat)
    return c


print(hypotenuse(0,0))
print(hypotenuse(3,4))

hypotenuse_mit_negativer_seitenlaenge = hypotenuse(-1,2)

if hypotenuse_mit_negativer_seitenlaenge == None:
    print("Fehler: Eine negative Seitenlänge wurde angegeben")