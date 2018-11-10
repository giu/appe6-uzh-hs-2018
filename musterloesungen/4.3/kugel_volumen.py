# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      4.3
# 
import math

def kugel_volumen(r):
    V = 4/3 * math.pi * r**3
    return V


volumen_einheitskugel = kugel_volumen(1)
volumen_null = kugel_volumen(0)

print("kugel_volumen(1):                    ", volumen_einheitskugel,                   "\t Erwartetes Ergebnis:", (4/3 * math.pi))
print("kugel_volumen(0):                    ", volumen_null,                            "\t\t\t Erwartetes Ergebnis:", 0)
print("kugel_volumen(0) + kugel_volumen(1): ", volumen_null + volumen_einheitskugel,    "\t Erwartetes Ergebnis:", (4/3 * math.pi))