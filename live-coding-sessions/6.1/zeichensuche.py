# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Session:      6.1

def suche(zeichen, wort):
    # Aktuelle Position im Wort
    position = 0
    # Boolesche Variable um festzuhalten, ob wir das Zeichen gefunden haben
    ist_zeichen_vorhanden = False
    
    for buchstabe in wort:
        # Falls wir das Zeichen finden, können wir gleich True zurückgeben
        if zeichen == buchstabe:
            return True

    # Da wir oben True zurückgeben sobald wir das Zeichen gefunden haben, 
    # bedeutet dies, dass wir aus der Funktion rausspringen. 
    # Sind wir aus der Funktion nicht rausgesprungen während der Ausführung der for-Schleife,
    # so wissen wir, dass wir das Zeichen definitiv nicht gefunden haben: wir können nun
    # also False zurückgeben
    return False

print("Befindet sich der Buchstabe 't' in 'Python'?", suche("t", "Python"))
print("Befindet sich der Buchstabe 'J' in 'Python'?", suche("J", "Python"))