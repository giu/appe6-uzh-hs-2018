# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Session:      4.3

def ist_sandwich(x,y,z):
    if x <= y and y <= z:
        return True
    else:
        return False

# Diese Funktion macht genau dasselbe wie ist_sandwich,
# nur haben wir alles auf eine Zeile komprimiert
def ist_sandwich_einfacher(x,y,z):
    return x <= y and y <= z
    
if ist_sandwich(3,1,2):
    print("Ist ein Sandwich")
else:
    print("Ist kein Sandwich")

if ist_sandwich(1,3,2):
    print("Ist ein Sandwich")
else:
    print("Ist kein Sandwich")

if ist_sandwich(1,2,3):
    print("Ist ein Sandwich")
else:
    print("Ist kein Sandwich")
