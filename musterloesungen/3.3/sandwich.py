# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      3.3

def ist_sandwich(x,y,z):
    if x <= y and y <= z:
        print("Ist ein Sandwich")
    else:
        print("Ist kein Sandwich")

ist_sandwich(3,1,2)
ist_sandwich(1,3,2)
ist_sandwich(1,2,3)