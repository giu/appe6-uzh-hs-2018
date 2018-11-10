# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Session:      6.3

def div_mit_rest(a,b):
    # Wir wandeln das Resultat der Division in einen int um, 
    # damit allfällige Nachkommastellen gestrichen werden
    quotient = int(a/b)
    rest = a % b

    return quotient, rest

print("Ergebnis (mit Rest) von 10 / 3: ", div_mit_rest(10, 3))
print("Ergebnis (mit Rest) von 12 / 4: ", div_mit_rest(12, 4))
print("Ergebnis (mit Rest) von 28 / 5: ", div_mit_rest(28, 5))