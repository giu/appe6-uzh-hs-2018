# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Session:      4.1

import math

def kreisflaeche(radius):
    A = math.pi * radius**2
    return A

# Die nächsten beiden Ausgaben sollten gleich sein,
# da die Fläche eines Kreises mit Radius 1 genau PI beträgt,
# denn wir haben A(1) = PI * 1^2 = PI
print("Berechnete Kreisfläche A(1): ", kreisflaeche(1), "     Erwartetes Ergebnis: ", math.pi)