# -*- coding: utf-8 -*-
# Kurs:         Python: Grundlagen der Programmierung für Nicht-Informatiker
# Semester:     Herbstsemester 2018
# Homepage:     http://accaputo.ch/kurs/python-uzh-hs-2018/
# Author:       Giuseppe Accaputo
# Aufgabe:      Warm-Up: Dictionaries besser kennenlernen

def preisliste_ausgeben(menu): 
    print("Unsere Preisliste:")
    
    for (gericht, preis) in menu.items():
        print(" *", gericht, ",", preis, "CHF")

menu = {
    "Burger":           10.5,
    "Pommes":           4.0,
    "Chicken Nuggets":  8.25
}

preisliste_ausgeben(menu)