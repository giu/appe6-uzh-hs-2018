# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      4.2

def celsius(f):
    c = (f - 32) * 5 / 9
    return c

print(celsius(33.8))
print(celsius(50))
print(celsius(95))
